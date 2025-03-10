import random
from datetime import datetime, timedelta

from generic import object_to_datetime_dict
from generic.db import init_db


def generate_item(date):
    global count
    count += 1
    date_dict = object_to_datetime_dict(date)

    step1_time_taken = random.randint(1, 5000)
    state1_time_taken = random.randint(1, 5000)
    step2_time_taken = state1_time_taken

    gross_time = step1_time_taken + step2_time_taken
    net_time = step2_time_taken

    item = {
        "_id": "{}{}".format(ITEM_PREFIX, count),
        "Title": "{} item".format(count),
        "_created_at": date_dict,
        "_created_by": USER,
        "_flow_name": FLOW_NAME,
        "_modified_at": date_dict,
        "_modified_by": USER,
        "Name": "{} item".format(count),
        "ProjectFlowInstance": [
            {
                "_id": "PkEeHGEYaY1_s",
                "_created_at": date_dict,
                "_modified_at": date_dict,
                "_created_by": USER,
                "_modified_by": USER,
                "_status": "Completed",
                "_project_flow_type": "MainProjectFlow",
                "_entered_at": date_dict,
                "_current_step_instance_id": "PkfyHGBzizIzz",
                "_current_step_id": "Step004",
                "_current_step_name": "Completed",
                "_project_flow_id": PROJECT_FLOW_ID,
                "Model": MODEL,
                "_project_flow_name": "Main Project",
                "_start_step_instance_id": "Pk46HGEYaYw6Q",
                "_current_state_instance_id": None,
                "_current_state_id": None,
                "_current_state_name": None,
                "_started_at": date_dict,
                "_completed_at": date_dict,
                "_gross_time": gross_time,
                "_net_time": net_time
            }
        ],
        "StepInstance": [
            {
                "_id": "Pk46HGEYaYw6Q",
                "_created_at": date_dict,
                "_modified_at": date_dict,
                "_created_by": USER,
                "_modified_by": USER,
                "_step_id": "Step001",
                "_step_type": "StartStep",
                "_project_flow_instance_id": "PkEeHGEYaY1_s",
                "_project_flow_id": PROJECT_FLOW_ID,
                "Model": MODEL,
                "_step_name": "Not started",
                "_entered_at": date_dict,
                "_next_step_instance_id": "PkS1HGBz0lkWl",
                "_exited_at": date_dict,
                "_time_taken": step1_time_taken
            },
            {
                "_id": "PkS1HGBz0lkWl",
                "_created_at": date_dict,
                "_modified_at": date_dict,
                "_created_by": USER,
                "_modified_by": USER,
                "_step_id": "Step003",
                "_step_type": "UserStep",
                "_project_flow_instance_id": "PkEeHGEYaY1_s",
                "_project_flow_id": PROJECT_FLOW_ID,
                "Model": MODEL,
                "_step_name": "Implementing",
                "_previous_step_instance_id": "Pk46HGEYaYw6Q",
                "_previous_step_id": "Step001",
                "_entered_at": date_dict,
                "_state_instance_id": "PkIbHGBz0snjl",
                "_start_state_instance_id": "PkIbHGBz0snjl",
                "_state_name": "Done",
                "_state_id": "State006",
                "_next_step_instance_id": "PkfyHGBzizIzz",
                "_exited_at": date_dict,
                "_time_taken": step2_time_taken
            },
            {
                "_id": "PkfyHGBzizIzz",
                "_created_at": date_dict,
                "_modified_at": date_dict,
                "_created_by": USER,
                "_modified_by": USER,
                "_step_id": "Step004",
                "_step_type": "EndStep",
                "_project_flow_instance_id": "PkEeHGEYaY1_s",
                "_project_flow_id": PROJECT_FLOW_ID,
                "Model": MODEL,
                "_step_name": "Completed",
                "_previous_step_instance_id": "PkS1HGBz0lkWl",
                "_previous_step_id": "Step003",
                "_entered_at": date_dict
            }
        ],
        "ActivityLogInstance": [
            {
                "_id": "Pkv6HGEYaYamC",
                "_action": "Initiated",
                "_action_started_at": date_dict,
                "_project_flow_name": "Main Project",
                "_project_flow_instance_id": "PkEeHGEYaY1_s",
                "_project_flow_id": PROJECT_FLOW_ID,
                "_step_id": "Step001",
                "_step_name": "Not started",
                "_step_instance_id": "Pk46HGEYaYw6Q",
                "_acted_by": USER,
                "_status": "Not started",
                "_time_taken": step1_time_taken,
                "_action_ended_at": date_dict
            },
            {
                "_id": "PkTmHGBz0sNPm",
                "_previous_step_instance_id": "Pk46HGEYaYw6Q",
                "_previous_step_id": "Step001",
                "_previous_step_name": "Not started",
                "_action": "ItemMoved",
                "_action_started_at": date_dict,
                "_project_flow_name": "Main Project",
                "_project_flow_instance_id": "PkEeHGEYaY1_s",
                "_project_flow_id": PROJECT_FLOW_ID,
                "_step_id": "Step003",
                "_step_name": "Implementing",
                "_step_instance_id": "PkS1HGBz0lkWl",
                "_state_id": "State006",
                "_state_name": "Done",
                "_state_instance_id": "PkIbHGBz0snjl",
                "_acted_by": USER,
                "_status": "In progress",
                "_time_taken": step2_time_taken,
                "_action_ended_at": date_dict
            },
            {
                "_id": "PkdNHGBzoJb7R",
                "_previous_step_instance_id": "PkS1HGBz0lkWl",
                "_previous_state_instance_id": "PkIbHGBz0snjl",
                "_previous_step_id": "Step003",
                "_previous_state_id": "State006",
                "_previous_step_name": "Implementing",
                "_previous_state_name": "Done",
                "_action": "Completed",
                "_action_started_at": date_dict,
                "_project_flow_name": "Main Project",
                "_project_flow_instance_id": "PkEeHGEYaY1_s",
                "_project_flow_id": PROJECT_FLOW_ID,
                "_step_id": "Step004",
                "_step_name": "Completed",
                "_step_instance_id": "PkfyHGBzizIzz",
                "_acted_by": USER,
                "_status": "Completed"
            }
        ],
        "_current_activity_log": "PkdNHGBzoJb7R",
        "_start_activity_log": "Pkv6HGEYaYamC",
        "_main_flow_instance": "PkEeHGEYaY1_s",
        "_counter": 2,
        "_item_id": "{}{}".format(ITEM_PREFIX, count),
        "StateInstance": [
            {
                "_id": "PkIbHGBz0snjl",
                "_step_instance_id": "PkS1HGBz0lkWl",
                "_step_id": "Step003",
                "_step_name": "Implementing",
                "_state_id": "State006",
                "_state_type": "DoneState",
                "_state_name": "Done",
                "_project_flow_id": PROJECT_FLOW_ID,
                "Model": MODEL,
                "_entered_at": date_dict,
                "_exited_at": date_dict,
                "_time_taken": state1_time_taken
            }
        ],
        "mock": True
    }
    items.append(item)


if __name__ == '__main__':
    create = True
    days = -1

    ACCOUNT = 'AcUZr0RbpnS3R'
    FLOW_NAME = 'Metric report test 04'
    MODEL = 'Metric_report_test_04'
    PROJECT_FLOW_ID = 'Metric_report_test_04_flow'
    ITEM_PREFIX = 'MRT3-mock'

    USER = {
        "_id": "UskujnRvJ2Rjs",
        "Name": "Parthipan",
        "Kind": "User"
    }
    count = 0
    items = list()

    db = init_db(ACCOUNT)
    project_collection = db[MODEL]

    project_collection.delete_many({'mock': True})

    if create:
        for value in range(days, 0):
            random_value = random.randint(0, 30)

            for index in range(random_value):
                item_date = datetime.utcnow() + timedelta(days=value, minutes=index)
                print('date: {}, random value: {}'.format(item_date, random_value))
                generate_item(item_date)

        print('Total mock items: {}'.format(len(items)))
        result = project_collection.insert_many(items)
        print('Inserted items count: {}'.format(len(result.inserted_ids)))
