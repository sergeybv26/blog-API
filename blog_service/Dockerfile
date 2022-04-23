# Builder

FROM python:3.9-alpine as builder

WORKDIR /usr/src/blog_api

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apk update && apk add postgresql-dev gcc python3-dev musl-dev

RUN pip install --upgrade pip
RUN pip install flake8==3.9.2
COPY . .
RUN flake8 --ignore=E501,F401

COPY ./requirements.txt .
RUN pip wheel --no-cache-dir --no-deps --wheel-dir /usr/src/blog_api/wheels -r requirements.txt

# Final

FROM python:3.9-alpine

RUN mkdir -p /home/blog_api

RUN addgroup -S blog_api && adduser -S blog_api -G blog_api

ENV HOME=/home/blog_api
ENV BLOG_API_HOME=/home/blog_api/web
RUN mkdir $BLOG_API_HOME
WORKDIR $BLOG_API_HOME

RUN apk update && apk add libpq
COPY --from=builder /usr/src/blog_api/wheels /wheels
COPY --from=builder /usr/src/blog_api/requirements.txt .
RUN pip install --no-cache /wheels/*

COPY ./entrypoint.sh .
RUN sed -i 's/\r$//g' $BLOG_API_HOME/entrypoint.sh
RUN chmod +x $BLOG_API_HOME/entrypoint.sh

COPY . $BLOG_API_HOME

RUN chown -R blog_api:blog_api $BLOG_API_HOME

USER blog_api

ENTRYPOINT ["/home/blog_api/web/entrypoint.sh"]
