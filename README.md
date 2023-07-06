# Django Blog applictaion 

1. Django  :
This blog application built with Django allows users to sign up and log in. Once logged in, users can view posts, share them, send emails, like posts, and comment on them.





## Technologies Used

 - [Web framework: Django ]()
 


##  Deployment

To deploy this project run


1. Clone the repository or download  the zip and extract :

```bash
https://github.com/Mhdjaseer/Blog-application.git
```
or download the zip file 

2. Create virtual enviorment:

```bash
 python -m venv env
```
2. activate env:

```bashe
env\scripts\activate   (/|\)
```
3. install django:

```bash
 pip install django

```


4. Install Required Dependencies:

```bash
 pip install -r requirements.txt

```
5. create database .makemigration/migrate :

```bash
 python manage.py makemigrations
 python manage.py migrate
 python manage.py createsuperuser
 // add post using admin

```

6. run your server :

```bash
python manage.py runserver 

```



