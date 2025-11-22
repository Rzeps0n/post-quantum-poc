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

#RUN echo -e "LoadModule ssl_module modules/mod_ssl.so\nInclude /etc/apache2/sites-available/default-ssl.conf\nLoadModule socache_shmcb_module modules/mod_socache_shmcb.so" >> /etc/apache2/apache2.conf

RUN openssl req -x509 -nodes -days 365 -newkey rsa \
-keyout /etc/ssl/apache2/server.key \
-out /etc/ssl/apache2/server.crt \
-subj "/C=PL/ST=Lesser Poland/L=Cracow/O=AGH University of Cracow/CN=localhost"

#COPY default-ssl.conf /etc/apache2/sites-available/default-ssl.conf
COPY default-ssl.conf /etc/apache2/mods-available/ssl.conf

RUN a2enmod ssl socache_shmcb && a2ensite default-ssl && apache2ctl configtest

CMD ["apache2", "-DFOREGROUND"]

EXPOSE 80 443
