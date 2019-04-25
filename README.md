# Python REST demo with Flask

## Setup

The first time around, run:

```
$ virtualenv venv
$ source venv/bin/activate
$ pip install flask flask-jsonpify flask-sqlalchemy flask-restful requests
$ pip freeze
```

This creates a new virtual environment, installs necessary dependencies and fixes those to the custom created environment called `venv`.

From the second time onward, run:

```
$ source venv/bin/activate
```

This reactivates a previously created virtual env, so that all installed dependencies are in place.

To deactivate the virtual environment, simply execute `deactivate`.

## Execution

```
$ python server.py
```

## Links

* [Building a basic RESTful API with Python](https://www.codementor.io/sagaragarwal94/building-a-basic-restful-api-in-python-58k02xsiq)
* [How to use Python virtualenv](https://www.pythonforbeginners.com/basics/how-to-use-python-virtualenv)