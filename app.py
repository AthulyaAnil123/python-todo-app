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