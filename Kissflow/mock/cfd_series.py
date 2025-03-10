import random
from datetime import datetime

from generic import object_to_datetime_dict, generate_pk
from generic.config import project_flow_id, model, bot_user, cfd_series_steps


class CFDSeries:
    """
    CFD Series class
    """

    def __init__(self, **kwargs):
        date = kwargs.get('date', datetime.utcnow())
        self.__date = date.replace(hour=0, minute=0, second=0, microsecond=0)
        self.__date_dict = object_to_datetime_dict(self.__date)

    def __build_cfd_series(self, step):
        active, on_hold, done, item_count = (0, 0, 0, 0)

        if step['type'] == 'UserStep':
            active = random.randint(0, 50)
            on_hold = random.randint(0, 50)
            done = random.randint(0, 50)
            item_count = active + on_hold + done
        else:
            item_count = random.randint(1, 50)

        return {
            "_id": generate_pk(),
            "_step_id": step['id'],
            "_date": self.__date,
            "_step_type": step['type'],
            "_step_name": step['name'],
            "Model": model,
            "_project_flow_id": project_flow_id,
            "_position": step['position'],
            "_item_count": item_count,
            "_states": {
                "Active": active,
                "On hold": on_hold,
                "Done": done
            },
            "_created_at": self.__date_dict,
            "_created_by": bot_user,
            "_flow_name": "ProjectCFDSeries",
            "_modified_at": self.__date_dict,
            "_modified_by": bot_user,
            "mock": True
        }

    def build(self):
        """
        Build CFD Series

        :returns:
        """
        series = []

        for step in cfd_series_steps:
            series.append(self.__build_cfd_series(step))

        return series
