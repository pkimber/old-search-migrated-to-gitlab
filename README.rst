Search
******

Django application for searching

Install
=======

Virtual Environment
-------------------

Note: replace ``patrick`` with your name (checking in the ``example`` folder
to make sure a file has been created for you)::

  mkvirtualenv dev_search
  pip install -r requirements/local.txt

  echo "export DJANGO_SETTINGS_MODULE=example.dev_patrick" >> $VIRTUAL_ENV/bin/postactivate
  echo "unset DJANGO_SETTINGS_MODULE" >> $VIRTUAL_ENV/bin/postdeactivate

  add2virtualenv ../base
  add2virtualenv ../login
  add2virtualenv .
  deactivate

To check the order of the imports::

  workon dev_search
  cdsitepackages
  cat _virtualenv_path_extensions.pth

Check the imports are in the correct order e.g::

  /home/patrick/repo/dev/app/search
  /home/patrick/repo/dev/app/login
  /home/patrick/repo/dev/app/base

Testing
=======

Using ``pytest-django``::

  workon dev_search
  find . -name '*.pyc' -delete
  py.test

To stop on first failure::

  py.test -x

Usage
=====

::

  workon dev_search

  py.test -x && \
      touch temp.db && rm temp.db && \
      django-admin.py syncdb --noinput && \
      django-admin.py migrate --all --noinput && \
      django-admin.py demo_data_login && \
      django-admin.py demo_data_search && \
      django-admin.py runserver

Release
=======

https://github.com/pkimber/docs
