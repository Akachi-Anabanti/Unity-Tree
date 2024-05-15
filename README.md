# UNITY TREE APPLICATION

## A Family Tree Application
Create, Discover, Visualize, and Share Family Connections

## Table of Contents
- [Project Overview](#project-overview)
- [Packages](#packages)
- [How to Run the App Locally](#how-to-run-the-app-locally)
- [Other Notes](#other-notes)

## Project Overview
The application allows users to create, discover, and visualize a family tree and add family members. The backend is built with Flask, providing a RESTful API. The frontend is built using the Vue 3 Composition API and Pinia for state management. The frontend is styled with CSS and Vuestic UI.

## Packages
This project uses the following packages and their versions:

### Frontend
1. [`Vue`](https://cli.vuejs.org/) `@vue/cli 5.0.8`
2. [`npm`](https://www.npmjs.com/) `10.6.0`
3. [`Vite`](https://vitejs.dev/) `5.2.10`

### Backend
1. [`python`](https://www.python.org/downloads/release/python-31012/) `3.10.12`
2. [`flask`](https://flask.palletsprojects.com/en/3.0.x/) `3.0.3`
3. [`werkzeug`](https://werkzeug.palletsprojects.com/en/3.0.x/) `3.0.3`
4. [`poetry`](https://python-poetry.org/) `1.6.1`

## How to Run the App Locally
1. Make sure you have `npm` version `10.6.0` installed on your computer. Here is a resource that should help with that: [npm documentation](https://docs.npmjs.com/).
2. Clone the repository: `Unity-Tree`.
3. Navigate to the `frontend` directory.
    - Create a `.env` file in the `frontend` directory and open it in your favorite editor. Set the `VITE_API_ENDPOINT` config variable:
      ```env
      VITE_API_ENDPOINT="http://localhost:8000/api/v1"
      ```
    - This is the endpoint where the Flask application will be listening.

    Run:
    - `npm install` - wait for npm to finish installing the packages.
    - `npm run dev` - This should spin up a Vite server. On Ubuntu 22, you should see a similar output as this:
      ```console
      > frontend@0.0.0 dev
      > vite
          VITE v5.2.10 ready in 316ms
          -> Local: http://localhost:5173/
          -> Network: use --host to expose
          -> press h + enter to show help
      ```

4. Open any browser of your choice and navigate to the URL http://localhost:5173/.

5. You should see this login page:
![Login](images/login-screenshot.png)

6. In another terminal, navigate to the `backend` folder and activate the virtual environment managed with Poetry by running on a Linux terminal:
    ```bash
    poetry shell
    ```
    This will create and activate the virtual environment.

7. Install the dependencies using Poetry by executing:
    ```bash
    poetry install
    ```
    This should install all the dependencies from the `pyproject.toml` file.

8. Navigate to the `app` directory and create a `.env` file. This file contains the environment configurations that Flask will need to run:
    ```env
    JWT_SECRET_KEY='Your key'
    JWT_CSRF_IN_COOKIES=True
    ```

9. To start the backend application, navigate back to the `backend` directory. Choose one of the following methods:

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

10. You can now visit the Web page and interact with it.