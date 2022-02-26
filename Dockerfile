FROM ubuntu:20.04
ENV DEBIAN_FRONTEND=noninteractive

WORKDIR /

RUN apt -y update && apt -y install make build-essential python-setuptools python3-pip npm

COPY backend/requirements.txt requirements.txt
RUN python3 -m pip install -r requirements.txt

COPY . .

EXPOSE 80

CMD ["make", "setup_production", "run_production"]
