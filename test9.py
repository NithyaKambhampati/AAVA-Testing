from flask import Flask, request, jsonify, abort
from flask.views import MethodView

app = Flask(__name__)

tasks = {}
task_id_counter = 1

class TaskAPI(MethodView):
 def get(self, task_id=None):
 if task_id is None:
 return jsonify(list(tasks.values())), 200
 task = tasks.get(task_id)
 if not task:
 abort(404, description='Task not found')
 return jsonify(task), 200

 def post(self):
 global task_id_counter
 data = request.get_json()
 if not data or 'title' not in data:
 abort(400, description='Title is required')
 task = {
 'id': task_id_counter,
 'title': data['title'],
 'description': data.get('description', ''),
 'done': False
 }
 tasks[task_id_counter] = task
 task_id_counter += 1
 return jsonify(task), 201

 def put(self, task_id):
 data = request.get_json()
 task = tasks.get(task_id)
 if not task:
 abort(404, description='Task not found')
 if 'title' in data:
 task['title'] = data['title']
 if 'description' in data:
 task['description'] = data['description']
 if 'done' in data:
 task['done'] = data['done']
 return jsonify(task), 200

 def delete(self, task_id):
 if task_id not in tasks:
 abort(404, description='Task not found')
 del tasks[task_id]
 return '', 204

# Register the endpoints
view = TaskAPI.as_view('task_api')
app.add_url_rule('/tasks/', defaults={'task_id': None}, view_func=view, methods=['GET',])
app.add_url_rule('/tasks/', view_func=view, methods=['POST',])
app.add_url_rule('/tasks/<int:task_id>', view_func=view, methods=['GET', 'PUT', 'DELETE'])

@app.errorhandler(400)
def bad_request(error):
 return jsonify({'error': error.description}), 400

@app.errorhandler(404)
def not_found(error):
 return jsonify({'error': error.description}), 404

if __name__ == '__main__':
 app.run(debug=True)
