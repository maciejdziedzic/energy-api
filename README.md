# Instruction:

#### 1. Run 'docker compose up' inside airflow directory



### 2. Run 'docker compose up' inside kafka directory

### 3. Run 'docker compose up' inside spark

### 4. Make sure that all containers are up and finished the setup. Re-start if necessary

### 5. Login to airflow (acc:airflow, password: airflow) UI and run a job (http://localhost:8080/)

### 6. Check if broker is healthy inside Kafka controller. Once job is running, you can check upcoming messages inside proper topic (http://localhost:9021/clusters)

### 7. Run data analysis inside Jupyter notebook from energy_api/spark/streaming.ipynb on (http://localhost:8888/)
