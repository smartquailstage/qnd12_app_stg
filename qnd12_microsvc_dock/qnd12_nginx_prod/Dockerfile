FROM nginx:1.23.0-alpine

COPY ./nginx/* /etc/nginx/
COPY ./nginx/run.sh /run.sh
COPY ./my-domain.com/* /etc/letsencrypt/live/nethousing.io

ENV LISTEN_PORT=80
ENV NGINX_PROXY=http://qnd12_app_stg:9000
ENV APP_HOST=qnodex_app
ENV APP_PORT=9000

USER root

RUN apk add --no-cache openssl bash
RUN chmod +x /run.sh

RUN mkdir -p /qnd12_app_stg/qnd12_app_stg/staticfiles && \
chmod 755 /qnd12_app_stg/qnd12_app_stg/staticfiles && \
mkdir -p /qnd12_app_stg/qnd12_app_stg/mediafiles && \
chmod 755 /qnd12_app_stg/qnd12_app_stg/mediafiles && \
mkdir -p /qnd12_app_stg/qnodex_app/media && \
chmod 755 /qnd12_app_stg/qnodex_app/media

VOLUME /qnd12_app_stg/qnd12_app_stg/staticfiles
VOLUME /qnd12_app_stg/qnd12_app_stg/mediafiles
VOLUME /vol/www
VOLUME /vol/proxy
VOLUME /etc/letsencrypt

CMD ["/run.sh"]