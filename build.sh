#!/bin/sh
eval $(minikube docker-env)
docker build server -t blog
docker build model -t model
kubectl apply -f infra