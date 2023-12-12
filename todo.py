from flask import Flask, render_template, request, redirect, url_for
app = Flask(__name__)
tasks = []
@app.route('/')
def index():
    return render_template('index.html', tasks=tasks)
@app.route('/add', methods=['POST'])
def add():
    task = request.form.get('task')
    tasks.append({'name': task, 'completed': False})
    return redirect(url_for('index'))
@app.route('/complete/<int:task_id>')
def complete(task_id):
    if 0 <= task_id < len(tasks):
        tasks[task_id]['completed'] = not tasks[task_id]['completed']
    return redirect(url_for('index'))
@app.route('/delete/<int:task_id>')
def delete(task_id):
    if 0 <= task_id < len(tasks):
        del tasks[task_id]
    return redirect(url_for('index'))
@app.route('/view/<int:task_id>')
def view(task_id):
    if 0 <= task_id < len(tasks):
        task = tasks[task_id]
        return render_template('view_task.html', task=task)
    else:
        return "Task not found"
if __name__ == '__main__':
    app.run(debug=True)
