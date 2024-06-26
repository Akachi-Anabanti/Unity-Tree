#!/usr/bin/env bash

#Install npm 
sudo apt-get update -y
sudo apt install -y nodejs npm


# Run the build
npm install
npm run build
# create the dir where the static files will be served from
# the current will hold the current build of the frontend application
sudo mkdir -p /var/www/unity-tree/releases/test /var/www/unity-tree/shared

echo "Test Static file setup" | sudo tee /var/www/unity-tree/releases/test/index.html

sudo ln -sf /var/www/unity-tree/releases/test/ /var/www/unity-tree/current

sudo chown -hR www-data:www-data /var/www/unity-tree

