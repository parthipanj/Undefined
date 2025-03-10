from datetime import datetime


def to_timestamp(date_string):
    date = datetime.strptime(date_string, '%Y-%m-%d')
    return datetime.timestamp(date) * 1000


def to_date(timestamp):
    return datetime.fromtimestamp(timestamp)


if __name__ == '__main__':
    timestamp_value = to_timestamp('2021-03-18')
    print(timestamp_value)
    print(to_date(timestamp_value / 1000))
