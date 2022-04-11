FROM python:3.7.5

# install heroku cli
RUN curl https://cli-assets.heroku.com/install.sh | sh


# change dir
WORKDIR /home/heroku-ase-db

# upgrade pip
RUN apt-get update && apt-get install -y \
    && pip install --upgrade pip

# install module
COPY requirements.txt /home
RUN pip install -r /home/requirements.txt