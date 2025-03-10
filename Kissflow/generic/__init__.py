import random
from datetime import datetime, timedelta

from generic.config import pk_prefix

strptime_fmt = "%Y-%m-%dT%H:%M:%S"


def datetime_to_display(datetime_dict, field=None):
    if datetime_dict.get('dv', None):
        return datetime_dict['dv']
    if datetime_dict['v'].tzinfo is None or datetime_dict['v'].tzinfo.zone == 'GMT':
        return ''.join([datetime_dict['v'].strftime(strptime_fmt), 'Z'])
    return ''.join([datetime_dict['v'].strftime(strptime_fmt), datetime_dict['td'], ' ', datetime_dict['tz']])


def object_to_datetime_dict(dt):
    if isinstance(dt, dict) and isinstance(dt['v'], datetime):
        return dt
    datetime_dict = dict()
    datetime_dict['v'] = dt
    datetime_dict['td'] = ''
    datetime_dict['tz'] = 'GMT'
    if dt.tzinfo is not None and dt.tzinfo.zone != 'GMT':
        datetime_dict['td'] = ":".join([dt.strftime('%z')[:-2], dt.strftime('%z')[-2:]])
        datetime_dict['tz'] = dt.tzinfo.zone
    datetime_dict['dv'] = datetime_to_display(datetime_dict)
    return datetime_dict


START_TIMESTAMP = 1533061800.0

ALPHABET = ''
ORIGINAL = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ_'
SHUFFLED = None
SEED = 0
PREVIOUS_SECONDS = 0


def get_random_number(ends=1000):
    """
        return a random number based on a seed. for try to reduce the same random value
    """
    global SEED
    SEED = SEED or random.random()
    SEED = (SEED * 9301 + 49297) % 233280
    ran = SEED / 233280.0
    val = 0
    while ran < ends:
        ran *= 10
        if ran < ends:
            val = int(ran)
    return val


def shuffle():
    """

    :return:
    """
    global ORIGINAL
    source_str = ORIGINAL
    target_str = ''

    while source_str.__len__() > 0:
        r = random.randrange(0, source_str.__len__())
        char = source_str[r]
        target_str += char
        source_str = source_str.replace(char, '', 1)
    return target_str


def get_shuffled():
    global SHUFFLED
    if SHUFFLED:
        return SHUFFLED
    SHUFFLED = shuffle()
    return SHUFFLED


def int_to_base63(num: int):
    """Converts a positive integer into a base36 string."""
    assert num >= 0
    digits = get_shuffled()

    res = ''
    while not res or num > 0:
        num, i = divmod(num, 63)
        res = digits[i] + res
    return res


def short_id(mult=1000):
    """
    this user to generate short unique_id
    this method return a short uuid this length 10 till datetime.datetime(2111, 12, 31, 0, 0, 0, 0) after that time
    size will change
    """
    global PREVIOUS_SECONDS
    from datetime import datetime
    seconds = (datetime.utcnow().timestamp() - START_TIMESTAMP) * mult
    if seconds == PREVIOUS_SECONDS:
        seconds += 1
    PREVIOUS_SECONDS = seconds
    key = int_to_base63(int(seconds))
    prfix = int_to_base63(get_random_number(500000))
    while not prfix.__len__() >= 2:
        prfix = int_to_base63(get_random_number(500000))
    suffix_len = 2
    # Note : Due to More uniqueness removed this
    # if key.__len__() == 7:
    #     suffix_len = 1
    suffix = int_to_base63(get_random_number(500000))
    while not suffix.__len__() >= suffix_len:
        suffix = int_to_base63(get_random_number(500000))
    return prfix[-2:] + key + suffix[-suffix_len:]


def generate_pk(key=pk_prefix):
    """
    this Creating _id
    :type key: str
    :param key: prefix of id
    :return: str
    """
    return key + short_id()


def get_date(date, minutes):
    return date + timedelta(minutes=minutes)
