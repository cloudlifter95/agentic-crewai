FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt
# ENV OPENAI_API_KEY=value
COPY . .

# CMD ["ls, -alR"]
CMD ["python", "main.py"]
