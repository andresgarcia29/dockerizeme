FROM python:3.8

RUN pip install poetry

RUN mkdir /app
COPY poetry.lock /app
COPY pyproject.toml /app

WORKDIR /app
RUN poetry config virtualenvs.create false --local
RUN poetry install

COPY /app /app

CMD ["python", "main.py"]
