from pyspark.sql import SparkSession

spark = SparkSession.builder.master("local[1]") \
          .appName("SparkByExamples.com") \
          .getOrCreate()

df = spark.read.parquet("./data/*")
df.printSchema()
