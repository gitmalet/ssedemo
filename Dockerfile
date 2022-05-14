# Base containing dependencies for all other containers
FROM python:3.10 AS base

WORKDIR /app

COPY ./requirements.txt /app/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

# Production ready container
FROM base AS prod

COPY src /app/src
EXPOSE 80
CMD ["uvicorn", "src.api:app", "--host", "0.0.0.0", "--port", "80"]

# Containerized tests
FROM base AS test

COPY src /app/src
COPY tests /app/tests
RUN pip install --no-cache-dir --upgrade pytest requests
CMD ["python", "-m", "pytest", "tests"]