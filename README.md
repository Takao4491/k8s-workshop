DataPress – POC Final
======================

Objectif
--------
Ce projet a pour objectif de développer un Proof of Concept (POC) pour la plateforme DataPress. 
Il s'agit de démontrer la faisabilité technique d'une architecture microservices simple, composée 
d'une API et d'une interface frontale, orchestrées via Docker et prêtes à être déployées sur Kubernetes.

Contexte client
---------------
DataPress est une PME éditrice de tableaux de bord pour les équipes marketing. 
Sa plateforme actuelle est monolithique, hébergée sur un seul serveur, et présente plusieurs limites :
- indisponibilité totale en cas de panne,
- difficulté de montée en charge,
- déploiements risqués,
- documentation dispersée.

Le DSI souhaite amorcer une modernisation via Docker, Kubernetes et CI/CD, en commençant par un POC isolé.

Arborescence du projet
----------------------
tp-final

├── app

│   ├── api

│   │   ├── app.py

│   │   └── Dockerfile

│   └── front

│       ├── Dockerfile

│       └── index.html

├── docker

│   └── docker-compose.yml

├── docs

│   ├── architecture.md

│   ├── decisions.md

│   └── exploitation.md

├── k8s

│   ├── api-deployment.yaml

│   ├── api-service.yaml

│   ├── configmap.yaml

│   ├── front-deployment.yaml

│   ├── front-service.yaml

│   └── secret.yaml

└── README.md


Instructions de lancement
-------------------------
1. Cloner le dépôt :
   git clone https://github.com/Takao4491/k8s-workshop.git
   cd tp-final

2. Lancer les services avec Docker Compose :
   docker compose -f docker/docker-compose.yml up --build

3. Accéder à l'application :
   - Frontend : http://localhost:80
   - API : http://localhost:5000

Technologies utilisées
----------------------
- Python 3.11
- Flask
- HTML5 / NGINX
- Docker & Docker Compose
- Kubernetes (manifests YAML)
- GitHub Actions (CI)

Documentation
-------------
La documentation technique est disponible dans le dossier `docs/` :
- architecture.md : description de l'architecture technique
- decisions.md : choix techniques et justifications
- exploitation.md : instructions de déploiement et d'exploitation

Présentation client
-------------------
Une présentation synthétique est disponible dans `docs/` au format PDF. 
Elle résume le contexte, l’architecture proposée, la sécurité, le CI/CD et les recommandations.

Lien vers le dépôt Git
-----------------------
https://github.com/Takao4491/k8s-workshop/tree/feature/final

État du projet
--------------

✅ Structure du projet en place

✅ API Flask minimale opérationnelle

✅ Frontend statique avec NGINX

✅ Intégration Docker Compose

✅ Manifests Kubernetes prêts

✅ Documentation technique complète

✅ Présentation client intégrée
