# TP S7 — Supervision d'une API avec Prometheus & Grafana

## Objectif

Mettre en place une stack de supervision pour une API Flask instrumentée avec Prometheus, et visualiser les métriques dans Grafana.

## Environnement de travail

Le projet a été développé et testé dans une machine virtuelle Linux (Ubuntu Desktop), avec interface graphique.  
Cette VM permet de simuler un environnement de supervision isolé tout en offrant un confort d’utilisation pour les outils visuels comme Grafana.  
Les services (API Flask, Prometheus, Grafana) sont orchestrés via `docker-compose`, ce qui facilite le déploiement et l’isolation des composants.  
L’édition du code s’est faite via un éditeur local (VS Code), avec un dossier partagé entre l’hôte et la VM.  
La supervision et la configuration des dashboards ont été réalisées directement dans le navigateur de la VM, en accédant à l’interface web de Grafana.

## Structure du projet

feature/s7/
├── api/
│   ├── app.py
│   └── Dockerfile
├── docker-compose.yml
├── prometheus/
│   ├── prometheus.yml
│   └── alerts.yml
├── grafana/
│   └── dashboard.json
├── fiches/
│   ├── alerte-latence.md
│   └── alerte-erreurs.md
└── README.md

## Fonctionnement

L'API expose des métriques via `/metrics` au format Prometheus.  
Prometheus interroge cette endpoint à intervalle régulier (scraping).  
Les métriques sont stockées et visualisées dans Grafana via des panels personnalisés.  
Des règles d’alerte sont définies dans `alerts.yml` pour détecter les anomalies (latence, erreurs).  
Grafana permet d’importer un dashboard JSON pour visualiser les données en temps réel.

## Lancement

docker-compose build  
docker-compose up -d

## Accès aux services

| Service    | URL                        |
|------------|----------------------------|
| API        | http://localhost:8080      |
| Prometheus | http://localhost:9090      |
| Grafana    | http://localhost:3000      |

## Dashboard Grafana

Nom : TP S7 - API Observability  
Datasource : Prometheus (http://prometheus:9090)  
Panels inclus :
- Latence moyenne
- Taux d’erreur
- Requêtes par endpoint

## Alertes Prometheus

| Alerte        | Condition                          | Gravité   |
|---------------|------------------------------------|-----------|
| HighLatency   | Latence > 0.5s pendant 1 min       | warning   |
| HighErrorRate | > 5% d’erreurs pendant 2 min       | critical  |

Voir les fiches dans le dossier `fiches/` pour les détails et remédiations.

## Commandes utiles

Afficher les logs de l’API :  
docker-compose logs api

Redémarrer uniquement Prometheus :  
docker-compose restart prometheus

Accéder aux métriques brutes :  
curl http://localhost:8080/metrics

Simuler des erreurs :  
curl http://localhost:8080/error

Simuler de la latence :  
curl http://localhost:8080/slow

## Concepts abordés

- Instrumentation avec prometheus_client
- Histogrammes, compteurs, labels
- Scraping Prometheus
- Visualisation Grafana
- Alerting Prometheus

## Auteur

Lucas — TP réalisé dans le cadre du module S7 Observabilité & Monitoring
