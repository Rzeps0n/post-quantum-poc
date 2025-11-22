FROM rzepson/oqs-openssl

ENTRYPOINT []

ENV APACHE_RUN_USER=www-data \
    APACHE_RUN_GROUP=www-data \
    APACHE_PID_FILE=/var/run/apache2/apache2.pid \
    APACHE_RUN_DIR=/var/run/apache2 \
    APACHE_LOCK_DIR=/var/lock/apache2 \
    APACHE_LOG_DIR=/var/log/apache2

RUN apt update && apt install -y apache2 && rm -rf /var/cache/apt/archives /var/lib/apt/lists/*

RUN mkdir -p /var/run/apache2 /etc/ssl/apache2 && . /etc/apache2/envvars

RUN openssl ecparam -name prime256v1 -genkey -noout \
    -out /etc/ssl/apache2/server.key && \
    openssl req -x509 -new -key /etc/ssl/apache2/server.key \
    -out /etc/ssl/apache2/server.crt \
    -days 365 \
    -subj "/C=PL/ST=Lesser Poland/L=Cracow/O=AGH University of Cracow/CN=localhost"

COPY default-ssl.conf /etc/apache2/mods-available/ssl.conf

RUN a2enmod ssl socache_shmcb && a2ensite default-ssl && apache2ctl configtest

CMD ["apache2", "-DFOREGROUND"]

EXPOSE 80 443
