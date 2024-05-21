#!/usr/bin/env bash

# Setup script for the backend

#install POETRY and Add to path
curl -sSL https://install.python-poetry.org | POETRY_HOME=/etc/poetry python3 -

# Set the path to the virtual env
poetry env use python3.8 --path ./unity-tree-virtual-env
poetry install

# create a socket file unity-tree.sock that will
# enable nginx to communicate with gunicorn
sudo python3.8 -c 'import socket as s, os; sock = s.socket(s.AF_UNIX); sock.bind(os.path.join(os.getcwd(), "unity-tree.sock"))'

# set the permission and ownership of unity-tree.sock to www-data and ubuntu
# www-data that's the default user nginx is running on

sudo chown ubuntu:www-data ./unity-tree.sock
sudo chmod 660 ./unity-tree.sock

# rename run.py to wsgi.py
mv ./run.py wsgi.py


# create a service file to start gunicorn once the system reloads
sudo touch /etc/systemd/system/unity-tree.service

# edit the service file to setup gunicorn and bind to unity-tree.sock
sudo printf '
[Unit]
Description=Gunicorn instance to serve unity-tree
After=network.target

[Service]
User=ubuntu
Group=www-data
WorkingDirectory=/home/ubuntu/Unity-Tree/backend
Environment="PATH=/home/ubuntu/Unity-Tree/unity-tree-virtual-env/bin
ExecStart=/home/ubuntu/Unity-Tree/unity-tree-virtual-env/bin/gunicorn -w4 --bind unix:/home/ubuntu/Unity-Tree/backend/unity-tree.sock -m 007 wsgi:app

[Install]
WantedBy=multi-user.target
' | sudo tee /etc/systemd/system/unity-tree.service > /dev/null

# start the service with systemctl
sudo systemctl daemon-reload
sudo systemctl start unity-tree
sudo systemctl enable unity-tree
