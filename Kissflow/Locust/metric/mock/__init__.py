import json
import os


def load_mock(file_name):
    dir_path = os.path.dirname(os.path.realpath(__file__))

    with open(f'{dir_path}/{file_name}.json') as f:
        data = json.load(f)

    return data


if __name__ == '__main__':
    load_mock('step')
