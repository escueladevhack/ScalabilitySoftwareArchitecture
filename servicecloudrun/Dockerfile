FROM python:3.7-slim
COPY src/ /app/
COPY Pipfile /app
COPY Pipfile.lock /app
#RUN ls -la /app/*
WORKDIR /app
RUN pip install pipenv
RUN pipenv install --system --deploy --ignore-pipfile
# set enviroment variables
ENV CREDENTIALS_PATH="TEST"
# Install production dependencies.
RUN pip install Flask gunicorn
CMD exec gunicorn --bind :$PORT --workers 1 --threads 8 api:app