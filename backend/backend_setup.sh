#!/usr/bin/env bash

# Setup script for the backend

# Install POETRY and Add to PATH
curl -sSL https://install.python-poetry.org | POETRY_HOME=/etc/poetry python3 -

# Add poetry to PATH
export PATH="/etc/poetry/bin:$PATH"

# Configure Poetry to create virtual environments in the project's root directory
poetry config virtualenvs.in-project true

# Set the path to the virtual env
poetry env use python3.8

# Lock dependencies (remove square brackets around --no-update)
poetry lock --no-update

# Install dependencies
poetry install

# Execute the DB upgrade
# creates the tables in the database
poetry run flask db upgrade

# Create a socket file unity-tree.sock that will enable nginx to communicate with gunicorn
sudo python3.8 -c 'import socket as s, os; sock = s.socket(s.AF_UNIX); sock.bind(os.path.join(os.getcwd(), "unity-tree.sock"))'

# Set the permission and ownership of unity-tree.sock to www-data and ubuntu
# www-data is the default user nginx is running as
sudo chown ubuntu:www-data ./unity-tree.sock
sudo chmod 660 ./unity-tree.sock

# Rename run.py to wsgi.py
mv run.py wsgi.py

# Create a service file to start gunicorn once the system reloads
sudo touch /etc/systemd/system/unity-tree.service

# Edit the service file to setup gunicorn and bind to unity-tree.sock
sudo bash -c 'cat <<EOF > /etc/systemd/system/unity-tree.service
[Unit]
Description=Gunicorn instance to serve unity-tree
After=network.target

[Service]
User=ubuntu
Group=www-data
WorkingDirectory=/home/ubuntu/Unity-Tree/backend
Environment="PATH=/home/ubuntu/Unity-Tree/backend/.venv/bin"
ExecStart=/home/ubuntu/Unity-Tree/backend/.venv/bin/gunicorn -w 4 --bind unix:/home/ubuntu/Unity-Tree/backend/unity-tree.sock -m 007 wsgi:app

[Install]
WantedBy=multi-user.target
EOF'

# Start the service with systemctl
sudo systemctl daemon-reload
sudo systemctl start unity-tree
sudo systemctl enable unity-tree
