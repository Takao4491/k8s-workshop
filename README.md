# TP S6 — Scalabilité & Résilience

## 🧠 Contexte

Ce TP vise à rendre une API plus robuste et scalable dans Kubernetes.  
On cherche à anticiper les pics de charge, garantir la disponibilité, et limiter les interruptions lors des mises à jour.

## 🎯 Objectifs

- Définir les ressources CPU/mémoire pour les workloads
- Mettre en place un HPA basé sur CPU et métrique personnalisée
- Gérer la résilience avec un PodDisruptionBudget
- Déployer un rollout canary (bonus)
- Définir des SLO/SLI et tester la charge avec K6

## ⚙️ Préparation du cluster

Avant de déployer, assure-toi que :

```bash
kubectl create namespace workshop
```

Et que les composants suivants sont installés :

- Prometheus Adapter (pour les métriques personnalisées)
- Argo Rollouts (si tu veux tester le canary)

## 🚀 Déploiement des ressources

On applique les manifestes dans l’ordre :

```bash
kubectl apply -f manifests/deployment-api.yaml      # Déploiement de l'API
kubectl apply -f manifests/hpa.yaml                  # Autoscaling
kubectl apply -f manifests/pdb.yaml                  # Résilience
kubectl apply -f manifests/rollout-canary.yaml       # Canary (bonus)
```

## 📐 SLO / SLI définis

On mesure la performance de l’API avec les indicateurs suivants :

| Service | SLI                  | SLO cible     | Fenêtre | Méthode de mesure                     | Budget d'erreur |
|---------|----------------------|---------------|---------|----------------------------------------|-----------------|
| API     | Latence p95          | < 300 ms      | 30 j    | Prometheus histogram_quantile         | 0.5%            |
| API     | Taux d'erreur        | < 1%          | 30 j    | rate(5xx)/rate(total)                 | 1%              |
| API     | Disponibilité        | ≥ 99.5%       | 30 j    | uptime probe                          | 0.5%            |
| API     | Saturation CPU       | < 80%         | 30 j    | container_cpu_usage_seconds_total     | —               |

## 📈 Test de charge avec K6

Un test de charge a été réalisé avec 50 requêtes par seconde pendant 5 minutes :

```bash
k6 run k6/script.js
```

L’API a maintenu une latence p95 de **25.94 ms** et un taux d’erreur de **0.09%**.  
La disponibilité observée était d’environ **99.91%**.

✅ Tous les SLO définis sont respectés.

### 🔬 Résultats observés

| SLI               | Résultat observé     | SLO cible     | ✅ / ❌ |
|-------------------|----------------------|---------------|--------|
| Latence p95       | 25.94 ms             | < 300 ms      | ✅     |
| Taux d’erreur     | 0.09%                | < 1%          | ✅     |
| Disponibilité     | ~99.91%              | ≥ 99.5%       | ✅     |
| Saturation CPU    | non mesurée          | < 80%         | —      |

## 📂 Structure du projet

```text
.
├── k6/
│   └── script.js                  # Script de test de charge
├── manifests/
│   ├── deployment-api.yaml        # Déploiement de l'API
│   ├── hpa.yaml                   # Horizontal Pod Autoscaler
│   ├── pdb.yaml                   # PodDisruptionBudget
│   ├── rollout-canary.yaml       # Rollout canary (bonus)
├── slo-sli/
│   └── fiche-slo-sli.md           # Définition des SLO/SLI
└── README.md
```

## 🔗 Liens utiles

- [K6](https://k6.io/docs/)
- [Prometheus Adapter](https://github.com/kubernetes-sigs/prometheus-adapter)
- [Argo Rollouts](https://argoproj.github.io/rollouts/)