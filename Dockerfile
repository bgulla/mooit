#FROM python:2-alpine
FROM python:2#:2-alpine
MAINTAINER Brandon Gulla "hey@bgulla.dev"

COPY ./src /app

# Create no priveleged user
#RUN addgroup -S 1001 && \
#    adduser -S -G 1001 1001 && \
RUN    chown -R 1001 /app
WORKDIR /app

# Install the dependencies from PIP
RUN pip install -r requirements.txt

USER 1001

ENTRYPOINT ["python"]
CMD ["mooit.py"]
