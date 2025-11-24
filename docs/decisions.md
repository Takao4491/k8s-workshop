# Décisions techniques - POC DataPress

## API
- **Serveur WSGI Gunicorn** : nous avons choisi d’utiliser Gunicorn au lieu du serveur Flask natif.  
  Cela permet de respecter les standards de déploiement en production et d’assurer une meilleure gestion des processus.
- **Utilisateur non-root** : le conteneur API est exécuté avec un utilisateur dédié (`datapress`) afin de renforcer la sécurité et éviter les privilèges excessifs.
- **Healthcheck Docker** : un healthcheck est défini sur l’endpoint `/health`.  
  Cela permet à Docker ou Kubernetes de vérifier automatiquement l’état du service et de redémarrer en cas de défaillance.
- **Multi-stage build** : utilisation d’une étape de build séparée pour installer les dépendances, puis copie dans une image finale plus légère.

## Front
- **Image nginx:alpine** : choix d’une image légère et rapide pour servir le front statique.
- **Fichier statique index.html** : déployé directement dans `/usr/share/nginx/html` pour simplifier la mise en place.
- Possibilité d’ajouter une configuration NGINX personnalisée (proxy vers l’API), mais non nécessaire pour le POC.

## Docker Compose
- **Réseau interne dédié (`datapress-net`)** : permet au front et à l’API de communiquer directement par nom de service.
- **Ports exposés** : `5000` pour l’API et `80` pour le front, afin de tester facilement en local.
- **depends_on** : garantit que le front démarre après l’API.

## Bonnes pratiques
- Documentation centralisée dans `README.md` et `docs/`.
- Séparation claire des services (API, front, auth).
- Respect des standards DevOps : sécurité, monitoring, optimisation des images.
