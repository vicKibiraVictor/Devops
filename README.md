### Docker

Docker is a software as a service that ships software as packages called containers.

### To run a container

On the terminal run

```bash
docker run hello-world
```

### To check running containers

```
docker ps
```

### To inspect a container

```
docker inspect container_id
```

### Useful docker commands
```
docker inspect container_id
docker rm container_id
docker rmi image_id
docker logs container_id
docker volume ls
docker network create network_name
docker-compose up
docker-compose down
docker-compose logs
docker stop container_id
docker ps -a
docker-compose restart
docker stop $(docker ps -a)
```

### Example: To start a postgres instance
```
docker run -it \
  --name postgres-two \
  --network my-network \
  -e POSTGRES_PASSWORD=root \
  -e POSTGRES_USER=root \
  -e POSTGRES_DB=root \
  -p 5432:5432 \
  -v postgres_data:/var/lib/postgresql/data \
  -d postgres

```
### To access it


```
psql -h 172.17.0.2 -p 5432 -d postgres

```
### To build a docker image
First create a docker file for the application,and then run

```
docker build -t hello-python .
docker run --rm hello-python

```

### License

[MIT](https://choosealicense.com/licenses/mit/)


 ### Debugging
 docker logs container_id
 docker exec -it container_id bin/bash
 docker inspect container_id



