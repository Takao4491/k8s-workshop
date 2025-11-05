############################################################
# TP Kubernetes - PostgreSQL StatefulSet (S5)
############################################################

Objectif
--------
Déployer une base PostgreSQL dans Kubernetes avec StatefulSet,
volume persistant, secret et configmap. Vérifier la persistance
des données après redémarrage du pod.

Structure du dossier
--------------------
manifests/
├── configmap.yaml
├── postgres-pvc.yaml
├── postgres-service.yaml
├── postgres-statefulset.yaml
├── secret.yaml              # Ignoré par Git (.gitignore)
└── secret-example.yaml      # Modèle public

Déploiement
-----------
```bash
# Créer le namespace si nécessaire
kubectl create namespace workshop-s5

# Appliquer les fichiers
kubectl apply -f manifests/configmap.yaml
kubectl apply -f manifests/secret.yaml          # ou secret-example.yaml
kubectl apply -f manifests/postgres-pvc.yaml
kubectl apply -f manifests/postgres-service.yaml
kubectl apply -f manifests/postgres-statefulset.yaml
```

À propos du secret
------------------
Le fichier `secret.yaml` contient le mot de passe PostgreSQL.
Il est ignoré par Git pour éviter d'exposer des données sensibles.

Utiliser `secret-example.yaml` comme modèle :
```yaml
stringData:
  POSTGRES_PASSWORD: example
```

Remplacer `"example"` par votre mot de passe réel dans `secret.yaml`.

Tests
-----
```bash
# Connexion à PostgreSQL
kubectl exec -it postgres-0 -n workshop-s5 -- psql -U postgres -d workshop
```

```sql
-- Création de table et insertion
CREATE TABLE test_table (
  id SERIAL PRIMARY KEY,
  name TEXT NOT NULL
);

INSERT INTO test_table (name) VALUES ('Lucas');
SELECT * FROM test_table;
```

```bash
# Test de persistance
kubectl delete pod postgres-0 -n workshop-s5
kubectl get pods -n workshop-s5 -w

# Reconnexion et vérification
kubectl exec -it postgres-0 -n workshop-s5 -- psql -U postgres -d workshop
```

```sql
SELECT * FROM test_table;
```

Résultat attendu
----------------
- Le pod redémarre automatiquement
- La base PostgreSQL reste accessible
- Les données insérées avant le redémarrage sont conservées

Captures
--------
Voir le dossier `captures/` pour les preuves de fonctionnement :
- `connexion.txt` : accès à PostgreSQL
- `insertion.txt` : création et lecture de données
- `persistance.txt` : données conservées après redémarrage

Conclusion
----------
TP validé si les données sont toujours présentes après redémarrage.