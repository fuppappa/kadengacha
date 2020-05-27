FROM amazonlinux:2

RUN amazon-linux-extras install python3
RUN yum install -y gcc python3-devel

RUN mkdir /var/www
ARG application_dir = /var/www

COPY ../application_server $application_dir

WORKDIR $application_dir
RUN pip install --no-cache-dir -r requirements.txt

CMD ["uwsgi","--ini","/var/www/uwsgi.ini"]