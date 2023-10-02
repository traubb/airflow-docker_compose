# Example DAG's in Airflow with Docker Compose

## Getting started
1. Start Docker
```
sudo service docker start
```
2. Start Airflow Webserver, Scheduler and postgres with docker compose
```
docker compose up -d
```
3. Now you should see the Airflow UI on http://localhost:8080
4. Both Example DAG's (one whit written Operator and one withoud Operator) should be visible
5. If you are finished run the following to shut down docker compose:
```
docker compose down
```