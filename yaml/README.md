# Mooing it up on Kubernetes
```bash
# Be sure to edit the hostname in cowsay-ingress.yml to match a resolvable host

kubectl create -f cowsay-svc.yml -f cowsay-ingress.yml -f cowsay-deployment.yml
```

