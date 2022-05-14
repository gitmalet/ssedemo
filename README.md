# SSE Demo

This repository contains a demo application implementing server side encryption functionality.
The API accepts data and returns it back over REST-like endpoints under `/data`.
The data uploaded via the API is encrypted in memory and decrypted when the data is retrieved again.

The project uses [FastAPI](https://github.com/tiangolo/fastapi) to implement the API and cryptographic primitives from [PyNaCl](https://github.com/pyca/pynacl/).

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

# Run SSE Demo (Docker)

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

# Run SSE Demo Tests (Docker)

You can run the tests in a special container that can be built from the same Dockerfile.

* Build the container under the name `ssedemo-test`:
```bash
docker build -t ssedemo-test --target=test .
```

* Run the container exposing the service under port 8080
```
docker run --rm ssedemo-test
```

# FAQ

* Why PyNaCL?
PyNaCl was chosen because it provides bindings to [LibSodium](https://github.com/jedisct1/libsodium) which implementing modern cryptographic primitives with an API that is hard to misuse.
The python library [Cryptography](https://github.com/pyca/cryptography) could be used instead as implements the same idea.
Other python cryptography libraries like the [PyCryptodome](https://github.com/Legrandin/pycryptodome) are error-prone and should not be used if the low level access they provide is not needed.

* What are the possible improvements about the SSE Demo?
Authentication and user management would be the next step to get a more usable application.
Key management besides better than storing the key on the file system next to the code would be great too.
There is currently no persistence in this demo and test coverage, error handling and deployment options could be improved as well.


