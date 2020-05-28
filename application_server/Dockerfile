FROM amazonlinux:2

RUN amazon-linux-extras install python3
RUN yum install -y gcc python3-devel

RUN mkdir /var/www

WORKDIR /var/www

COPY requirements.txt /tmp/
CMD ["ls", "/var/www"]
CMD ["ls", "/tmp"]

RUN pip3 install --upgrade pip
RUN pip install --no-cache-dir -r /tmp/requirements.txt

CMD ["ls", "/var/www"]
CMD ["uwsgi","--ini","/var/www/uwsgi.ini"]