FROM  mcr.microsoft.com/devcontainers/python:3.10-bookworm

ENV PYTHONUNBUFFERED 1

COPY requirements.txt /tmp/pip-tmp/

RUN pip3 --disable-pip-version-check --no-cache-dir install -r /tmp/pip-tmp/requirements.txt \
    && rm -rf /tmp/pip-tmp

RUN wget -P /tmp/exercism-tmp/ https://github.com/exercism/cli/releases/download/v3.2.0/exercism-3.2.0-linux-arm64.tar.gz \
    && tar -xf /tmp/exercism-tmp/exercism*.tar.gz -C /tmp/exercism-tmp/ \
    && cp /tmp/exercism-tmp/exercism /usr/local/bin \
    && rm -rf /tmp/exercism-tmp
