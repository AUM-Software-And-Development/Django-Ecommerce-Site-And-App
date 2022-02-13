![alt text](https://lucid.app/publicSegments/view/54f2757e-9c2b-428d-ae1a-2bad5f74ea61/image.jpeg)

# Installation steps:

    py -m venv
    venv\Scripts\activate (Use tab to quick find)
    pip install django
    django-admin startproject ecommerce_project

# Dependencies:\

    pip install pytest
    pip install pytest-django
    pip install pytest-factoryboy
    pip install pytest-selenium
    download a ChromeDriver for the version of Chrome

# Notes:\

    pytest -m "not selenium" -rP
    py manage.py dumpdata inventory.category --indent 4 > new.json
    py manage.py dumpdata inventory.category > new.json
