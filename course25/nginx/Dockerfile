FROM nginx:latest

# Add start script
ADD ./config/start.sh /
RUN chmod +x start.sh

# Add nginx config file
ADD ./config/nginx.tmpl /

## Add SSL certs to location specified in nginx.conf
#ADD ./config/*.crt /etc/ssl/certs/
#ADD ./config/*.key /etc/ssl/private/

# Execute start script
CMD ["./start.sh"]