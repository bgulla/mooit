# mooit


<pre>
  ___
< cows say the darnedest things >
  ---
         \   ^__^
          \  (oo)\_______
             (__)\       )\/\
                 ||----w |
                 ||     ||
                 </pre>


Mooit - everyone loves `cowsay` so I decided to throw it in a Flask Docker container. This repo is used as a canary test when setting up 
new k8s clusters but runs fine using a local python interpreter as well.



## Deploying to Kubernetes
### Installing with Helm
Included in this repo is a baseline `helm` chart. You must have [helm](https://helm.sh/docs/using_helm/) installed.
```bash
git clone https://github.com/bgulla/mooit .
helm install --name mooit mooit  --debug
```

### YAML
```yaml
apiVersion: extensions/v1beta1
kind: Deployment
metadata:
  labels:
    app: mooit
  name: mooit-yaml
spec:
  replicas: 1
  template:
    metadata:
      labels:
        app: mooit
    spec:
      containers:
      - image: bgulla/mooit
        name: mooit
#        ports:
#        - containerPort: 80
apiVersion: extensions/v1beta1
kind: Ingress
metadata:
  name: mooit-svc
spec:
  rules:
  - host: mooit.example.com  #Hostname resolution. Make sure DNS is configured.
    http:
      paths:
      - backend:
          serviceName: mooit-svc
          servicePort: 80
        path: /
apiVersion: v1
kind: Service
metadata:
  labels:
    app: mooit
  name: mooit-svc
spec:
  ports:
  - name: "80"
    port: 80         # the port the service will expose at the edge
    targetPort: 8080    # container portt tthat tthe service will forward to
  selector:
    app: mooit
status:
  loadBalancer: {}
```

## Deploying locally with Docker
```bash
docker run --rm -t \
    -p 5000:5000 \
    bgulla/mooit
```

## Running locally with `Python`
```bash
virtualenv venv
venv/pip install -r src/requirements.txt
venv/python src/app.py
```

## OpenShift support
In order to use this image on OpenShift 3.x, add the `USER` and `LOGNAME` environment variables.
