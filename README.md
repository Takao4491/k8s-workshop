## TP S4  Déploiement Nginx avec Service et Ingress

Ce projet déploie une application Nginx dans Kubernetes avec un service interne et un accès via Ingress.

### Ce qui est mis en place :
- Un déploiement s4-nginx avec 2 pods
- Un service s4-nginx de type ClusterIP
- Un Ingress s4-ingress qui route les requêtes HTTP vers le service
- Un Ingress Controller ingress-nginx actif
- Un accès fonctionnel via http://s4.local:8080

### Commandes utilisées et sorties :

```bash
kubectl get pods -n workshop -o wide
kubectl get svc -n workshop
kubectl get endpoints -n workshop
kubectl get ingress -n workshop
kubectl describe ingress s4-ingress -n workshop
kubectl get pods -n ingress-nginx -o wide
```


### Résultat :
- Les pods s4-nginx sont en Running
- Le service expose bien les pods sur le port 80
- Les endpoints sont visibles et corrects
- LIngress est configuré avec le host s4.local
- Le controller NGINX est actif et route les requêtes
- La page Nginx saffiche bien dans le navigateur

### Fichiers YAML inclus :
- s4-nginx-deployment.yaml
- s4-nginx-service.yaml
- s4-ingress.yaml

### Commandes de lancement et test

#### 📦 Appliquer les fichiers YAML

```bash
kubectl apply -f s4-nginx-deployment.yaml
kubectl apply -f s4-nginx-service.yaml
kubectl apply -f s4-ingress.yaml
```

#### 🔍 Vérifier les ressources déployées

```bash
kubectl get pods -n workshop
kubectl get svc -n workshop
kubectl get endpoints -n workshop
kubectl get ingress -n workshop
```

#### 🌐 Tester l’accès via port-forward

```bash
kubectl -n ingress-nginx port-forward svc/ingress-nginx-controller 8080:80
```

#### 🧪 Tester l’application dans le navigateur ou avec curl

```bash
curl -H "Host: s4.local" http://localhost:8080
```

### Diagramme de fonctionnement

```
Navigateur (http://s4.local:8080)
            |
         [Ingress]
            |
         [Service]
            |
     +-------------+
     |             |
 [Pod Nginx]   [Pod Nginx]
```