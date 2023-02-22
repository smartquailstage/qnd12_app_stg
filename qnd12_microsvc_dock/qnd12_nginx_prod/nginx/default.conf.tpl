server { 
    listen 80;
    server_name ${DOMAIN}
    www.${DOMAIN} Ip_Adress_droplet 127.0.0.1;
    
    location /.well-known/acme-challenge/ {
        root /vol/www/;
        }
        
    location / {
        return 301 https://$host$request_uri;
        }
}




