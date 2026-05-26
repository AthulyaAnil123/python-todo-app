from flask import Flask, request, redirect, url_for, render_template_string
import os

app = Flask(__name__)

tasks = []

html = """
<!DOCTYPE html>
<html>
<head>
    <title>Todo App</title>
</head>
<body>
    <h2>Todo App</h2>
    <form method="POST" action="/add">
        <input type="text" name="task" placeholder="Enter task" required>
        <button type="submit">Add</button>
    </form>
    <ul>
    {% for task in tasks %}
        <li>{{ task }} <a href="/delete/{{ loop.index0 }}">Delete</a></li>
    {% endfor %}
    </ul>
</body>
</html>
"""

@app.route('/')
def home():
    return render_template_string(html, tasks=tasks)

@app.route('/add', methods=['POST'])
def add():
    task = request.form['task']
    if len(task) > 50:
        return "Task too long!"
    tasks.append(task)
    return redirect(url_for('home'))

@app.route('/delete/<int:index>')
def delete(index):
    tasks.pop(index)
    return redirect(url_for('home'))

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)