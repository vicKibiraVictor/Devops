### Kubernetes
- Open source container orchestration tool.
- Helps you manage applications made up 100 or  1000 of containers in different environments(physical, virtual or even hybrid)

### Features of Kubernetes

- High availability or no downtime
- Scalability or high performance
- Disaster recovery - backup and restore

### Kubernetes components
- Node(worker node):Physical server or virtual machine.
- Pod: - Smallest unit OF K8S.
  Abstraction over container.
  Usually 1 application per pod.
  They are ephemeral.
  
- Service - Permanent IP address.
            Loadbalancer

  External service - allows the     application to be outside 
- Ingress - A request get to ingress and then to the service
- ConfigMap - Contains configuration data,like db urls.
- Secret - Used to store credentials,which are base 64 encoded

- Volumes - Attaches a physical storage on a pod.
- Deployment - Blueprint of a pod.
- Stateful - Meant for databases.
             Very tidious.

### Kubernetes Architecture
- Worker nodes : Container runtime.
               Kubelet.
               Kube proxy.

- Master nodes: API Server(acts as a gatekeeper for the authentication).

- Scheduler - Looks at where to put the pod.

- Contoller Manager - Detects state changes like crashing of pods.

- ETCD - Is the cluster brain.Its a key value store for any change in the cluster.

### What is Minikube?
One node k8s cluster that runs on your local machine.
Allows you to test and work with kubernetes locally.
Runs master and worker nodes.

### Kubectl
This a commandline tool that enables you to interact with minikube.
Not for minikube alone,but also for any cluster.

### Minikube Installation
Follow the link to  download minikube for various os's

https://minikube.sigs.k8s.io/docs/start/?arch=%2Flinux%2Fx86-64%2Fstable%2Fbinary+download

On MacOS

```
brew update
brew install hyperkit
brew install minikube
kubectl
minikube
```

### Start a cluster
```
minikube start
minikube start --vm-driver=hyperkit
kubectl get nodes
minikube status
kubectl version
```

### Delete cluster and restart in debug mode
```
minikube delete
minikube start --vm-driver=hyperkit --v=7 --alsologtostderr
minikube status
```

### Kubectl commands
```
kubectl get nodes
kubectl get pod
kubectl get services
kubectl create deployment nginx-depl --image=nginx
kubectl get deployment
kubectl get replicaset
kubectl edit deployment nginx-depl
kubectl get deployment nginx-depl -o yaml > nginx-deply.yaml

```

### Debugging
```
kubectl logs {pod-name}
kubectl exec -it {pod-name} --/bin/bash
```
### create mongo deployment
```
kubectl create deployment mongo-depl --image=mongo
kubectl logs mongo-depl-{pod-name}
kubectl describe pod mongo-depl-{pod-name}
```
### Delete deployment
```
kubectl delete deployment mongo-depl
kubectl delete deployment nginx-depl
```

### Create or edit config file
```
nano nginx-deployment.yml
kubectl apply -f nginx-deployment.yaml
kubectl get pod
kubectl get deployment
```
### Delete with config
```
kubectl delete -f nginx-deployment.yaml
```

### To check metrics of the current cpu and memory usage for the clusters pods or nodes
```
kubectl top
```

###  Kubernetes Manifest Structure
A manifest is configuration file written in YAML that tells Kubernetes what you want to create,run or manage-such as deployments,services etc.

### Basic structure of any manifest
Every Kubernetes manifest file shows this general structure:
```
apiVersion: <API version>   # e.g., apps/v1 or v1
kind: <Resource type>       # e.g., Deployment, Pod
metadata:
  name: <Name of the resource>
  labels:                   # Optional but useful for selectors
    key: value
spec:
  # Configuration specific to the kind of resource

```
### Breakdown of each section
```
1. apiVersion
Specifies the Kubernetes API version to use for the object.

v1 — for core resources like Pod, Service, ConfigMap

apps/v1 — for higher-level resources like Deployment, StatefulSet

2. kind
Declares what type of object you're creating.

Examples include:

Pod

Deployment

Service

ConfigMap

Secret

Ingress

3. metadata
Provides identifying information about the resource.

name: (Required) Unique name within the namespace.

namespace: (Optional) Defaults to default if omitted.

labels & annotations: Used for grouping, selection, and extra metadata.

4. spec (Specification)
Defines the desired state of the object.
Its contents depend on the kind you're creating.
```
### Example: Deployment Manifest
```
apiVersion: apps/v1
kind: Deployment
metadata:
  name: nginx-depl
  labels:
    app: nginx
spec:
  replicas: 2
  selector:
    matchLabels:
      app: nginx
  template:
    metadata:
      labels:
        app: nginx
    spec:
      containers:
      - name: nginx
        image: nginx:latest
        ports:
        - containerPort: 80

```
### Highlights
- replicas: Number of Pod copies to run.

