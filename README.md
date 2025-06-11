# devops


docker run --name some-postgres -e POSTGRES_PASSWORD=mysecretpassword -d postgres


psql -h 172.17.0.2 -p 5432 -d postgres


docker run -it \
  --name postgres-one \
  --network my-network \
  -e POSTGRES_PASSWORD=root \
  -e POSTGRES_USER=root \
  -e POSTGRES_DB=root \
  -d postgres
