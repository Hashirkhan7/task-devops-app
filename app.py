from flask import Flask, jsonify, request, render_template
import sqlite3

app = Flask(__name__)

def get_db():
    conn = sqlite3.connect("tasks.db")
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = get_db()
    conn.execute("""
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            done INTEGER NOT NULL DEFAULT 0
        )
    """)
    conn.commit()
    conn.close()

@app.route("/")
def hello():
    return "Hello World"

@app.route("/tasks")
def get_tasks():
    conn = get_db()
    rows = conn.execute("SELECT * FROM tasks").fetchall()
    conn.close()
    return jsonify([dict(row) for row in rows])

@app.route("/tasks", methods=["POST"])
def add_task():
    data = request.get_json()
    title = data.get("title")
    conn = get_db()
    conn.execute("INSERT INTO tasks (title) VALUES (?)", (title,))
    conn.commit()
    conn.close()
    return jsonify({"message": "Task added"}), 201

@app.route("/tasks/<int:task_id>/done", methods=["PUT"])
def mark_done(task_id):
    conn = get_db()
    conn.execute("UPDATE tasks SET done = 1 WHERE id = ?", (task_id,))
    conn.commit()
    conn.close()
    return jsonify({"message": "Task marked done"})

@app.route("/tasks/<int:task_id>", methods=["DELETE"])
def delete_task(task_id):
    conn = get_db()
    conn.execute("DELETE FROM tasks WHERE id = ?", (task_id,))
    conn.commit()
    conn.close()
    return jsonify({"message": "Task deleted"})

@app.route("/home")
def home():
    return render_template("index.html")

init_db()

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)