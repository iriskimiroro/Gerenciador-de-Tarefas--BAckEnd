from flask import Flask, jsonify, request
import sqlite3

app = Flask(__name__)

# Rota para obter todas as tarefas
@app.route('/tasks', methods=['GET'])
def get_tasks():
    conn = sqlite3.connect('tasks.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM tasks')
    tasks = cursor.fetchall()
    conn.close()
    return jsonify(tasks)

# Rota para adicionar uma nova tarefa
@app.route('/tasks', methods=['POST'])
def add_task():
    data = request.get_json()
    conn = sqlite3.connect('tasks.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO tasks (name, task, date) VALUES (?, ?, ?)',
                   (data['name'], data['task'], data['date']))
    conn.commit()
    conn.close()
    return 'Tarefa adicionada com sucesso!'

if __name__ == '__main__':
    app.run(debug=True)