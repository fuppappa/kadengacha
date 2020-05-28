FROM amazonlinux:2

RUN yum -y update

RUN amazon-linux-extras install nginx1.12


ENTRYPOINT ["/usr/sbin/nginx", "-g", "daemon off;", "-c", "/etc/nginx/nginx.conf"]

