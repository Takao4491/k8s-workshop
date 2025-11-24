# Étape de build
FROM python:3.11-slim AS builder
WORKDIR /app
COPY app.py .
RUN pip install flask gunicorn

# Étape runtime
FROM python:3.11-slim
WORKDIR /app
COPY --from=builder /app /app
COPY --from=builder /usr/local/lib/python3.11/site-packages /usr/local/lib/python3.11/site-packages

# Utilisateur non-root
RUN useradd -m datapress
USER datapress

EXPOSE 5000

# Ajout du serveur Gunicorn
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "app:app"]

# Healthcheck Docker
HEALTHCHECK CMD curl --fail http://localhost:5000/health || exit 1
