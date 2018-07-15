### Running automated tests

Since we have yet to decide on how we test our application, test dependencies have not been added to pipfile. Install it manually:

```
pip install pytest

pip install expects
```

Run the tests using unittest:

```
python -m unittest test.test_app
```

To run all tests using pytest's test discovery:

```
pytest -v
```
