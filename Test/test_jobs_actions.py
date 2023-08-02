# Databricks notebook source
from pyspark.sql.types import *

# COMMAND ----------

schema = StructType([StructField('quarter', DoubleType(), True), StructField('industry_code', StringType(), True), StructField('industry_name', StringType(), True), StructField('filled jobs', IntegerType(), True), StructField('filled jobs revised', IntegerType(), True), StructField('filled jobs diff', IntegerType(), True), StructField('filled jobs % diff', DoubleType(), True), StructField('total_earnings', IntegerType(), True), StructField('total earnings revised', IntegerType(), True), StructField('earnings diff', IntegerType(), True), StructField('earnings % diff', DoubleType(), True)])

df = spark.read.csv("dbfs:/mnt/nahid/test_csv.csv", header=True, schema=schema)

# COMMAND ----------

df.collect()

# COMMAND ----------

dbutils.fs.ls("/mnt/")
