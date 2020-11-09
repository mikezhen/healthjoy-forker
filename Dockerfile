FROM node:15-alpine AS web

WORKDIR /usr/app
COPY web .
RUN npm install
RUN npm run build


FROM python:3-alpine

WORKDIR /usr/app
COPY forker forker
COPY --from=web /usr/app/build forker/static
COPY setup.py .
RUN pip install .