- selector: Matches Pods with label app: nginx.

- template: Describes the Pod to be created (like a Pod manifest inside the Deployment).

### Optional fields across manifests
- status: Set by Kubernetes after creation — do not include manually.

- resources: Define CPU and memory requests and limits.

- env: Set environment variables inside containers.

- volumeMounts and volumes: For attaching external or persistent storage.



### To access the mongo express 
```
minikube service mongo-express-service
kubectl port-forward service/mongo-express-service 8081:8081
```

### Namespaces
Namespaces in Kubernetes are like virtual clusters within a single physical cluster. They help you organize and manage resources in a multi-team or multi-project environment.

### Why Use Namespaces?
- Isolation: Separate environments (e.g., dev, test, prod) within one cluster.

- Resource Quotas: Limit CPU/memory usage per team or application.

- Name Conflicts: Avoid resource name collisions (e.g., multiple nginx services across teams).

- Access Control: Apply RBAC rules per namespace for fine-grained security.

### How to intall kubectx + kubens
```
sudo wget https://raw.githubusercontent.com/ahmetb/kubectx/master/kubens -O /usr/local/bin/kubens
sudo chmod +x /usr/local/bin/kubens

```
### Check all the namespaces
```
kubens
```
### Switch to a namespace
```
kubens namespace-name
```
### Ingress
Ingress is a Kubernetes object that manages external access to services in a cluster, typically HTTP/HTTPS traffic. Instead of exposing each service with a NodePort or LoadBalancer, you can use Ingress to route requests based on the URL or host.

### Why Use Ingress?
- Smart Routing: Route traffic to different services based on path (/api, /app) or host (app.example.com, api.example.com).

- TLS/HTTPS Support: Easily configure SSL with cert-manager or your own certificates.

- Centralized Entry Point: Acts as a gateway to your cluster's services.

### Types of Ingress Configurations
Kubernetes Ingress can be configured in various ways depending on how traffic should be routed to services. Here are the main types:
### 1. Single Service Ingress (Basic Routing)
Routes all HTTP requests to a single backend service.

```
rules:
- http:
    paths:
    - path: /
      pathType: Prefix
      backend:
        service:
          name: my-service
          port:
            number: 80

```
### 2. Path-Based Routing
Routes requests to different services based on URL paths.

```
rules:
- host: myapp.local
  http:
    paths:
    - path: /api
      pathType: Prefix
      backend:
        service:
          name: api-service
          port:
            number: 80
    - path: /app
      pathType: Prefix
      backend:
        service:
          name: frontend-service
          port:
            number: 80

```
### Host-Based Routing
Routes traffic based on domain name (host).
```
rules:
- host: api.example.com
  http:
    paths:
    - path: /
      pathType: Prefix
      backend:
        service:
          name: api-service
          port:
            number: 80
- host: app.example.com
  http:
    paths:
    - path: /
      pathType: Prefix
      backend:
        service:
          name: frontend-service
          port:
            number: 80

```
### Ingress with TLS (HTTPS)
Secure services using TLS (HTTPS) certificates.

```
tls:
- hosts:
  - myapp.local
  secretName: tls-secret  # must contain TLS cert and key

rules:
- host: myapp.local
  http:
    paths:
    - path: /
      pathType: Prefix
      backend:
        service:
          name: my-service
          port:
            number: 80

```
### Ingress with Rewrite and Redirect Annotations
Customize behavior with annotations like URL rewrites, redirects, or rate limiting (depends on Ingress Controller).

```
metadata:
  annotations:
    nginx.ingress.kubernetes.io/rewrite-target: /
    nginx.ingress.kubernetes.io/ssl-redirect: "true"

```
### Putting it all together in our project(demo project)
### Notes
- Host-based Routing: Routes requests from http://mongo-express.local to the mongo-express-service.

- Annotations:

- rewrite-target: / ensures that URLs like /dashboard are passed cleanly to the backend.

- PathType:

Prefix matches all requests under /.
### Enable ingress
```
 minikube addons enable ingress

```
###  Check Ingress Controller is Running
```
kubectl get pods -n ingress-nginx

```
### Get the minikube ip
```
minikube ip

```
###  Accessing the App via Ingress
To make mongo-express.local work:

1. Add it to your local /etc/hosts file:
```
sudo echo "127.0.0.1 mongo-express.local" | sudo tee -a /etc/hosts

```
If using Minikube, replace 127.0.0.1 with minikube ip.

2. Apply the Ingress:
```
kubectl apply -f mongo-express-ingress.yaml

```

3. Open in browser: http://mongo-express.local

###  Ports
- containerPort: Port the container listens on internally. 
- targetPort:  Port the Pod receives traffic on.
- port: Port exposed by the service.
- nodePort:  Port exposed on the Node IP (external access). 
- hostPort:  Exposes a container port directly on the host (less common, often avoided).

