python3 -m venv cloudy   # creaty cloudy as env


#> create virtual env
   virtualenv mypython

#> to activate the env
   <name>\Scripts\activate

#> to run the app in venv
   set FLASK_APP=dynamic.py
   set FLASK_DEBUG=1
   flask run

#> list all the virtual env
   lsvirtualenv -b

#> list all the packages in the env
   pip freeze