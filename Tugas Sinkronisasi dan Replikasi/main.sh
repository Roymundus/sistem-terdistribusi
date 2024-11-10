cd primary
docker build -t primary-db .


cd ../secondary
docker build -t secondary-db .


docker run -d --name primary-db primary-db

docker run -d --name primary-db --network pg-replication-net primary-db

docker run -d --name secondary-db --network pg-replication-net secondary-db


docker exec -it primary-db psql -U admin -d primarydb -c "CREATE TABLE test_table (id SERIAL PRIMARY KEY, data TEXT);"
docker exec -it primary-db psql -U admin -d primarydb -c "INSERT INTO test_table (data) VALUES ('Replication Test Data');"


docker exec -it secondary-db psql -U admin -d secondarydb -c "SELECT * FROM test_table;"


docker restart secondary-db
docker exec -it secondary-db psql -U admin -d secondarydb -c "SELECT * FROM test_table;"

