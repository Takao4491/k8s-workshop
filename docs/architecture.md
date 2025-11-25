🏢 Architecture du Microservice MCE-Utility

Le projet MCE-Utility est une architecture mono-microservice simple, conçue pour être facilement répliquée et mise à l'échelle sur Kubernetes.

---

1. Vue d'ensemble

Le service est une API RESTful basée sur Python/Flask et conteneurisée avec Docker. Il est déployé sur un cluster Kubernetes, où il est géré par un Deployment et exposé via un Service.

---

2. Composants Clés


2.1. Microservice API (Cœur Fonctionnel)

- Technologie : Flask (Python)

- Rôle : Exécute la logique métier de calcul des coûts d'enchantement et de validation des recettes de crafting.

- Runtime : Gunicorn est utilisé comme serveur d'application WSGI pour garantir la stabilité et la gestion de la concurrence en environnement de production.


2.2. Conteneurisation (Dockerfile)

Le Dockerfile utilise la stratégie du multi-stage build pour créer une image finale très légère, incluant uniquement le runtime Python et l'application. Cette approche renforce la sécurité et réduit les temps de déploiement. L'exécution se fait sous un utilisateur non-root.


2.3. Orchestration (Kubernetes)
Le déploiement est géré par des objets Kubernetes :

- Deployment : Assure le maintien du nombre de répliques souhaité et gère les mises à jour progressives.

- Service : Fournit un point d'entrée stable à l'API à l'intérieur et à l'extérieur du cluster.

- Healthchecks : Les endpoints /health de l'API sont utilisés par les sondes Liveness et Readiness de Kubernetes pour garantir la disponibilité du service.

---

3. Flux de Données

- Requête Externe : Un utilisateur ou une application cliente envoie une requête HTTP (POST) au Service Kubernetes.

- Service (Load Balancing) : Le Service transfère la requête à l'un des Pods disponibles.

- Pod / API : Le conteneur Flask/Gunicorn traite la requête et renvoie la réponse (coût d'enchantement ou validation de recette).
