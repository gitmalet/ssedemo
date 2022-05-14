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