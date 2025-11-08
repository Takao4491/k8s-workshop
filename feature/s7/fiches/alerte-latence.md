# 🔔 Alerte : Latence élevée sur l'API

## 📌 Déclencheur
L’alerte `HighLatency` se déclenche lorsque la latence moyenne dépasse **0.5 seconde** pendant plus d’**1 minute**.

## 📊 Cause probable
- Saturation du backend ou de la base de données
- Boucle lente ou traitement bloquant dans le code
- Charge réseau ou contention CPU

## 🔥 Impact
- Dégradation de l’expérience utilisateur
- Risque de timeout côté client
- Augmentation du taux d’abandon

## 🛠️ Remédiation
- Identifier les endpoints lents via les logs ou Grafana
- Optimiser les requêtes ou les traitements
- Mettre en cache les réponses fréquentes
- Scaler horizontalement si nécessaire
