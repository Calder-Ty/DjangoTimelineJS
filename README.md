# DjangoTimelineJS
A django powered backend for working with Timeline JS

[Timeline JS](https://timeline.knightlab.com/) is a javascript webapp that allows you to tell vibrant stories through timelines. It however (in it's simplest form) requires that you use a google spreadsheet to store your data. This can be harder to work with. DjangoTimelinJS provides a simple ready to use backend for handling your Event Data. 

# Installation
To download this code, simply clone this repository
```
git clone https://github.com/Calder-Ty/DjangoTimelineJS.git
```

To install requirments
```{bash}
cd DjangoTimelineJS
pip install -r requirements.txt
```
Finaly migrate the database and add yourself as a superuser
```
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
```
