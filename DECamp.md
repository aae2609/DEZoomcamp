# Data Engineering Zoomcamp 2024

## Module 1
Docker & SQL

### HW

1. Ingest data into postgres

    0. Start Docker Engine
    1. Start a docker container with db:
       `docker run -it -e POSTGRES_USER="root" -e POSTGRES_PASSWORD="root" -e POSTGRES_DB="ny_taxi" -v C:\_prog\DEZoomcamp\data\postgres_db:/var/lib/postgresql/data -p 5431:5432 postgres:13`
    2. Test connection:
        a. `docker ps`  # copy <container_id>
        b. `docker exec -it <container_id> /bin/bash`
        c. `psql -d ny_taxi`
        d. `\dt`
    3. Insert data
