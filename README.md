# Q-CTRL Backend Challenge 
This repository is addressing the backend challenge from Q-CTRL and contains the following: 

## Requiements Met
1. Create a control :white_check_mark:
1. List all controls (five per page) :white_check_mark:
1. Get a specific control :white_check_mark:
1. Update a specific control - :white_check_mark:
1. Delete a specific control - :white_check_mark:
1. Bulk upload controls in CSV format - :white_check_mark:
1. Download controls in CSV format - :white_check_mark:

## How To Run
1. Clone Project
1. Build and Run the Dockerfile and Spin Up Containers
2. May have to run postgresql setup (unsure)
2. Run 
``` 
docker-compose build 
```
 
docker-compose exec web python manage.py migrate to make sure database migrations work.
2. Check psql is running docker-compose exec db psql --username=postgres --dbname=postgres_db

## Steps
Created API for controls

## Resources Used
https://testdriven.io/blog/dockerizing-django-with-postgres-gunicorn-and-nginx/#docker : Consulted to Create Django and Postgres Backend on Docker

 