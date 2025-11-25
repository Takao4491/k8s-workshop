# MCE-Utility : Minecraft Enchantment Utility

## 🎯 Objectif du Projet (Fil Rouge)

Mettre en œuvre une architecture conteneurisée et orchestrée par Kubernetes pour un service utilitaire dédié à la communauté Minecraft Java.

**MCE-Utility** est un microservice API simple permettant aux joueurs de vérifier les coûts d'enchantement et de rechercher des recettes de *crafting* complexes, offrant un outil centralisé et fiable pour l'optimisation des ressources sur un serveur privé.

## 🛠️ Technologies Clés

| Catégorie | Technologie | Rôle | 
| ----- | ----- | ----- | 
| **Backend** | Python 3.11, Flask | Microservice API léger pour la logique métier. | 
| **Conteneurisation** | Docker | Packaging de l'API pour un environnement standardisé. | 
| **Orchestration** | Kubernetes | Déploiement, scaling et haute disponibilité du service. | 
| **Outils** | `docker-compose` | Environnement de développement et de test local. | 

## 📁 Structure du Projet

├── app/
│     ├── api.py # Microservice Flask 
│     └── Dockerfile # Configuration du conteneur API 
├── docs/ 
│     ├── architecture.md # Vue d'ensemble de l'architecture 
│     └── exploitation.md # Guide de lancement et commandes 
├── k8s/ 
│     ├── api-deployment.yaml # Déploiement K8s (Pods) 
│     └── api-service.yaml # Exposition réseau K8s (Service) 
├── .gitignore 
└── README.md


## 🚀 Lancement Rapide (Local)

Pour démarrer l'API et la tester avec Docker Compose :

1. Construire l'image : `docker-compose build`

2. Lancer le service : `docker-compose up -d`

3. Vérifier le statut : `curl http://localhost:5000/health` (doit retourner "OK")

Pour le déploiement Kubernetes, référez-vous au guide dans `docs/exploitation.md`.
