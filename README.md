# For developers. 
This application is wrappered by Docker for both frontend and backend. 
The following procedures instantly lead you to develop the application. 

## Backend. 
Enter the following commands for the first time.
```
 sudo docker-compose -f docker-compose.dev.yml run django python manage.py makemigrations
 sudo docker-compose -f docker-compose.dev.yml run django python manage.py migrate
 sudo docker-compose -f docker-compose.dev.yml run django python manage.py createsuperuser
```
Then, from the next time, you can launch up django app by `docker-compose -f docker-compose.dev.yml up`.
Access to `localhost:8000/admin` or `localhost:8000/api`.
It is noted that, the root path (`localhost:8000`) returns the error page since the url path is not set.

## Frontend.
First you should type,  
`docker-compose -f docker-compose.dev.yml run app yarn install`

From the next time, you can launch up react redux app by `docker-compose -f docker-compose.dev.yml up`.
Access to `localhost:3000` will show you react redux app.

# Frequently used command. 
- Change owner : `sudo chown -R $USER:$USER .` 
    - This command is used if the following error occurs. : `error checking context: 'can't stat '/home/toshiaki/Desktop/scrapquiz/db/data''.`

- Start new app.
` sudo docker-compose run django python manage.py startapp <app_name>`

``` 
sudo docker-compose run django python manage.py makemigrations
sudo docker-compose run django python manage.py migrate 
sudo docker-compose run django python manage.py createsuperuser 
```
``` 
 docker-compose exec django python manage.py collectstatic --no-input --clear
 ```

 # for development server. 
 ```
 sudo docker-compose -f docker-compose.dev.yml run django python manage.py makemigrations
 sudo docker-compose -f docker-compose.dev.yml run django python manage.py migrate
 sudo docker-compose -f docker-compose.dev.yml run django python manage.py createsuperuser
```

# Development histories  

## Create django project by docker. 

Type  
`docker-compose -f docker-compose.start.yml build` : build image.  
`docker-compose -f docker-compose.start.yml web django-admin startproject backend .` : Create "backend" django project.  

## Change settings
- Change database settings.
- Edit ALLOWED_HOSTS.
- Create `logs` directory.

## Prepare docker file for development. 

- To activate celery 
    - Add magic word to `backend/__init__.py`. 
    - Add celery packages to INSTALLED_APPS of setting file. 
    - Add celery.py to `backend` directory.
    - Edit `docker-compose.dev.yml` file for celery to find setting file of django.

## REST api settings
- Follow this site https://www.digitalocean.com/community/tutorials/build-a-to-do-application-using-django-and-react

## Frontend settings.
- Initialize (Installing node is required at first.)
`npx create-react-app frontend --template redux-typescript`  
