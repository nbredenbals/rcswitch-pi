FROM arm64v8/debian:latest
WORKDIR /tmp/rcswitch

EXPOSE 5000

# Install the application dependencies
RUN mkdir -p /tmp/rcswitch
COPY * /tmp/rcswitch/
RUN apt-get update
RUN apt-get install -y wget python3 python3-flask
RUN wget https://github.com/WiringPi/WiringPi/releases/download/3.16/wiringpi_3.16_arm64.deb
RUN dpkg -i wiringpi_3.16_arm64.deb

CMD ["/bin/sh", "-c", "/usr/bin/python3 /tmp/rcswitch/webserver.py"]