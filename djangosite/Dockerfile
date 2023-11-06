# syntax=docker/dockerfile:1

FROM nvidia/cuda:11.7.1-runtime-ubuntu22.04

RUN apt-get update && apt-get install -y software-properties-common
RUN apt-get install -y g++-11 make python3 python-is-python3 pip python3.10-venv

RUN apt-get install -y build-essential libpq-dev  

ENV PYTHONUNBUFFERED=1

COPY requirements_frozen.txt .

# Install python venv and upgrade pip, install postgres client and requirements
RUN python -m venv /py && \
    /py/bin/pip install --upgrade pip

# use BuildKit cache mount to drastically reduce redownloading from pip on repeated builds
RUN --mount=type=cache,target=/root/.cache /py/bin/pip install --timeout 100 -r requirements_frozen.txt

COPY . ./app
COPY ./scripts /scripts

WORKDIR /app
RUN mkdir -p /app/temp
RUN mkdir -p /home/app

EXPOSE 8000

RUN mkdir -p /vol/web/static && \
    mkdir -p /vol/web/media

RUN DEBIAN_FRONTEND=noninteractive adduser --disabled-password --no-create-home  --gecos "" app  && \
    chown -R app:app /vol && \
    chmod -R 777 /py && \
    chmod -R 777 /home/app && \
    chown -R app /app && \
    chown -R app:app /py/ && \
    chmod -R 755 /vol && \
    chmod -R +x /scripts
    

ENV PATH="/scripts:/py/bin:$PATH"

CMD ["run.sh"]

