FROM python:3.7-alpine

COPY Pipfile /app/Pipfile

WORKDIR /app

RUN pip install pipenv

RUN pipenv install

CMD ["pipenv", "run", "python", "src/app.py"]
