server {
    listen 443 ssl;
    server_name
    ${DOMAIN} www.${DOMAIN};
    ssl_certificate 
    /etc/letsencrypt/live/${DOMAIN}/fullchain.pem;
    ssl_certificate_key 
    /etc/letsencrypt/live/${DOMAIN}/privkey.pem;
    
    include /etc/nginx/options-ssl-nginx.conf;
    ssl_dhparam /vol/proxy/ssl-dhparams.pem;
    add_header Strict-Transport-Security
    "max-age=31536000;
    includeSubDomains" always;
    
    location /static {
        alias /qnd12_app_stg/qnd12_app_stg/staticfiles;
        client_max_body_size 1000M;
        }
        
    location / {
        uwsgi_pass ${APP_HOST}:${APP_PORT};
        include /etc/nginx/uwsgi_params;
        client_max_body_size 1000M;
        }
}