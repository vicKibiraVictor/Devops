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

https://minikube.sigs.k8s.io/docs/start/?arch=%2Flinux%2Fx86-64%2Fstable%2Fbinary+download

On MacOS

```
curl -LO https://github.com/kubernetes/minikube/releases/latest/download/minikube-darwin-amd64
sudo install minikube-darwin-amd64 /usr/local/bin/minikube

```
On Linux
```
curl -LO https://github.com/kubernetes/minikube/releases/latest/download/minikube-linux-amd64
sudo install minikube-linux-amd64 /usr/local/bin/minikube && rm minikube-linux-amd64

```