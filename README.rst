Search
******

Django application for searching

Install
=======

Virtual Environment
-------------------

::

  virtualenv --python=python3 venv-search
  source venv-search/bin/activate

  pip install -r requirements/local.txt

Testing
=======

::

  find . -name '*.pyc' -delete
  py.test -x

Usage
=====

::

  py.test -x && \
      touch temp.db && rm temp.db && \
      django-admin.py syncdb --noinput && \
      django-admin.py demo_data_login && \
      django-admin.py demo_data_search && \
      django-admin.py runserver

Release
=======

https://www.kbsoftware.co.uk/docs/
