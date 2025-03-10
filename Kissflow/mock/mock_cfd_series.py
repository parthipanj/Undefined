import time
from datetime import datetime, timedelta

from generic.config import cfd_series_collection
from generic.db import get_db
from mock.cfd_series import CFDSeries


class MockCFDSeries:
    """
    Mock cfd series class
    """

    def __init__(self, **kwargs):
        db = kwargs.get('db')
        self.__collection = db[cfd_series_collection]
        self.__create = kwargs.get('create', True)
        self.__delete = kwargs.get('delete', True)
        self.__days = kwargs.get('days', -1)
        self.__cfd_series = []

    def __delete_cfd_series(self):
        if self.__delete:
            self.__collection.delete_many({'mock': True})

    def mock(self):
        """
        Mock CFD series

        :returns:
        """
        cfd_series_class = CFDSeries

        for value in range(self.__days, 0):
            cfd_series_date = datetime.utcnow() + timedelta(days=value)
            cfd_series_instance = cfd_series_class(date=cfd_series_date)
            cfd_series = cfd_series_instance.build()
            self.__cfd_series.extend(cfd_series)

        print(f'Mock CFD Series Count: {len(self.__cfd_series)}')

    def save(self):
        """
        Save the mocked CFD series into DB.

        :returns:
        """
        self.__delete_cfd_series()

        if self.__create:
            count = 0

            for cfd_series in self.__cfd_series:
                self.__collection.insert_one(cfd_series)
                count += 1
                print(f'''CFD Series Count: {count}''')

            print(f'Inserted CFD Series Count: {count}')


if __name__ == '__main__':
    mock_instance = MockCFDSeries(db=get_db(), create=True, delete=True, days=-365)

    start = time.time()
    mock_instance.mock()
    print(f'Mock Time Taken: {time.time() - start}')

    start = time.time()
    mock_instance.save()
    print(f'Save Time Taken: {time.time() - start}')
