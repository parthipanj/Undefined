import random
import statistics
import time
from collections import deque
from copy import deepcopy

MOVING_AVG_INTERVAL = 5
SUM = 'sum'
MOVING_AVG = 'MovingAvg'


def moving_average_with_loop(result: list) -> list:
    initial_queue_value = list(map(int, '0' * MOVING_AVG_INTERVAL))
    previous_points = deque(initial_queue_value, maxlen=MOVING_AVG_INTERVAL)

    for document in result:
        document[MOVING_AVG] = statistics.mean(previous_points)
        document['previous_value'] = previous_points.copy()
        previous_points.popleft()
        previous_points.append(document[SUM])
        del document[SUM]

    return result


def moving_average_with_while(result: list):
    index = 0
    initial_queue_value = list(map(int, '0' * MOVING_AVG_INTERVAL))
    previous_points = deque(initial_queue_value, maxlen=MOVING_AVG_INTERVAL)

    while index < len(result):
        document = result[index]
        document[MOVING_AVG] = statistics.mean(previous_points)
        document['previous_value'] = previous_points.copy()
        previous_points.popleft()
        previous_points.append(document[SUM])
        del document[SUM]
        index += 1

    return result


if __name__ == '__main__':
    expected_output = [
        {'MovingAvg': 0, 'previous_value': deque([0, 0, 0, 0, 0])},
        {'MovingAvg': 1, 'previous_value': deque([0, 0, 0, 0, 5])},
        {'MovingAvg': 3, 'previous_value': deque([0, 0, 0, 5, 10])},
        {'MovingAvg': 6, 'previous_value': deque([0, 0, 5, 10, 15])},
        {'MovingAvg': 10, 'previous_value': deque([0, 5, 10, 15, 20])},
        {'MovingAvg': 15, 'previous_value': deque([5, 10, 15, 20, 25])},
        {'MovingAvg': 20, 'previous_value': deque([10, 15, 20, 25, 30])},
        {'MovingAvg': 25, 'previous_value': deque([15, 20, 25, 30, 35])},
        {'MovingAvg': 30, 'previous_value': deque([20, 25, 30, 35, 40])},
        {'MovingAvg': 35, 'previous_value': deque([25, 30, 35, 40, 45])}
    ]
    # input_result = [
    #     {'sum': 5}, {'sum': 10}, {'sum': 15}, {'sum': 20}, {'sum': 25}, {'sum': 30}, {'sum': 35}, {'sum': 40},
    #     {'sum': 45}, {'sum': 50}
    # ]

    input_result = [{'sum': random.randint(0, 500)} for x in range(20)]

    # Moving Average with for loop
    start = time.time()
    moving_average_with_loop(deepcopy(input_result))
    end = time.time()
    print('For-loop time taken: ', end - start)

    # Moving Average with recursion
    start = time.time()
    moving_average_with_while(deepcopy(input_result))
    end = time.time()
    print('Recursion time taken: ', end - start)


val = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
in1 = [0, 1, 2, 3, 4, 5]
in2 = [1, 2, 3, 4, 5, 6]
in3 = [2, 3, 4, 5, 6, 7]
