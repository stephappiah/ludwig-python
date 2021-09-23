# ludwig-python
A sentence search engine that fetches examples from trusted news/media websites. Great for improving writing & speaking better English.

# Installation
Using [docker](https://www.docker.com/), 
Build the image
```
docker-compose build
```
## Run migrations
```
docker-compose run web python manage.py migrate
```

### Run the application
```
docker-compose up
```

Visit the URL ```http://localhost:8000```