FROM python:3.10

# We copy just the requirements.txt first to leverage Docker cache
COPY ./requirements.txt /app/requirements.txt
RUN apt-get update && \
    apt-get install -y build-essential libzbar0

WORKDIR /app
RUN pip install -r requirements.txt
COPY . /app
ENTRYPOINT [ "sh" ]
CMD [ "ejecutar.sh" ]

