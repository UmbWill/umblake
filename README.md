# umblake
Move data from MSSQL to Postgres using Django-Docker

A way to move data from one container with MSSQL to another container with Django+PostgreSQL

**How to run:**

First lets move into the project folder and create the enviroment using the requirements.txt file

```
pipenv install -r path/to/requirements.txt
```
then we are ready to create the container in docker
```
sudo docker-compose up --build -d
docker exec -it djlake_web_1  python manage.py makemigrations
docker exec -it djlake_web_1  python manage.py migrate
docker exec -it djlake_web_1  python manage.py mig

```
**Mig** is the magic command that moves the data from one database to another. 
It is use the models of Django, so you have to know the sorurce tables (columns and data types).

If the user database will be update, we can just run again 

```
docker exec -it djlake_web_1  python manage.py mig

```
this is not an automatic way to update the PostgreSQL database, but it is a first step to reach this goal.
