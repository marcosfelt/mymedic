# From https://github.com/tiangolo/uwsgi-nginx-flask-docker
FROM tiangolo/uwsgi-nginx-flask:python3.6

#Install flask ask
COPY flask_ask/ flask_ask/
RUN cd flask_ask/ && pip install .

ENV LISTEN_PORT 443

EXPOSE 443

COPY ./app /app