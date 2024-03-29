from flask import Flask, request
import model, logic

app = Flask(__name__)

_event_logic = logic.EventLogic()
class ApiException(Exception):
    pass

def _from_raw(raw_event: str) -> model.Event:
    parts = raw_event.split('|')
    if len(parts) == 3:
        event = model.Event()
        event.id = None
        event.date = parts[0]
        event.title = parts[1]
        event.text = parts[2]
        return event
    elif len(parts) == 4:
        event = model.Event()
        event.id = parts[0]
        event.date = parts[1]
        event.title = parts[2]
        event.text = parts[3]
        return event
    else:
        raise ApiException(f'invalid RAW event data {raw_event}')

def _to_raw(event: model.Event) -> str:
    if event.id is None:
        return f'{event.date}|{event.title}|{event.text}'
    else:
        return f'{event.id}|{event.date}|{event.title}|{event.text}'


API_ROOT = '/api/v1'
EVENT_API_ROOT = API_ROOT + '/calendar'


@app.route(EVENT_API_ROOT + '/', methods=['POST'])
def create():
    try:
        data = request.get_data().decode('utf-8')
        event = _from_raw(data)
        _id = _event_logic.create(event)
        return f'new id: {_id}', 201
    except Exception as ex:
        return f'api failed to CREATE  with: {ex}', 404


@app.route(EVENT_API_ROOT + '/', methods=['GET'])
def list():
    try:
        events = _event_logic.list()
        raw_events = ""
        for event in events:
            raw_events += _to_raw(event) + '\n'
        return raw_events, 200
    except Exception as ex:
        return f'api failed to LIST with: {ex}', 404


@app.route(EVENT_API_ROOT + '/<_id>/', methods=['GET'])
def read(_id: str):
    try:
        event = _event_logic.read(_id)
        raw_event = _to_raw(event)
        return raw_event, 200
    except Exception as ex:
        return f'api failed to READ with {ex}', 404



@app.route(EVENT_API_ROOT + '/<_id>/', methods=['PUT'])
def update(_id: str):
    try:
        data = request.get_data().decode('utf-8')
        event = _from_raw(data)
        _event_logic.update(_id, event)
        return 'updated', 200
    except Exception as ex:
        return f'api failed to UPDATE: {ex}', 404

@app.route(EVENT_API_ROOT + '/<_id>/', methods=['DELETE'])
def delete(_id: str):
    try:
        _event_logic.delete(_id)
        return 'deleted', 200
    except Exception as ex:
        return f'api failed to DELETE: {ex}', 404






#
# @app.route("/api/user/<username>")
# def api_v1_user_by_name_v1(username):
#     return f"{request.method}. Hello, {username}-v1!"
#
# @app.route("/api/user/<username>/", methods=['GET'])
# def api_v1_user_by_name_v2(username):
#     return f"{request.method}. Hello, {username}-v2!"
#
# @app.route("/api/user/<username>/", methods=['POST'])
# def api_v1_user_by_name_v3(username):
#     return f"{request.method}. Hello, {username}-v2! / {request.get_data()}"
#
# @app.route("/api/note/<id>/", methods=['GET'])
# def note_get_id(id):
#     return f'note: {id}'