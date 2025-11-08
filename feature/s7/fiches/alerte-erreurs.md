# 🔔 Alerte : Taux d’erreur élevé sur l'API

## 📌 Déclencheur
L’alerte `HighErrorRate` se déclenche lorsque plus de **5% des requêtes** échouent (code 500) pendant plus de **2 minutes**.

## 📊 Cause probable
- Exception non gérée dans le code
- Service tiers indisponible
- Mauvaise validation des entrées

## 🔥 Impact
- Perte de données ou d’intégrité métier
- Frustration utilisateur
- Dégradation de la réputation du service

## 🛠️ Remédiation
- Analyser les logs d’erreur
- Ajouter des try/catch et des validations
- Mettre en place des retries ou des fallbacks
- Monitorer les dépendances externes
