# Setup Development Environment

You need a working python installation with virtual environment support (This needs an extra package on some Linux distributions).

* Create a python virtual environment in the root directory of this project and activate it:
```bash
python -m venv .venv
. .venv/bin/activate
```
* Install dependencies defined in `requirements.txt`:
```
pip install -r requirements.txt
```

Run the development server with:

```bash
uvicorn src.api:app --reload
```

The API should be reachable under <http://127.0.0.1:8000> with automatic API documentation under <http://127.0.0.1:8000/docs>

# Runnig inside a Docker Container

The project provides a Dockerfile that can be used to run a production ready instance of the service.
A working installation of Docker is needed to run the container.
In order to build an run the container do the following.

* Build the container under the name `ssedemo`:
```bash
docker build -t ssedemo --target=prod .
```

* Run the container exposing the service under port 8080
```
docker run --rm -p 8080:80 ssedemo
```

The API should be reachable under <http://127.0.0.1:8080> with automatic API documentation under <http://127.0.0.1:8080/docs>