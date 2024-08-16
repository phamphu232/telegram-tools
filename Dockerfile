FROM docker.io/python:3.7-alpine3.16
ARG UID=1000
ARG GID=1000
RUN deluser app 2>/dev/null || true
RUN addgroup -g ${GID} app \
    && adduser -u ${UID} -G app -h /home/app -s /sbin/nologin -D app
CMD ["tail", "-f", "/dev/null"]