FROM python:3.12-alpine

# Upgrade zlib from the Alpine repositories
RUN apk upgrade --no-cache zlib

WORKDIR /app

CMD ["python", "--version"]
