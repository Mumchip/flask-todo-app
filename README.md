# Web Development Project: Flask To‑Do App

This repository contains a **full‑stack web application** that implements a simple yet extensible To‑Do list manager using the [Flask](https://flask.palletsprojects.com/) micro‑framework.  The application demonstrates common patterns in web development, including routing, templating, database integration and REST‑like interactions via AJAX.  It is intended as a starting point for senior project work focusing on web architectures.

## Features

* 📝 **CRUD operations for tasks** – users can create new tasks, mark them as complete or pending, edit existing tasks and delete tasks they no longer need.
* 💄💟👿 **Persistent storage via SQLite** – tasks are stored in a SQLite database through [SQLAlchemy](https://www.sqlalchemy.org/), allowing easy migration to other relational databases.
* 🎨 **Responsive UI** – the front‑end uses HTML5, CSS3 and a sprinkle of JavaScript to provide a clean, responsive interface.  Tasks are updated asynchronously via fetch API calls, so the page does not need to reload on every action.
* 🔌 **RESTful endpoints** – the back‑end exposes JSON endpoints for creating, updating and deleting tasks, making it straightforward to build additional clients (e.g. a mobile app) on top of the same API.

## Getting started

Ensure Python 3.8+ is installed on your system.  Then install the required packages using:

```
pip install -r requirements.txt
```

### Running the development server

From within the `web_project` directory, initialize the database and start the server:

```
export FLASK_APP=app.py
python -m flask db_init    # one‑time database initialization
flask run --reload
```

The application will be available at **http://127.0.0.1:5000/**.  Open the URL in your browser to start managing tasks.

### Project structure

```text
web_project/
├── app.py              # Flask application with routes and API endpoints
├── requirements.txt     # Python dependencies
├── README.md           # Project overview and instructions (this file)
├── templates/
│   ├── base.html       # Shared HTML layout
│   └── index.html      # Main page listing tasks
└── static/
    └── style.css       # Minimal CSS styling
```

## Extending the project

This project serves as a foundation for more complex web applications.  Here are some ideas for enhancements:

* 👥 **User authentication:** Add sign‑up/login functionality using Flask‑Login to allow multiple users to manage their own lists.
* ⏰ **Due dates and reminders:** Allow tasks to have due dates and send reminder emails using a background job queue (e.g. Celery + Redis).
* 📱 **Mobile client:** Build a Flutter or React Native application that consumes the same REST API exposed by this server.
* 🌐 **Deployment:** Containerize the application with Docker and deploy it to a cloud provider like AWS or Heroku.

Contributions, bug reports and feature requests are welcome!
