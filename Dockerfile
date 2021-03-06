FROM python:2.7-slim-jessie

RUN apt-get update && apt-get install -y libsodium-dev git libevent-dev libzmq-dev libffi-dev libssl-dev gcc file
WORKDIR /opt/bridge
COPY . /opt/bridge
RUN pip install --upgrade pip && pip install -r requirements-dev.txt
RUN pip install -e .
RUN apt-get clean

ENV TZ=Europe/Kiev
ENV LANG="en_US.UTF-8"
ENV LC_ALL="en_US.UTF-8"
ENV LC_LANG="en_US.UTF-8"
ENV PYTHONIOENCODING="UTF-8"
ENV PYTHONPATH="/opt/bridge/:${PYTHONPATH}"

CMD ["/usr/local/bin/databridge", "/etc/databridge.yaml"]
