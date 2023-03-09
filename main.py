from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route('/')
def index():
    return "Bem vindo"

tasks = []

@app.route('/tasks')
def task_list():
    return render_template('task_list.html', tasks=tasks)

@app.route('/tasks/new', methods=['GET', 'POST'])
def add_task():
    if request.method == 'POST':
        task = request.form['task']
        tasks.append(task)
        return redirect('/tasks')
    else:
        return render_template('add_task.html')

@app.route('/tasks/delete/<int:index>')
def delete_task(index):
    del tasks[index]
    return redirect('/tasks')

@app.route('/tasks/edit/<int:index>', methods=['GET', 'POST'])
def edit_task(index):
    if request.method == 'POST':
        task = request.form['task']
        tasks[index] = task
        return redirect('/tasks')
    else:
        return render_template('edit_task.html', task=tasks[index], index=index)

if __name__ == "__main__":
    app.run(debug=True)
