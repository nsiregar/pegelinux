### Setting up Virtualenv

You need pipenv for easy managing python project(prevent dependency break). Install it with:

```
$ sudo pip install pipenv
```

Clone pegelinux repository

```
$ git clone https://github.com/<user>/pegelinux
```

Install all requirement packages with pipenv:

```
$ cd pegelinux
$ pipenv install
Creating a virtualenv for this project...
Pipfile: /tmp/pegelinux/Pipfile
Using /usr/bin/python3.6m (3.6.5) to create virtualenv...
⠋Running virtualenv with interpreter /usr/bin/python3.6m
Using base prefix '/usr'
New python executable in /home/<user>/.local/share/virtualenvs/pegelinux-MMjIeVK8/bin/python3.6m
Also creating executable in /home/<user>/.local/share/virtualenvs/pegelinux-MMjIeVK8/bin/python
Installing setuptools, pip, wheel...done.
Setting project for pegelinux-MMjIeVK8 to /tmp/pegelinux

Virtualenv location: /home/<user>/.local/share/virtualenvs/pegelinux-MMjIeVK8

```

To activate pipenv, use `pipenv shell`

```
$ pipenv shell
Launching subshell in virtual environment…
 . /home/<user>/.local/share/virtualenvs/pegelinux-MMjIeVK8/bin/activate
```

Verify if you are inside pipenv:

```
$ pip -V
pip 10.0.1 from /home/<user>/.local/share/virtualenvs/pegelinux-MMjIeVK8/lib/python3.6/site-packages/pip (python 3.6)
```

### Setting up database

Before you can use flask, you need to specify flask app environment:

```
export FLASK_APP=app.py
```

After that, migrate flask db:

```
$ flask db migrate           
INFO  [alembic.runtime.migration] Context impl SQLiteImpl.
INFO  [alembic.runtime.migration] Will assume non-transactional DDL.
```

After that, do db upgrade:

```
$ flask db upgrade 
INFO  [alembic.runtime.migration] Context impl SQLiteImpl.
INFO  [alembic.runtime.migration] Will assume non-transactional DDL.
INFO  [alembic.runtime.migration] Running upgrade  -> 3b1f45ed96c7, empty message
INFO  [alembic.runtime.migration] Running upgrade 3b1f45ed96c7 -> fbfec56d097e, empty message
INFO  [alembic.runtime.migration] Running upgrade fbfec56d097e -> a4702859796a, empty message
INFO  [alembic.runtime.migration] Running upgrade a4702859796a -> 27630d92b728, empty message
INFO  [alembic.runtime.migration] Running upgrade 27630d92b728 -> 5d01d82188c8, empty message
INFO  [alembic.runtime.migration] Running upgrade 5d01d82188c8 -> 07105363599f, empty message
INFO  [alembic.runtime.migration] Running upgrade 07105363599f -> b510973ced08, empty message
INFO  [alembic.runtime.migration] Running upgrade b510973ced08 -> 3872d2c85f25, empty message
```

Reference: https://flask-migrate.readthedocs.io/en/latest/

And now you can run pegelinux app with:

```
$ flask run
 * Environment: production
   WARNING: Do not use the development server in a production environment.
   Use a production WSGI server instead.
 * Debug mode: off
```

Browse http://127.0.0.1:5000/ and you are done~