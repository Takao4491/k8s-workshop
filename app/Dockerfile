# Multi-stage build pour une image finale légère
# Étape 1: Environnement de build
FROM python:3.11-slim as builder

# Définition du répertoire de travail dans le conteneur
WORKDIR /app

# Création d'un fichier requirements.txt minimal pour le POC
RUN echo "Flask" > requirements.txt \
    && echo "gunicorn" >> requirements.txt

# Installation des dépendances
RUN pip install --no-cache-dir -r requirements.txt

# Étape 2: Environnement d'exécution (final)
FROM python:3.11-slim

# Configuration de l'utilisateur non-root (meilleure pratique de sécurité)
RUN adduser --disabled-password --gecos '' appuser
USER appuser
WORKDIR /app

# Copie des dépendances installées depuis l'étape de build
COPY --from=builder /usr/local/lib/python3.11/site-packages /usr/local/lib/python3.11/site-packages

# Copie du code de l'application
COPY app/api.py .

# Définition du port d'écoute
EXPOSE 5000

# Commande de lancement en utilisant Gunicorn pour la production
# On expose le port 5000, le Healthcheck est géré par l'endpoint /health
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "api:app"]
