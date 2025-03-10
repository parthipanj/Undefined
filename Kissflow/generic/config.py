"""
Module to maintain the mock configs
"""
from urllib.parse import quote_plus

#: MongoDB config
mongo = dict(
    host=[
        'perf-mongo-app-d001-shard-00-00.gjezj.mongodb.net:27017',
        'perf-mongo-app-d001-shard-00-01.gjezj.mongodb.net:27017',
        'perf-mongo-app-d001-shard-00-02.gjezj.mongodb.net:27017'
    ],
    replicaSet='atlas-11mkh5-shard-0',
    connect=True,
    username=quote_plus('perf_app_developer'),
    password=quote_plus('Fx1W7QO6B2m7MHua'),
    authSource='admin',
    authMechanism='SCRAM-SHA-1',
    tls=True,
    tlsAllowInvalidCertificates=True
)
account_id = 'AcyUOxvMyk77b'

prefix = 'MOCK'

#: Item config
flow_name = 'Performance 02'
model = 'Performance_02'
project_flow_id = 'Performance_02_flow'
item_prefix = f'PE02-{prefix}-'
user = {'_id': 'Usaq_gVjkS7Dl', 'Name': 'Parthipan', 'Kind': 'User'}

#: Item steps & states config
Step002Between = {'NoOfSteps': list(range(2, 5)), 'States': {'NoOfStates': list(range(0, 4))}}
Step003Between = {'NoOfSteps': list(range(2, 5)), 'States': {'NoOfStates': list(range(0, 4))}}
Step004Between = {'NoOfSteps': list(range(35, 38)), 'States': {'NoOfStates': list(range(0, 2))}}
steps_map = {
    'Step001': {'Id': 'Step001', 'Name': 'Not started', 'Type': 'StartStep', 'Between': None, 'ItemCount': 250},
    'Step002': {'Id': 'Step002', 'Name': 'Planning', 'Type': 'UserStep', 'Between': Step002Between,
                'ItemCount': 300},
    'Step003': {'Id': 'Step003', 'Name': 'Implementing', 'Type': 'UserStep', 'Between': Step003Between,
                'ItemCount': 300},
    'Step004': {'Id': 'Step004', 'Name': 'Completed', 'Type': 'EndStep', 'Between': Step004Between, 'ItemCount': 650}
}
start_step = steps_map.get('Step001')
step_ids = list(steps_map.keys())

states_map = {
    'State001': {'Id': 'State001', 'Name': 'Active', 'Type': 'InProgressState'},
    'State002': {'Id': 'State002', 'Name': 'On hold', 'Type': 'HoldState'},
    'State003': {'Id': 'State003', 'Name': 'Done', 'Type': 'DoneState'}
}
state_ids = list(states_map.keys())
status_map = {'StartStep': 'Not started', 'UserStep': 'In progress', 'EndStep': 'Completed'}
pk_prefix = f'{prefix}-'

#: Position config
position_collection = 'ProjectPosition'

#: CFD Series config
bot_user = {"_id": "flobot", "Name": "Flobot", "Kind": "User"}
cfd_series_collection = 'CFDSeries'


def position(num):
    return 65535 + (num * 1024)


cfd_series_steps = [
    {'id': 'Step001', 'type': 'StartStep', 'name': 'Not started', 'position': position(0)},
    {'id': 'Step002', 'type': 'UserStep', 'name': 'Planning', 'position': position(1)},
    {'id': 'Step003', 'type': 'UserStep', 'name': 'Implementing', 'position': position(2)},
    {'id': 'Step004', 'type': 'UserStep', 'name': 'UserStepA', 'position': position(3)},
    {'id': 'Step005', 'type': 'UserStep', 'name': 'UserStepB', 'position': position(4)},
    {'id': 'Step006', 'type': 'UserStep', 'name': 'UserStepC', 'position': position(5)},
    {'id': 'Step007', 'type': 'UserStep', 'name': 'UserStepD', 'position': position(6)},
    {'id': 'Step008', 'type': 'UserStep', 'name': 'UserStepE', 'position': position(7)},
    {'id': 'Step009', 'type': 'UserStep', 'name': 'UserStepF', 'position': position(8)},
    {'id': 'Step010', 'type': 'EndStep', 'name': 'Completed', 'position': position(9)}
]
