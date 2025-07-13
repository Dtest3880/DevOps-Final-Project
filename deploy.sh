#!/bin/bash
echo "Starting Deployment to Minikube..."

kubectl apply -f Phase2/deployment.yaml
kubectl apply -f Phase2/service.yaml

echo "Deployment finished!"
