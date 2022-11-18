FROM python:3.10

COPY app.py ./app.py
COPY views.py ./views.py
COPY koch_snowflake.py ./koch_snowflake.py
COPY requirements.txt ./requirements.txt
COPY static/ ./static
COPY templates/ ./templates

RUN pip install -r requirements.txt

CMD ["python", "app.py"]