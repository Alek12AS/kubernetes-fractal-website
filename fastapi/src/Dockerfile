FROM python:3.10

COPY api.py ./api.py
COPY koch_snowflake.py ./koch_snowflake.py
COPY requirements.txt ./requirements.txt

RUN pip install -r requirements.txt

CMD ["uvicorn", "api:app", "--host", "0.0.0.0", "--port", "80"]