Used for communication between containers, services, and external clients.

### Storage Volumes
Kubernetes volumes allow data to persist beyond container restarts.

- EmptyDir: Temporary storage; data lost when the Pod is deleted.

- hostPath: Mounts a file/folder from the host into the Pod (not portable).

- PersistentVolume (PV) and PersistentVolumeClaim (PVC): Abstraction for durable storage (e.g., EBS, NFS, cloud disks).

Used for databases, caching, and sharing data between containers.

###  Health Checks
Kubernetes uses probes to monitor the health of containers:

- Liveness Probe: Checks if the container is alive. If it fails, Kubernetes restarts it.

- Readiness Probe: Checks if the container is ready to receive traffic. If not, it’s removed from the service endpoint.

- Startup Probe: Ensures the app has started before the other two probes kick in.

### Observability
Observability tools help monitor and troubleshoot Kubernetes apps.

Common components:

- Metrics: CPU, memory usage (metrics-server, Prometheus).

- Logs: Container logs (kubectl logs, EFK stack, Loki).

- Traces: Distributed tracing (Jaeger, OpenTelemetry).

- Dashboards: Visual monitoring tools like Grafana, Lens, K9s, Kubernetes Dashboard.


### RBAC (Role-Based Access Control)
RBAC restricts access to Kubernetes resources.

Key components:

- Role: Defines permissions within a namespace.

- ClusterRole: Same as Role but cluster-wide.

- RoleBinding: Grants a Role to a user/service account.

- ClusterRoleBinding: Grants a ClusterRole to a user/service account across the cluster.

### Kubernetes Jobs
Kubernetes Jobs are used to run one-off or batch tasks that run to completion.

### Use Cases
- Database migrations

- Data backups or restores

- Sending emails in bulk

- Cleanup scripts

- Scheduled data transformations

### Types of Jobs
### Standard Job
Runs a pod to completion a specific number of times.
```
apiVersion: batch/v1
kind: Job
metadata:
  name: hello-job
spec:
  template:
    spec:
      containers:
        - name: hello
          image: busybox
          command: ["echo", "Hello from Kubernetes Job"]
      restartPolicy: Never
```
### Parallel Jobs
Run multiple pods in parallel for the same task.
```
spec:
  completions: 5
  parallelism: 2
```
- completions: total successful pods needed

- parallelism: how many run at the same time

###  CronJobs
Scheduled jobs that run at specific times like a cron task.

```
apiVersion: batch/v1
kind: CronJob
metadata:
  name: db-backup
spec:
  schedule: "0 * * * *"  # every hour
  jobTemplate:
    spec:
      template:
        spec:
          containers:
            - name: backup
              image: my-backup-image
              args: ["backup.sh"]
          restartPolicy: OnFailure
```
###  Clean Up Completed Jobs
```
kubectl delete jobs --all
kubectl delete pod <pod-name>
```
or auto-cleanup using TTL (Time To Live):
```
spec:
  ttlSecondsAfterFinished: 100
```
### Bonus Tips
- Jobs are idempotent: they can be retried without negative side effects.

- Always set restartPolicy: Never or OnFailure for jobs.

- Monitor job success/failure with kubectl get jobs and kubectl describe job <job-name>.

### Helm
Helm simplifies deploying applications in Kubernetes by using charts — pre-configured templates for Kubernetes resources.

###  Why Use Helm?
- Manage complex Kubernetes apps as a single unit.

- Reuse and share configurations easily.

- Customize deployments with simple variables.

- Rollback updates if something breaks.

### Helm Concepts

- Chart:	A Helm package containing YAML templates, values, and metadata.
- Release:	A specific instance of a chart deployed in your cluster.
- Values:	Customizable configurations (like values.yaml) that override chart defaults.
- Templates:	Kubernetes manifest files written with Go templating.
- Repositories:	Hosts charts you can download and install.

### Helm folder structure
```
my-chart/
├── charts/              # Dependencies
├── templates/           # YAML templates for resources
│   ├── deployment.yaml
│   ├── service.yaml
│   └── _helpers.tpl
├── values.yaml          # Default values
├── Chart.yaml           # Chart metadata
└── README.md
```
### Common Helm Commands

- Install Helm chart:	helm install myapp ./my-chart
- Uninstall release:	helm uninstall myapp
- Upgrade chart:	helm upgrade myapp ./my-chart
- View current values:	helm get values myapp
- Lint your chart:	helm lint ./my-chart
- Create a new chart:	helm create my-chart
- Add chart repo:	helm repo add bitnami https://charts.bitnami.com/bitnami
- Search charts:	helm search repo nginx

###  Pro Tips
- Store Helm charts in a Git repo for version control.

- Use helm diff (via plugin) before upgrading to see changes.

