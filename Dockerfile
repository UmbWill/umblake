# syntax=docker/dockerfile:1
FROM python:3
RUN pip install --upgrade pip
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR /opt/djlake
COPY requirements.txt /opt/djlake


RUN apt-get update && apt-get install -y --no-install-recommends \
    unixodbc-dev \
    unixodbc \
    libpq-dev 

RUN apt install apt-utils -y

RUN curl https://packages.microsoft.com/keys/microsoft.asc | apt-key add -
RUN curl https://packages.microsoft.com/config/ubuntu/18.04/prod.list > /etc/apt/sources.list.d/mssql-release.list
RUN apt-get update
RUN ACCEPT_EULA=Y apt-get install -y --allow-unauthenticated msodbcsql17
RUN ACCEPT_EULA=Y apt-get install -y --allow-unauthenticated mssql-tools
RUN echo 'export PATH="$PATH:/opt/mssql-tools/bin"' >> ~/.bash_profile
RUN echo 'export PATH="$PATH:/opt/mssql-tools/bin"' >> ~/.bashrc


#RUN sudo apt-get install python3-dev default-libmysqlclient-dev build-essential
RUN pip install -r requirements.txt
COPY . /opt/djlake
#RUN python manage.py syncdb
#RUN python manage.py makemigrations
#RUN python manage.py migrate
#RUN python manage.py inspectdb > models.py

