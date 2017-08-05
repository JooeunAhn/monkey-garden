
FROM python:3.6
RUN groupadd -r uwsgi && useradd -r -g uwsgi uwsgi
RUN pip3 install django==1.10.6 uwsgi==2.0.14
WORKDIR /monkey_garden
COPY monkey_garden /monkey_garden
ADD requirements.txt /monkey_garden/
RUN pip3 install -r requirements.txt
RUN python3 manage.py collectstatic --settings=monkey_garden.settings.prod
EXPOSE 8080
USER uwsgi
ENV DJANGO_SETTINGS_MODULE monkey_garden.settings.prod
CMD ["uwsgi", "--http", "0.0.0.0:8080", "--wsgi-file", "/monkey_garden/monkey_garden/wsgi.py"]

