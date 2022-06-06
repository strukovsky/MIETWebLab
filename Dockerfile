FROM python:3.9
WORKDIR /project
COPY api ./api
COPY main ./main
COPY app ./app
COPY static ./static
COPY manage.py ./manage.py
COPY requirements.txt ./requirements.txt
COPY run.sh ./run.sh
RUN pip install django
RUN pip install psycopg2==2.9.3
RUN pip install django-cors-headers
RUN pip install gunicorn
RUN chmod 700 ./run.sh
CMD /bin/sh ./run.sh