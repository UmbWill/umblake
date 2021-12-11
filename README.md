# umblake
Move data from MSSQL to Postgres using Django-Docker

A way to move data from one container with MSSQL to another container with Django+PostgreSQL

**How to run:**
```
sudo docker-compose up --build -d
docker exec -it djlake_web_1  python manage.py makemigrations
docker exec -it djlake_web_1  python manage.py migrate
docker exec -it djlake_web_1  python manage.py mig

```
Mig is the magic command that moves the data from one database to another. 
It is use the models of Django, so you have to know the sorurce tables (columns and data types).
