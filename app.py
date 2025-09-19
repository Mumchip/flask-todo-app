#!/usr/bin/env python
"""
app.py
-------

Flask application implementing a simple to-do list with SQLite persistence.  The
application exposes both HTML routes and JSON API endpoints for creating,
editing and deleting tasks.  It is designed to be self-contained and easy to
extend for more advanced coursework.
"""
from __future__ import annotations

import os
from typing import List, Dict, Any

from flask import Flask, render_template, request, jsonify, abort
from flask_sqlalchemy import SQLAlchemy


# Configuration
BASE_DIR = os.path.abspath(os.path.dirname(__file__))
DATABASE_PATH = os.path.join(BASE_DIR, "todo.db")

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{DATABASE_PATH}"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)


class Task(db.Model):
    """Database model representing a single to-do task."""
    id: int = db.Column(db.Integer, primary_key=True)
    title: str = db.Column(db.String(200), nullable=False)
    completed: bool = db.Column(db.Boolean, default=False)

    def as_dict(self) -> Dict[str, Any]:
        return {"id": self.id, "title": self.title, "completed": self.completed}


@app.cli.command("db_init")
def db_init() -> None:
    """Initialize the SQLite database.  Run `flask db_init` once before first use."""
    db.create_all()
    print(f"Database created at {DATABASE_PATH}")


@app.route("/")
def index() -> str:
    """Serve the main page showing the list of tasks."""
    tasks: List[Task] = Task.query.order_by(Task.id.desc()).all()
    return render_template("index.html", tasks=tasks)


@app.route("/api/tasks", methods=["GET", "POST"])
def tasks_endpoint():
    """Endpoint to list all tasks or create a new one."""
    if request.method == "GET":
        tasks: List[Task] = Task.query.all()
        return jsonify([task.as_dict() for task in tasks])
    # POST: create a new task
    data = request.get_json(force=True)
    title: str = data.get("title", "").strip()
    if not title:
        return jsonify({"error": "Title is required"}), 400
    task = Task(title=title)
    db.session.add(task)
    db.session.commit()
    return jsonify(task.as_dict()), 201


@app.route("/api/tasks/<int:task_id>", methods=["PUT", "DELETE"])
def task_endpoint(task_id: int):
    """Endpoint to update or delete a specific task."""
    task: Task | None = Task.query.get(task_id)
    if task is None:
        abort(404)
    if request.method == "PUT":
        data = request.get_json(force=True)
        title = data.get("title", task.title).strip()
        completed = data.get("completed", task.completed)
        task.title = title or task.title
        task.completed = bool(completed)
        db.session.commit()
        return jsonify(task.as_dict())
    # DELETE
    db.session.delete(task)
    db.session.commit()
    return jsonify({"result": True})


if __name__ == "__main__":
    app.run(debug=True)
