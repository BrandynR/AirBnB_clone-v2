#!/usr/bin/env bash
# Setup up web severs for deployment of web static

sudo apt-get -y update
sudo apt-get -y install nginx
mkdir -p /data/web_static/releases/test/
mkdir -p /data/web_static/shared/
echo -e '<html>\n<head>\n</head>\n<body>\nHolberton Temp File\n</body>\n</html>' > /data/web_static/releases/test/index.html
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current
sudo chown -R ubuntu:ubuntu /data/
sudo sed -i "42i location /hbnb_static {\nalias /data/web_static/current;\n}" /etc/nginx/sites-available/default
sudo service nginx restart
