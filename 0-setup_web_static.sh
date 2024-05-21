#!/usr/bin/env bash
# sets up the web servers for the deployment of web_static

sudo apt-get -y update
sudo apt-get -y upgrade
sudo apt-get -y install nginx

sudo mkdir -p /var/www/unity-tree/releases/test /var/www/unity-tree/shared
echo "Test Static file setup" | sudo tee /var/www/unity-tree/releases/test/index.html
sudo ln -sf /var/www/unity-tree/releases/test/ /var/www/unity-tree/current
sudo chown -hR www-data:www-data /var/www/unity-tree
HOSTNAME=$(hostname)
sudo printf '
server {
  listen 80 default_server;
  listen [::]:80 default_server;
  server_name $HOSTNAME;

  add_header X-Served-By $HOSTNAME;

  location / {
     alias /var/www/unity-tree/current/;
     index index.html index.htm;
     try_files $uri $uri/ /index.html;
  }

  location /api/ {
      include proxy_params;
      proxy_pass http://unix:/home/ubuntu/Unity-Tree/backend/unity-tree.sock;
   }
 }' | sudo tee /etc/nginx/sites-available/default > /dev/null

sudo service nginx restart
