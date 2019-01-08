FROM python:2
MAINTAINER Brandon Gulla "hey@brandongulla.com"
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
ENTRYPOINT ["python"]
EXPOSE 8443
CMD ["wsgi.py"]
