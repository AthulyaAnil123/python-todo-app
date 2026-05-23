from flask import Flask, jsonify, request

app = Flask(__name__)


todo_list = [
    {"id": 1, "task": "Learn DevOps", "done": False},
    {"id": 2, "task": "Setup Docker", "done": False}
]

@app.route('/todos', methods=['GET'])
def get_todos():
    return jsonify({"todos": todo_list})

@app.route('/todos', methods=['POST'])
def add_todo():
    new_task = request.json.get('task')
    if not new_task:
        return jsonify({"error": "Task is required"}), 400
    
    task_item = {
        "id": len(todo_list) + 1,
        "task": new_task,
        "done": False
    }
    todo_list.append(task_item)
    return jsonify({"message": "Task added successfully", "task": task_item}), 201
    
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
  from flask import Flask, render_template, request, redirect

app = Flask(__name__)
tasks = []

@app.route('/')
def index():
    return render_template('index.html', tasks=tasks)

@app.route('/add', methods=['POST'])
def add():
    task = request.form.get('task')
    tasks.append(task)
    return redirect('/')

@app.route('/delete')
def delete():
    if tasks:
        tasks.pop()
    return redirect('/')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)  