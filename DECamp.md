# Data Engineering Zoomcamp 2024

## Module 1
Docker & SQL

### HW

1. Which tag has the following text? - Automatically remove the container when it exits
> docker run --rm

2. What is version of the package wheel?
> 0.42.0

3. Ingest data into postgres


docker run -it -e POSTGRES_USER="root" -e POSTGRES_PASSWORD="root" -e POSTGRES_DB="ny_taxi" -v C:\_prog\DEZoomcamp\data\postgres_db:/var/lib/postgresql/data -p 5431:5432 postgres:13
