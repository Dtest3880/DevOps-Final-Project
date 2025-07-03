A. Download and config Minikube.exe

B. Run minikube version command
C. Ensure version is shown correctly:

C:\Users\Razgi>minikube version
minikube version: v1.35.0
commit: dd5d320e41b5451cdf3c01891bc4e13d189586ed-dirty

D. Set up a Kubernetes cluster using Minikube -
Run minikube start command

Expected Result:

Done! kubectl is now configured to use "minikube" cluster and "default" namespace by default

E. Verify Cluster created via: kubectl get nodes command.

Expected Result:
C:\Users\Razgi>kubectl get nodes
NAME       STATUS   ROLES           AGE   VERSION
minikube   Ready    control-plane   44s   v1.32.0

F. Create deployment.yaml file

Set replicas: 2

Ensure selector is set for pods

Under template -> spec -> containers -> image: davetool1234/final_project:v0.1

Under ports field, set:
- containerPort: 5000

G. Create service.yaml file

Ensure selector matches the pods defined in the deployment

Set metadata: app: flask-app

Set port: 80 (External port)

Set targetPort: 5000 (Internal app port)

Set type: LoadBalancer

H. Create hpa.yaml file (Horizontal Pod Autoscaler)

Set minReplicas: 3

Set maxReplicas: 5

Under metrics -> resource -> target -> averageUtilization: 50

I. Apply deployment.yaml:
kubectl apply -f deployment.yaml
Verify pods created via:
kubectl get pods

J. Apply service.yaml:
kubectl apply -f service.yaml

K. Verify services:
kubectl get services
Ensure the service "flask-app-service" is listed and has External IP and CLUSTER-IP

L. Access the web application via:
minikube service flask-app-service
OR:
http://127.0.0.1:65382/

Verify the "Hello World" message is shown.

M. Pull the Docker image manually if needed:
docker pull davetool1234/final_project

N. Create configmap.yaml file:

Define key-value pairs for environment variables such as:

DB_HOST=localhost

DB_PORT=5432

Reference the ConfigMap in the deployment file under envFrom -> configMapRef

O. Create secret.yaml file:

Define base64-encoded sensitive values, for example:

DATABASE_PASSWORD

API_SECRET

Reference the Secret in the deployment file under envFrom -> secretRef

P. Create cronjob.yaml file:

Set schedule: "* * * * *" (every minute)

Define job template that runs a container with:

The same image: davetool1234/final_project:v0.1

Access to ConfigMap and Secret (same as deployment)

Container that prints time and values from config/secret every 10 seconds for 1 minute

Verify jobs created every minute:
kubectl get jobs

Check pod logs for the job to ensure correct output:
kubectl logs 

Q. Verify CronJobs are running properly:

kubectl get cronjob

Ensure the ACTIVE column shows activity

Verify COMPLETED jobs under:
kubectl get jobs

Use selector to get the pod for a specific job:
kubectl get pods --selector=job-name=