# TP S6 — Scalabilité & Résilience

## 🎯 Objectifs

- Définir les ressources (CPU/mémoire) pour les workloads
- Mettre en place un HPA basé sur CPU et métrique personnalisée
- Gérer la résilience avec un PodDisruptionBudget
- Déployer un rollout canary (bonus)
- Définir des SLO/SLI et tester la charge avec k6

## ⚙️ Prérequis

- Cluster Kubernetes (kind, minikube, k3d…)
- Namespace `workshop` créé
- Prometheus Adapter installé pour les métriques personnalisées
- Argo Rollouts installé (si bonus activé)

## 🚀 Déploiement

```bash
kubectl apply -f manifests/deployment-api.yaml
kubectl apply -f manifests/hpa.yaml
kubectl apply -f manifests/pdb.yaml
kubectl apply -f manifests/rollout-canary.yaml   # bonus
```

## 📈 Test de charge avec K6

Un test de charge a été réalisé avec 50 requêtes par seconde pendant 5 minutes.  
L’API a maintenu une latence p95 de 25.94 ms et un taux d’erreur de 0.09%.

✅ Tous les SLO définis sont respectés.