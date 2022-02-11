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

# Development histroy.  

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