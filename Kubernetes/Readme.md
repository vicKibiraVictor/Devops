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

