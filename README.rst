Django-CRM
==========

Django CRM is opensourse CRM developed on django framework. It has all the basic features of CRM to start with. We welcome code contributions and feature requests via github.


.. image:: https://travis-ci.org/MicroPyramid/Django-CRM.svg?branch=master
   :target: https://travis-ci.org/MicroPyramid/Django-CRM

.. image:: https://coveralls.io/repos/github/MicroPyramid/Django-CRM/badge.svg?branch=master
   :target: https://coveralls.io/github/MicroPyramid/Django-CRM?branch=master

.. image:: https://landscape.io/github/MicroPyramid/Django-CRM/master/landscape.svg?style=flat
   :target: https://landscape.io/github/MicroPyramid/Django-CRM/master
   :alt: Code Health

.. image:: https://img.shields.io/github/license/MicroPyramid/Django-CRM.svg
    :target: https://pypi.python.org/pypi/Django-CRM/

.. image:: https://www.codetriage.com/micropyramid/django-crm/badges/users.svg
    :target: https://www.codetriage.com/micropyramid/django-crm

http://django-crm.readthedocs.io for latest documentation


This project contains the following modules.

   * Contacts
   * Accounts
   * Cases
   * Leads
   * Opportunity
   * Planner


Installation - Requirements
===========================


Ubuntu 64bit - 16.04
--------------------
$ sudo apt-get update && apt-get upgrade -y

$ sudo apt-get install -y curl wget libpq-dev python3-dev gem ruby ruby-dev build-essential libssl-dev libffi-dev python-dev python-virtualenv python-pip git redis-server libtiff5-dev libjpeg8-dev zlib1g-dev libfreetype6-dev liblcms2-dev libwebp-dev libharfbuzz-dev libfribidi-dev tcl8.6-dev tk8.6-dev python-tk

$ sudo gem install sass


If you cloned the package from git use virtualenv to install requirements::

    pip install -r requirements.txt

Visit our Django web development page [Here](https://micropyramid.com/django-ecommerce-development/)

Demo Available `here`_.

Demo credentials for Django CRM:

  * **Email:** admin@micropyramid.com
  * **Password:** admin

Feature requests and bug reports
================================
We welcome your feedback and support, raise github issue if you want to report a bug or request new feature. we are glad to help.

Need additional commercial support? `Contact us here`_

.. _contact us here: https://micropyramid.com/contact-us/

.. _here: https://django-crm.micropyramid.com/

---------Run ENV 02/01/2019------------
cd /Users/gstearmit/Django-CRM
source django-crm/bin/activate
python manage.py runserver 8080
python manage.py migrate
python manage.py createsuperuser

--> access admin pages : http://127.0.0.1:8081/login or http://127.0.0.1:8080/login
gstearmit@gmail.com / ng******52

---------Env Tach biet--------------
$ virtualenv -p python django-crm
$ django-crm/bin/activate
$ django-crm/bin/pip install django

—————Hard Code —————
$ python -m venv  django-crm
$ cd django-crm
$ source django-crm/bin/activate
$ pip  install -r requirements.txt

(django-crm) gstearmit:Django-CRM gstearmit$ python manage.py createsuperuser
Email: gstearmit@gmail.com
Username: gstearmit
Password:
Password (again):
Superuser created successfully.
(django-crm) gstearmit:Django-CRM gstearmit$ python manage.py runserver 8080
Performing system checks...


---------install Gem ruby ------------

brew install ruby
sudo gem install sass
pip install compressor

--------------------


Error : django.core.exceptions.ImproperlyConfigured: Error loading MySQLdb module.
Did you install mysqlclient?

$ django-crm/bin/pip install mysqlclient
------------------------
Demo credentials for Django CRM:

Email: admin@micropyramid.com
Password: admin@123!@#

-----------------------------------------------
1.0. git code  https://github.com/MicroPyramid/Django-CRM


2.0 Test check case
   $ python manage.py test accounts
    Creating test database for alias 'default'...
    System check identified no issues (0 silenced).
    ..........
    ----------------------------------------------------------------------
    Ran 10 tests in 7.621s

    OK
    Destroying test database for alias 'default'...





