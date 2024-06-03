# start by pulling the python image
FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE=1
# copy the requirements file into the image
COPY ./requirements.txt /app/requirements.txt

# switch working directory
WORKDIR /app

# install the dependencies and packages in the requirements file
RUN pip install -r requirements.txt
RUN pip install gunicorn

# copy every content from the local file to the image
COPY . /app

EXPOSE 8000

CMD ["gunicorn -w 4 -b 0.0.0.0 'server:app'"]