"""
Module to mock items
"""
import random
import time
from copy import deepcopy
from datetime import datetime, timedelta

from generic.config import model, steps_map, position_collection, project_flow_id, prefix
from generic.db import get_db
from mock.item import Item


class MockItem:
    """
    Mock item class
    """

    def __init__(self, **kwargs):
        db = kwargs.get('db')
        self.__collection = db[model]
        self.__position_collection = db[position_collection]
        self.__create = kwargs.get('create', True)
        self.__delete = kwargs.get('delete', True)
        self.__days = kwargs.get('days', -1)
        self.__items = []

    def __get_position(self):
        return self.__position_collection.find_one({'_project_flow_id': project_flow_id})

    def __update_position(self, doc):
        self.__position_collection.update_one({'_project_flow_id': project_flow_id}, {'$set': doc})

    def __delete_items(self):
        if self.__delete:
            self.__collection.delete_many({'mock': True})

            position = self.__get_position()

            _position = deepcopy(position['_position'])
            for item_id in position['_position']:
                if prefix in item_id:
                    _position.remove(item_id)

            self.__update_position({'_position': _position})

    def mock(self):
        """
        Mock the items based on step

        :returns:
        """
        item_class = Item
        date = datetime.utcnow()
        days_range = list(range(self.__days, 0))

        for step in steps_map.values():
            for _ in range(0, step['ItemCount']):
                days = random.choice(days_range)
                item_date = date + timedelta(days=days)

                item_instance = item_class(date=item_date, step=step)
                item = item_instance.build()

                self.__items.append(item)

        print(f'Mock Items Count: {len(self.__items)}')

    def save(self):
        """
        Save the mocked items into DB.

        :returns:
        """
        self.__delete_items()

        if self.__create:
            count = 0
            item_ids = []

            for item in self.__items:
                self.__collection.insert_one(item)
                count += 1
                item_ids.append(item['_id'])
                print(f'''Item Id: {item['_id']}''')

            print(f'Inserted Items Count: {count}')

            position = self.__get_position()
            position['_position'].extend(item_ids)
            self.__update_position({'_position': position['_position']})


if __name__ == '__main__':
    mock_instance = MockItem(db=get_db(), create=True, delete=True, days=-365)

    start = time.time()
    mock_instance.mock()
    print(f'Mock Time Taken: {time.time() - start}')

    start = time.time()
    mock_instance.save()
    print(f'Save Time Taken: {time.time() - start}')
