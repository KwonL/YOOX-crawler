FROM python:3.8
LABEL maintainer "lkh116@snu.ac.kr"

WORKDIR /root
ADD requirements/prod.txt .
RUN pip install -r prod.txt

ADD . .

CMD [ "scrapy", "crawl", "yoox" ]