FROM python:3.9

RUN groupadd -r user && useradd -r -g user user

# Environment Variables
ENV PYTHONUNBUFFERED=1
ENV DATABASE_URL="postgresql+psycopg2://postgres:postgres@emails.cjgydgtvqate.us-east-1.rds.amazonaws.com/emails"
ENV NEW_RELIC_APP_NAME="blacklists"
ENV NEW_RELIC_LOG=stdout
ENV NEW_RELIC_DISTRIBUTED_TRACING_ENABLED=true
ENV NEW_RELIC_LICENSE_KEY=95b18ad6c435f33edb5ef919fb370236FFFFNRAL
ENV NEW_RELIC_LOG_LEVEL=info

EXPOSE 3000

WORKDIR /blacklist_microservice

ADD requirements.txt ./

RUN pip install -r requirements.txt

COPY . .

RUN chown -R user:user .
RUN ["chmod", "+x", "run_service.sh"]

CMD ["/bin/bash", "./run_service.sh"]

ENTRYPOINT ["newrelic-admin", "run-program"]

USER user
