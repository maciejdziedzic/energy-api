# Instruction:

#### 1. Set-up Docker

##### 1.A. Run 'docker compose up' inside airflow directory

##### 1.B. Run 'docker compose up' inside kafka directory

##### 1.C. Run 'docker compose up' inside spark

##### Make sure that all containers are up and finished the setup. Re-start if necessary

![Docker](https://github.com/maciejdziedzic/energy-api/blob/main/assets/docker.gif?raw=true)

#### 2. Login to airflow (acc:airflow, password: airflow) UI and run a job (http://localhost:8080/)

![Docker](https://github.com/maciejdziedzic/energy-api/blob/main/assets/airflow.gif?raw=true)

#### 3. Check if broker is healthy inside Kafka controller. Once job is running, you can check upcoming messages inside proper topic (http://localhost:9021/clusters)

![Docker](https://github.com/maciejdziedzic/energy-api/blob/main/assets/kafka_cc.gif?raw=true)

#### 4. You can run data analysis inside Jupyter notebook from energy_api/spark/streaming.ipynb on (http://localhost:8888/)

![Docker](https://github.com/maciejdziedzic/energy-api/blob/main/assets/notebook.gif?raw=true)
