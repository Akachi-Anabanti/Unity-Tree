# UNITY TREE APPLICATION

## A Family Tree Application
Create, Discover, Visualize and Share Family Connections

## Table of Contents
- Project Overview
- Packages
- How to Run the App Locally
- Other Notes

## Project Overview
The application allows users to create, discover, and visualize a family tree and add family members. The backend was built with Flask, providing a RESTful API. The frontend is built on Vue3Js Composition API and Pinia for state management. The frontend was styled with CSS and Vuestic UI.

## Packages
This project uses the following packages and their versions:

### Frontend
1. `Vue` `@vue/cli 5.0.8`
2. `npm` `10.6.0`
3. `Vite` `5.2.10`

### Backend
1. `python` `3.10.12`
2. `flask` `3.0.3`
3. `werkzeug` `3.0.3`
4. `poetry` `1.6.1`

## How to Run the App Locally
1. Make sure you have `npm` version `10.6.0`, the node package manager, installed on your computer. Here is a resource that should help with that: npm documentation
2. Clone the repository: Unity-Tree
3. Navigate to the `frontend` directory and run:
    - `npm install` - wait for npm to finish installing the packages
    - `npm run dev` - This should spin up a `vite` server. On `Ubuntu 22`, you should see a similar output as this:
    ```console
    > frontend@0.0.0 dev
    > vite
        VITE v5.2.10 ready in 316ms
        -> Local: http://localhost:5173/
        -> Network: use --host to expose
        -> press h + enter to show help
    ```

## Other Notes
You can integrate any frontend of your choice.
