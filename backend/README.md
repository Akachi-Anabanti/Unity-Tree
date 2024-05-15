# UNITY TREE BACKEND

## A Family Tree Application Backend
Create, Discover, Visualize, and Share Family Connections

## Table of Contents
- [Project Overview](#project-overview)
- [Packages](#packages)
- [API Endpoints](#api-endpoints)
- [How to Run the Backend Locally](#how-to-run-the-backend-locally)
- [Other Notes](#other-notes)

## Project Overview
The backend of the Unity Tree application provides a RESTful API to support the creation, discovery, and visualization of family trees. It is built with Flask and serves as the core of the Unity Tree application, handling all data management and server-side logic.

Authentication is managed using `flask_jwt_extended`, which provides endpoints for login and can handle both cookies and Authorization Header Bearer Tokens.

## Packages
This project uses the following packages and their versions:

### Backend
1. [`python`](https://www.python.org/downloads/release/python-31012/) `3.10.12`
2. [`flask`](https://flask.palletsprojects.com/en/3.0.x/) `3.0.3`
3. [`werkzeug`](https://werkzeug.palletsprojects.com/en/3.0.x/) `3.0.3`
4. [`poetry`](https://python-poetry.org/) `1.6.1`
5. [`alembic`](https://alembic)
6. [`SQLAlchemy`](https://sqlalchemy)

## API Endpoints

### Status and Utility
- **GET** `/api/v1/status/` - Check API status
- **GET** `/api/v1/ping` - Ping the server

### User Management
- **POST** `/api/v1/register` - Register a new user
- **POST** `/api/v1/login` - Login a user
- **POST** `/api/v1/logout` - Logout a user
- **GET** `/api/v1/user/` - Get current user information
- **PUT** `/api/v1/user/<string:user_id>/` - Update user information
- **DELETE** `/api/v1/user/<string:user_id>/` - Delete a user

### Family Management
- **POST** `/api/v1/family/` - Create a new family
- **GET** `/api/v1/family/<string:_id>/` - Get a family's details
- **PUT** `/api/v1/family/<string:family_id>/` - Update a family's details
- **DELETE** `/api/v1/family/<string:family_id>/` - Delete a family
- **GET** `/api/v1/user/family-created/` - Get all families created by the current user
- **GET** `/api/v1/family/owner/<string:family_id>/` - Get the owner of a family

### Family Member Management
- **POST** `/api/v1/family/member/<string:family_id>/` - Add a family member
- **GET** `/api/v1/family/member/<string:member_id>/` - Get a family member's details
- **PUT** `/api/v1/family/member/<string:member_id>/` - Update a family member's details
- **DELETE** `/api/v1/family/member/<string:family_id>/<string:member_id>/` - Delete a family member
- **DELETE** `/api/v1/family/members/<string:family_id>/` - Delete all family members in a family
- **GET** `/api/v1/family/members/<string:family_id>/` - Get all family members in a family
- **POST** `/api/v1/register/<string:member_id>` - Register a new family member

### Family Relationships
- **GET** `/api/v1/family/ancestors/<string:member_id>/` - Get ancestors of a family member
- **GET** `/api/v1/family/decendants/<string:member_id>/` - Get descendants of a family member
- **GET** `/api/v1/family/member/get-siblings/<string:member_id>/` - Get siblings of a family member

### Static Files
- **GET** `/static/<path:filename>` - Serve static files

### Server-Sent Events
- **GET** `/stream` - Stream server-sent events

## How to Run the Backend Locally
1. Ensure you have Python 3.10.12 installed. You can download it from the [official Python website](https://www.python.org/downloads/release/python-31012/).
2. Clone the repository: `Unity-Tree`.
3. Navigate to the `backend` directory and activate the virtual environment managed with Poetry by running:
    ```bash
    poetry shell
    ```
    This will create and activate the virtual environment.

4. Install the dependencies using Poetry by executing:
    ```bash
    poetry install
    ```
    This should install all the dependencies from the `pyproject.toml` file.

5. Navigate to the `app` directory and create a `.env` file. This file contains the environment configurations that Flask will need to run:
    ```env
    JWT_SECRET_KEY='Your key'
    JWT_CSRF_IN_COOKIES=True
    DATABASE_URL="YOUR database url"
    ```

6. To start the backend application, navigate back to the `backend` directory. 
    execute
    - `flask db upgrade` to create the database migrations
Choose one of the following methods:

    **[a] Using Gunicorn**:
    - Execute:
      ```bash
      gunicorn -w 4 run:app
      ```
      This starts the Flask application instance `app` in the `run.py` file with 4 workers. You can adjust this number depending on your computer's resources.

      **Output:**
      ```console
      [2024-05-15 10:38:12 +0100] [138002] [INFO] Starting gunicorn 22.0.0
      [2024-05-15 10:38:12 +0100] [138002] [INFO] Listening at: http://127.0.0.1:8000 (138002)
      [2024-05-15 10:38:12 +0100] [138002] [INFO] Using worker: sync
      [2024-05-15 10:38:12 +0100] [138003] [INFO] Booting worker with pid: 138003
      [2024-05-15 10:38:12 +0100] [138004] [INFO] Booting worker with pid: 138004
      [2024-05-15 10:38:12 +0100] [138005] [INFO] Booting worker with pid: 138005
      [2024-05-15 10:38:13 +0100] [138006] [INFO] Booting worker with pid: 138006
      ```

    **[b] Using Flask's Built-in Server**:
    - Execute:
      ```bash
      flask run --debug -p 8000
      ```
      to start the app in debug mode.

      **Output:**
      ```console
       * Debug mode: on
      WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
       * Running on http://127.0.0.1:8000
      Press CTRL+C to quit
       * Restarting with stat
       * Debugger is active!
       * Debugger PIN: 397-832-417
      ```

    - Alternatively, execute:
      ```bash
      flask run -p 8000
      ```
      to start the app without debug mode.

      **Output:**
      ```console
       * Debug mode: off
      WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
       * Running on http://127.0.0.1:8000
      Press CTRL+C to quit
      ```

## Other Notes
This backend is designed to be integrated with any frontend of your choice.
