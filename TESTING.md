### Running automated tests

Since we have yet to decide on how we test our application, test dependencies have not been added to pipfile. Install it manually:

```
pip install pytest

pip install expects
```

Initialize the database for test:

```
APP_CONFIG=config.application.TestingConfig flask db upgrade
```

Run the tests using unittest:

```
APP_CONFIG=config.application.TestingConfig python -m unittest test.test_app
APP_CONFIG=config.application.TestingConfig python -m unittest test.test_app_with_expect
```

To run all tests using pytest's test discovery:

```
APP_CONFIG=config.application.TestingConfig pytest -v
```
