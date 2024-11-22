FROM python:3.11

WORKDIR /app

RUN pip install poetry
COPY ./pyproject.toml /app/pyproject.toml
COPY ./poetry.lock /app/poetry.lock
RUN poetry config virtualenvs.create false
RUN poetry install --no-interaction --no-ansi --no-dev

COPY . /app

EXPOSE 8080
CMD ["python", "app/main.py"]