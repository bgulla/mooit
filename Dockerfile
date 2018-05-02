FROM python:2.7-alpine3.7
MAINTAINER Brandon Gulla "hey@brandongulla.com"
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
ENTRYPOINT ["python"]
CMD ["app.py"]
