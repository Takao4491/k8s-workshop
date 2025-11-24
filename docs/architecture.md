# Architecture - POC DataPress

## Vue d’ensemble
Le POC DataPress est composé de plusieurs services conteneurisés et orchestrés via Docker Compose.  
Chaque service est isolé mais communique au sein d’un réseau interne (`datapress-net`).

## Composants principaux
- **API (Flask + Gunicorn)**  
  - Fournit les endpoints `/` et `/health`.  
  - Exposé sur le port `5000`.  
  - Conteneur sécurisé avec utilisateur non-root.  
  - Healthcheck intégré pour supervision.

- **Front (NGINX)**  
  - Sert le fichier statique `index.html`.  
  - Exposé sur le port `80`.  
  - Peut être configuré pour proxy vers l’API.

- **Auth (Flask)** *(optionnel selon ton TP)*  
  - Service d’authentification basique.  
  - Exposé sur le port `5001`.

## Communication
- Les services partagent le réseau interne `datapress-net`.  
- Le front peut appeler l’API via `http://api:5000`.  
- Les conteneurs sont isolés mais interconnectés par nom de service.

## Schéma simplifié

```
          +----------------+
          |   Front (NGINX)|----> http://localhost:80
          +----------------+
                  |
                  v
          +----------------+
          | API (Flask)    |----> http://localhost:5000
          +----------------+
                  |
                  v
          +----------------+
          | Auth (Flask)   |----> http://localhost:5001
          +----------------+
```

## Déploiement
- **Local** : via `docker-compose up --build`.  
- **Production** : peut être étendu avec Kubernetes (`k8s/` manifests).  
- **Monitoring** : healthcheck sur l’API, logs accessibles via `docker-compose logs`.

