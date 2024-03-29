FROM python:3.8.5
LABEL description="Compose Editor - gethue.com"

ADD . /build

RUN mkdir /app
WORKDIR /app

# Should update OS packages

RUN python -m pip install --upgrade pip
# Should use a virtual env
#&& pip install virtualenv && python -m venv python_env

# SHELL ["/bin/bash", "-c"]
# RUN source python_env/bin/activate

# UI
# FROM node:14 AS ui
# sudo apt-get install -y nodejs
RUN curl -sL https://deb.nodesource.com/setup_12.x | bash - \
  && apt-get install -y nodejs
RUN cd /build/sql-scratchpad && \
    npm install && \
    sed -i "s/http:\/\/localhost:8005/https:\/\/api.gethue.com/g" index.html && \
    mv /build/sql-scratchpad /app/static/

# API
RUN python -m pip install /build && rm -rf /build && python -m pip install mysqlclient==2.0.3

# Should have a more elegant conf dir
COPY compose/docker/local_settings.py /usr/local/lib/python3.8/site-packages/compose/conf/local_settings.py
# COPY compose/docker/local_settings.py compose/conf/local_settings.py

COPY compose/docker/startup.sh .
COPY compose/docker/db-demo.sqlite3 .

# Should chown and use a compose user

# Should copy virtual env into new lean image and same with UI

EXPOSE 8005
ENTRYPOINT ["./startup.sh"]
