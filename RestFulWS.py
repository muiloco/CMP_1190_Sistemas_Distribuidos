from flask import Flask, jsonify, abort, make_response, request

app = Flask(__name__)

tasks = [
    {
        'id': 1,
        'titulo': u'Conferencia sobre DataCenter',
        'data': u'18/09/2019', 
        'duracao': u'5 dias'
    },
    {
        'id': 2,
        'titulo': u'Conferencia sobre Inteligencia Artificial',
        'data': u'25/11/2019', 
        'duracao': u'2 horas'
    }
]

def procurarInconsAlt(task):
    for index in range(len(tasks)):
        dict1 = tasks[index]
        if task[0]['id'] != dict1['id']:
            if task[0]['data'] == dict1['data']:
                return True
            elif task[0]['duracao'] == dict1['duracao']:
                return True
    return False

def procurarInconsCriar(task):
    for index in range(len(tasks)):
        dict1 = tasks[index]
        if task['id'] != dict1['id']:
            if task['data'] == dict1['data']:
                return True
            elif task['duracao'] == dict1['duracao']:
                return True
    return False

@app.route('/todo/api/v1.0/tasks', methods=['GET'])
def get_tasks():
    return jsonify({'tasks': tasks})

@app.route('/todo/api/v1.0/tasks/<int:task_id>', methods=['GET'])
def get_task(task_id):
    task = [task for task in tasks if task['id'] == task_id]
    if len(task) == 0:
        abort(404)
    return jsonify({'task': task[0]})

@app.route('/todo/api/v1.0/tasks', methods=['POST'])
def create_task():
    if not request.json or not 'titulo' in request.json:
        abort(400)
    task = {
        'id': tasks[-1]['id'] + 1,
        'titulo': request.json['titulo'],
        'data': request.json.get('data', ""),
        'duracao': request.json.get('duracao', "")
    }
    if procurarInconsCriar(task):
        abort(401)
    tasks.append(task)
    return jsonify({'task': task}), 201

@app.route('/todo/api/v1.0/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    task = [task for task in tasks if task['id'] == task_id]
    if len(task) == 0:
        abort(404)
    if not request.json:
        abort(400)
    if 'titulo' in request.json and type(request.json['titulo']) is not str:
        abort(400)
    if 'data' in request.json and type(request.json['data']) is not str:
        abort(400)
    if 'duracao' in request.json and type(request.json['duracao']) is not str:
        abort(400)
    task[0]['titulo'] = request.json.get('titulo', task[0]['titulo'])
    task[0]['data'] = request.json.get('data', task[0]['data'])
    task[0]['duracao'] = request.json.get('duracao', task[0]['duracao'])
    if procurar(task):
        abort(401)
    return jsonify({'task': task[0]})

@app.route('/todo/api/v1.0/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    task = [task for task in tasks if task['id'] == task_id]
    if len(task) == 0:
        abort(404)
    tasks.remove(task[0])
    return jsonify({'result': True})

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

if __name__ == '__main__':
    app.run(debug=True)
