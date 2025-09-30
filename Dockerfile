FROM python:3.11-slim

WORKDIR /app

# System deps (psycopg needs libpq), and clean up apt lists
RUN apt-get update && apt-get install -y --no-install-recommends \
    libpq5 curl && rm -rf /var/lib/apt/lists/*

# Install deps (use psycopg v3)
COPY requirements/base.txt /app/requirements/base.txt
RUN pip install --no-cache-dir --upgrade pip \
 && pip install --no-cache-dir "psycopg[binary]==3.2.*" \
 && pip install --no-cache-dir -r requirements/base.txt

# Copy project
COPY . /app

EXPOSE 8000

# Default command (override in compose if needed)
CMD ["sh", "-c", "python src/manage.py migrate && python src/manage.py runserver 0.0.0.0:8000"]