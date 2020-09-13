### Setting up Virtualenv

You need pipenv for easy managing python project(prevent dependency break). Install it with:

```
$ sudo pip install pipenv
```

Don't forget to **fork** pegelinux repository to your github account: https://github.com/nsiregar/pegelinux

After that, clone pegelinux repository from your account

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
export APP_CONFIG=config.application.DevelopmentConfig
```

After that, migrate flask db:

```
$ flask db stamp head
INFO  [alembic.runtime.migration] Context impl SQLiteImpl.
INFO  [alembic.runtime.migration] Will assume non-transactional DDL.
INFO  [alembic.runtime.migration] Running stamp_revision  -> xxxxxxxxxx
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


## Using Docker

By using docker, you don't need to setup anything except installing docker and docker-compose. Please open official documentation for each tools to install it for your OS.

### Docker compose configuration
First copy the example file to docker-compose.yml

```
cp docker-compose.yml.example docker-compose.yml
```

### Start server
Run this command to automatically create and running web and database container

```
inv docker-server start
```
Wait after a while, there will be some error because we just created the container but haven't migrate tha database yet. **Ctrl + C** to stop
Next we do database migration

```
docker-compose run web flask db upgrade
```
After that you can start again the server

```
inv docker-server start
```
to start and
```
inv docker-server stop
```
to stop.


To apply your code change, please stop the server and rebuild the container by using
```
inv docker-build
```
It will rebuild the container almost instantly, except if you add new dependencies to pipfile, it will rebuild all the dependencies once only.

### Other Method
This will make your container reload when you change your code

First copy the docker-compose.yml.example file to docker-compose.yml

```
cp docker-compose.yml.example docker-compose.yml
```

### Up & Build

For the first time, run this command to automatically create and running web and database container

```
 docker-compose up --build -d
```

### Database migration

We just created a web container and database, so that the application can run we have to migrate the database, first we go into the web container.

```
docker exec -it pegelinux_web_1 bash
```
Run this command to migrate database

```
bash-4.4# flask db migrate
bash-4.4# flask db upgrade
bash-4.4# exit
```

Done, now you can access this web from `localhost:5000`

### Stop container

To stop this container, run this command

```
docker-compose stop
```

If you not change anything on docker-compose.yml, just run this command to running your container

```
docker-compose up -d
```


Do you ever feel like something need a change? We are waiting for your contributions and we <3 PR. See [CONTRIBUTING.md](CONTRIBUTING.md)
