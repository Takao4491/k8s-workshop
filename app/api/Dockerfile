# Étape de build
FROM python:3.11-slim AS builder
WORKDIR /app
COPY app.py .
RUN pip install flask

# Étape runtime
FROM python:3.11-slim
WORKDIR /app
COPY --from=builder /app /app
COPY --from=builder /usr/local/lib/python3.11/site-packages /usr/local/lib/python3.11/site-packages

# Utilisateur non-root
RUN useradd -m datapress
USER datapress

EXPOSE 5000
CMD ["python", "app.py"]
