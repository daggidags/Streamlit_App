
FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install

COPY . .

EXPOSE 8501

CMD ["streamlit","run","app.py"]

