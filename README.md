# Blog post classifier

## Prerequisites

1. [docker](https://docs.docker.com/engine/install/)

2. [kubectl](https://kubernetes.io/docs/tasks/tools/)

3. [minikube](https://minikube.sigs.k8s.io/docs/start/)

4. [helm](https://helm.sh/)

## Setup

### Start up the minikube cluster
```
minikube start
```

### Setup docker host as the cluster
```
eval $(minikube docker-env)
```

### Build the blog & model servers

```
docker build server -t blog
docker build model -t model
```

### Setup DB, metrics server and secrets
```
kubectl apply -f infra
```

### Configure host

Get the ip of the cluster
```
minikube ip
```
Edit `/etc/hosts` and add a line at the bottom. HostName can be anything you want.
```
<IP> <HostName>
```
Goto `infra/blog/values.yaml` and change ingress.hosts.host to <HostName>


### Install blog and model servers in the cluster
```
helm install blog ./infra/blog
helm install model ./infra/model
```

### Setup DB schema

Get the pod of the db by executing `kubectl get pods`and look for `blog-db-...`. Execute these commands to run the ddl script
```
kubectl cp ./server/ddl.sql <POD_NAME>:.
kubectl exec <POD_NAME> -- psql -U user -f ddl.sql
```

### Visit `<HostName>/docs` to get the swagger UI of the blog server