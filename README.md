To create venv and intsall dependencies type ```pipenv install```

```
cd apps
/manage.py test
```
To run tests
```
cd apps
/manage.py migrate
```
Would create sqlite database.
```
cd apps
/manage.py runserver
```
Would run a server on 127.0.0.1:8000

You can access applications api at /api/applications/

To generate new key use /api/applications/id/generate_new_key

To test key send get request at /api/test with x-api-key http header