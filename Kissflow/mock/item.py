"""
Module for mock item
"""
import random
from datetime import datetime

from generic import object_to_datetime_dict, generate_pk, get_date
from generic.config import item_prefix, user, flow_name, project_flow_id, model, status_map, start_step, \
    step_ids, steps_map, state_ids, states_map
from generic.constants import PROJECT_FLOW_NAME


class Item:
    """
    Item class
    """
    count = 0

    def __init__(self, **kwargs):
        Item.count += 1
        self.__date = kwargs.get('date', datetime.utcnow())
        self.__date_dict = object_to_datetime_dict(self.__date)
        self.__step_time_taken = 0
        time_period = (datetime.utcnow() - self.__date).days * 1440

        max_time = random.randint(1440, 7200)
        if time_period < max_time:
            max_time = time_period

        self.__time_period = max_time

        self.__config_step = kwargs.get('step')

        self.__item = {}
        self.__project_flow = []
        self.__step = []
        self.__state = []
        self.__activity = []

        self.__current_project_flow = {}
        self.__current_step = {}
        self.__previous_step = {}
        self.__current_state = {}
        self.__previous_state = {}
        self.__current_activity = {}
        self.__previous_activity = {}

    def __del__(self):
        del self.__item
        del self.__project_flow
        del self.__step
        del self.__state
        del self.__activity

        del self.__current_project_flow
        del self.__current_step
        del self.__previous_step
        del self.__current_state
        del self.__current_activity
        del self.__previous_activity

    """ Item """

    def __build_item(self):
        self.__item = {
            'mock': True,
            '_id': f'{item_prefix}{self.count}',
            'Title': f'Item {self.count}',
            '_created_at': self.__date_dict,
            '_created_by': user,
            '_flow_name': flow_name,
            '_modified_at': self.__date_dict,
            '_modified_by': user,
            'Name': f'Item {self.count}',
            '_scheduled_jobs': [],
            '_counter': self.count,
            '_item_id': f'{item_prefix}{self.count}'
        }

    def __update_item(self):
        self.__item.update({
            '_current_activity_log': self.__current_activity['_id'],
            '_start_activity_log': self.__current_activity['_id'],
            '_main_flow_instance': self.__current_project_flow['_id'],
            'ProjectFlowInstance': self.__project_flow,
            'StepInstance': self.__step,
            'StateInstance': self.__state,
            'ActivityLogInstance': self.__activity
        })

    """ ProjectFlowInstance """

    def __build_project_flow_instance(self):
        project_flow = {
            '_id': generate_pk(),
            '_created_at': self.__date_dict,
            '_modified_at': self.__date_dict,
            '_created_by': user,
            '_modified_by': user,
            '_project_flow_type': 'MainProjectFlow',
            '_entered_at': self.__date_dict,
            '_project_flow_id': project_flow_id,
            'Model': model,
            '_project_flow_name': PROJECT_FLOW_NAME,
            'AssignedTo': user
        }

        self.__current_project_flow = project_flow
        self.__project_flow.append(project_flow)

    def __update_project_flow_instance(self):
        status = status_map.get(self.__current_step['_step_type'])

        self.__current_project_flow.update({
            '_current_step_id': self.__current_step['_step_id'],
            '_current_step_name': self.__current_step['_step_name'],
            '_start_step_instance_id': self.__step[0]['_id'],
            '_current_step_instance_id': self.__current_step['_id'],
            '_status': status
        })

        if len(self.__step) > 1:
            self.__current_project_flow.update({'_started_at': self.__step[1]['_entered_at']})

        if status == 'Completed':
            gross_time = self.__step[-1]['_entered_at']['v'] - self.__step[0]['_created_at']['v']
            net_time = self.__date_dict['v'] - self.__current_project_flow['_started_at']['v']

            self.__current_project_flow.update({
                '_completed_at': self.__date_dict,
                "_gross_time": gross_time.total_seconds() / 60.0,
                "_net_time": net_time.total_seconds() / 60.0
            })

        if self.__current_step['_step_type'] == 'UserStep' and self.__current_state:
            self.__current_project_flow.update({
                '_current_state_instance_id': self.__current_state['_id'],
                '_current_state_id': self.__current_state['_state_id'],
                '_current_state_name': self.__current_state['_state_name']
            })

    """ StepInstance """

    def __pick_random_step(self):
        step_id = random.choice(step_ids)

        if step_id == self.__current_step['_step_id']:
            self.__pick_random_step()

        return steps_map.get(step_id)

    def __step_instance(self, step_config):
        step = {
            '_id': generate_pk('Mock-'),
            '_created_at': self.__date_dict,
            '_modified_at': self.__date_dict,
            '_created_by': user,
            '_modified_by': user,
            '_step_id': step_config['Id'],
            '_step_type': step_config['Type'],
            '_project_flow_instance_id': self.__current_project_flow['_id'],
            '_project_flow_id': project_flow_id,
            'Model': model,
            '_step_name': step_config['Name'],
            '_entered_at': self.__date_dict,
            'AssignedTo': user
        }

        self.__previous_step = self.__current_step
        self.__current_step = step
        self.__step.append(step)

    def __update_step_instance(self):
        if self.__previous_step:
            self.__current_step.update({
                '_previous_step_instance_id': self.__previous_step['_id'],
                '_previous_step_id': self.__previous_step['_step_id']
            })

            self.__previous_step.update({
                '_next_step_instance_id': self.__current_step['_id'],
                '_exited_at': self.__date_dict,
                '_time_taken': self.__step_time_taken
            })

    def __set_next_date(self):
        time_period = random.randint(0, self.__time_period)
        self.__date = get_date(self.__date, minutes=time_period)
        self.__date_dict = object_to_datetime_dict(self.__date)
        self.__step_time_taken = self.__time_period - time_period
        self.__time_period -= time_period

    def __step_instance_pipeline(self, step):
        if not self.__current_step or self.__current_step['_step_id'] != step['Id']:
            action = 'ItemMoved' if self.__current_step else 'Initiated'
            self.__set_next_date()
            self.__step_instance(step)
            self.__update_step_instance()
            self.__build_activity_log_instance(action=action)

    def __build_between_steps(self):
        if between := self.__config_step.get('Between'):
            no_of_steps = between.get('NoOfSteps')

            for _ in range(0, random.choice(no_of_steps)):
                step = self.__pick_random_step()
                self.__step_instance_pipeline(step)

                if (states := between.get('States')) and step['Type'] == 'UserStep':
                    no_of_states = states.get('NoOfStates')

                    for _ in range(0, random.choice(no_of_states)):
                        self.__build_state_instance()

    def __build_step_instance(self):
        self.__step_instance_pipeline(start_step)  #: Start step

        #: Config step creation with between step(s)
        if self.__config_step['Type'] != 'StartStep':
            self.__build_between_steps()  #: Between steps
            self.__step_instance_pipeline(self.__config_step)  #: Final steps
            self.__build_state_instance()

    def __update_step_with_state(self):
        self.__current_step.update({
            '_state_instance_id': self.__current_state['_id'],
            '_start_state_instance_id': self.__state[0]['_id'],
            '_state_name': self.__current_state['_state_name'],
            '_state_id': self.__current_state['_state_id']
        })

    """ StateInstance """

    def __pick_random_state(self):
        state_id = random.choice(state_ids)

        if self.__current_state and state_id == self.__current_state['_state_id']:
            self.__pick_random_state()

        return states_map.get(state_id)

    def __update_state_instance(self):
        if self.__previous_state:
            self.__current_state.update({
                '_previous_state_instance_id': self.__previous_state['_id'],
                '_previous_state_id': self.__previous_state['_step_id']
            })

            time_taken = random.randint(0, 100)
            self.__previous_state.update({
                '_next_state_instance_id': self.__current_state['_id'],
                '_exited_at': object_to_datetime_dict(get_date(self.__date, minutes=time_taken)),
                '_time_taken': time_taken
            })

        self.__update_step_with_state()

    def __state_instance(self, chosen_state):
        state = {
            '_id': generate_pk(),
            '_step_instance_id': self.__current_step['_id'],
            '_step_id': self.__current_step['_step_id'],
            '_step_name': self.__current_step['_step_name'],
            '_state_id': chosen_state['Id'],
            '_state_type': chosen_state['Type'],
            '_state_name': chosen_state['Name'],
            '_project_flow_id': project_flow_id,
            'Model': model,
            '_entered_at': self.__date_dict
        }

        self.__previous_state = self.__current_state
        self.__current_state = state
        self.__state.append(state)

    def __build_state_instance(self):
        if self.__current_step['_step_type'] == 'UserStep':
            state = self.__pick_random_state()
            self.__state_instance(state)
            self.__update_state_instance()
            self.__build_activity_log_instance(action='ItemMoved')

    """ ActivityLogInstance """

    def __update_activity_log_instance(self):
        if self.__previous_step:
            self.__current_activity.update({
                '_previous_step_instance_id': self.__previous_step['_id'],
                '_previous_step_id': self.__previous_step['_step_id'],
                '_previous_step_name': self.__previous_step['_step_name']
            })

        if self.__current_state:
            self.__current_activity.update({
                "_state_id": self.__current_state['_state_id'],
                "_state_name": self.__current_state['_state_name'],
                "_state_instance_id": self.__current_state['_id'],
            })

        if self.__previous_state:
            self.__current_activity.update({
                '_previous_state_instance_id': self.__previous_state['_id'],
                '_previous_state_id': self.__previous_state['_step_id'],
                '_previous_state_name': self.__previous_state['_step_name']
            })

        if self.__previous_activity:
            self.__previous_activity.update({
                '_time_taken': self.__previous_step.get('_time_taken', 0),
                '_action_ended_at': self.__previous_step.get('_exited_at', self.__date_dict)
            })

    def __activity_log_instance(self, action):
        activity = {
            '_id': generate_pk(),
            '_action': action,
            '_action_started_at': self.__date_dict,
            '_project_flow_name': PROJECT_FLOW_NAME,
            '_project_flow_instance_id': self.__current_project_flow['_id'],
            '_project_flow_id': project_flow_id,
            '_step_id': self.__current_step['_step_id'],
            '_step_name': self.__current_step['_step_name'],
            '_step_instance_id': self.__current_step['_id'],
            '_acted_by': user,
            '_status': status_map.get(self.__current_step['_step_type'])
        }

        if action != 'Initiated' and user:
            activity.update({'AssignedTo': user})

        self.__previous_activity = self.__current_activity
        self.__current_activity = activity
        self.__activity.append(activity)

    def __build_activity_log_instance(self, action):
        self.__activity_log_instance(action=action)
        self.__update_activity_log_instance()

        if action == 'Initiated':
            self.__build_activity_log_instance(action='Assigned')

    def build(self):
        """
        Construct a mock item document.

        :returns:
        """
        self.__build_item()
        self.__build_project_flow_instance()
        self.__build_step_instance()
        self.__update_project_flow_instance()
        self.__update_item()

        return self.__item
