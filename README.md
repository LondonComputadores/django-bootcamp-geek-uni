# django-bootcamp-geek-uni
This is a Django Bootcamp from Udemy by Geek University as a Recap where will be built 3 different applications such as a Real Time, Geo location, and Data Manipulation one, which can be seen topics like Websockets, Facebook Login, PDF Creator, Customized models and admin, tests, deploy and so on...

#### Link Application 1: This Repo
#### Link Application 2:
#### Link Application 3:


## What's going on Application 1: Django Basics Recap

Terminal's issued commands:

$ python -m venv venv
$ source venv/bin/activate
$ pip install django
$ pip freeze > requirements.txt
$ django-admin startprojec django1 .
$ python manage.py startapp app
$ python manage.py runserver
$ python manage.py makemigrations
$ python manage.py migrate
$ python manage.py createsuperuser
$ python manage.py shell (
    >>> from app.views import index
    >>> dir(index)
    >>> from app.models import Product
    >>> dir(Product)
    >>> product = Product.objects.all()
    >>> product
    >>> product.id
    >>> product.pk
    >>> product = Product.objects.first()
    >>> product = Product.objects.filter(id=1)
    >>> Product.objects.filter(id=1)
    >>> for product in product:
    ...     print(product)
    >>> Product.objects.count()
    >>> from django1.settings import BASE_DIR
    >>> BASE_DIR
    >>> STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
    >>> STATIC_ROOT
)