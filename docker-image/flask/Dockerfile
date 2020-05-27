FROM amazonlinux:2

RUN amazon-linux-extras install python3
RUN yum install -y gcc python3-devel

ARG application_dir = /web_application/morison_server

COPY ../application_server $application_dir

WORKDIR $project_dir
RUN pip install -r requirements.txt