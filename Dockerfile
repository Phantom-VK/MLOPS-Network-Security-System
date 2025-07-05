FROM python:3.13-bookworm

WORKDIR /app

# Copy only requirements first (helps Docker cache better)
COPY requirements.txt .

RUN apt update -y && apt install awscli -y
RUN pip install --upgrade pip && pip install -r requirements.txt

# Now copy the rest of the code
COPY . .

CMD ["python3.13", "app.py"]
