#!/usr/bin/env bash
# Sets up web servers for the deployment of web_static


apt-get update
apt-get install -y nginx

mkdir -p /data/
mkdir -p /data/web_static/
mkdir -p /data/web_static/releases/
mkdir -p /data/web_static/shared/
mkdir -p /data/web_static/releases/test/
touch /data/web_static/releases/test/index.html

echo "<h1> Hello World </h1>" > /data/web_static/releases/test/index.html

ln -sF /data/web_static/releases/test/ /data/web_static/current

chown -R ubuntu /data/
chgrp -R ubuntu /data/

printf %s " server {
        listen          80 default_server;
        listen          [::]:80 default_server;
        root            /data/web_static/current;
        index           index.html index.htm;
        location /redirect_me {
                return 301 https://www.youtube.com/watch?v=QH2-TGUlwu4;
        }

	location /hbnb_static {
		alias /data/web_static/current;
		index index.html index.htm;
	}

        error_page 404 /404.html;
        location /404 {
                root /etc/nginx/html;
                internal;
        }
        add_header X-Served-By '$HOSTNAME';
}" > /etc/nginx/sites-available/default
service nginx restart
