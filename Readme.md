# Benchmarking 
The goal was to test a 1GB data for in-memory computation, using DuckDB and Spark.

This project, I used my local P.C with 16GB RAM, 12 CPU CORES.



## How to Run
* docker-compose up to set up Apache spark on your local machine (Requirement: have docker installed)
* Generate the data in parquet by running

```sh
python ducks.py
```

### setting up Spark
* install Apache Spark 
* set the Environment Variables
* set path for Hadoop
* start master and worker
* run `main.ipynb` 



## setting up DuckDB
* run `ducks.ipynb`