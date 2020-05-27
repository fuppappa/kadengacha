FROM amazonlinux:2

ARG application_dir = /web_application/morison_server

COPY ../application_server $application_dir

WORKDIR $project_dir
RUN pip install -r requirements.txt