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