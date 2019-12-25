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
2. Build+Run the docker container for this project and db
``` 
docker-compose up -d --build 
```
3. Setup Database Schema
 ```
docker-compose exec web python manage.py migrate 
```
4. Check psql is running 
```
docker-compose exec db psql --username=postgres --dbname=postgres_db
```
5. Check App is running by visiting
```
[http://localhost:8000/](http://localhost:8000/)
```
6. Run Unit Tests using
```
docker-compose exec web python manage.py test
```

## Steps Done
#### Project Structure is as follows:
backend_qctrl contains project config while controls contains the api models serializers, views and urls. 
#### Specifics of tasks are:
- [x] Created API for controls which accessible with GET, POST, UPDATE, DELETE Requests
- [x] Can View the API using django-rest-framework-json-api with pagination view (max 5 per page)
- [x] Upload and Export functionality implemented using library django-import-export
- [x] Conforms to JSON:API Specification
- [x] Added a .env.dev file and the docker-compose file which contains credentials this should be changed for security by the users



## Resources Used
https://testdriven.io/blog/dockerizing-django-with-postgres-gunicorn-and-nginx/#docker : Consulted to Create Django and Postgres Backend on Docker

 