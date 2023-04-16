FROM python:3.9

RUN groupadd -r user && useradd -r -g user user

ENV PYTHONUNBUFFERED=1
ENV DATABASE_URL="postgresql+psycopg2://postgres:postgres@emails.cjgydgtvqate.us-east-1.rds.amazonaws.com/emails"

EXPOSE 3000

WORKDIR /blacklist_microservice

ADD requirements.txt ./

RUN pip install -r requirements.txt

COPY . .

RUN chown -R user:user .
RUN ["chmod", "+x", "run_service.sh"]

CMD ["/bin/bash", "./run_service.sh"]

USER user
