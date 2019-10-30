FROM python:3.7

# Add code
ADD ./pizza_app /srv/starter/pizza_app
ADD ./pizza_auth_app /srv/starter/pizza_auth_app
ADD ./pizza_project /srv/starter/pizza_project
ADD ./rest_api_app /srv/starter/rest_api_app
ADD ./static /srv/starter/static
ADD ./manage.py /srv/starter/manage.py


# Install application requirements
ADD ./requirements.txt /srv/starter/
ADD ./requirements_deploy.txt /srv/starter/
RUN pip3 install -r /srv/starter/requirements_deploy.txt
RUN pip3 install -r /srv/starter/requirements.txt

# Add start script
ADD ./config/start.sh /

# Add uWSGI config
ADD ./config/django-uwsgi.ini /etc/uwsgi/django-uwsgi.ini

# Add database check script
ADD ./config/database-check.py /srv/config/database-check.py

# Create django user, will own the Django app
RUN adduser --no-create-home --disabled-login --group --system django
RUN chown -R django:django /srv/starter

# Execute start script
CMD ["./start.sh"]