from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .appName("Test App") \
    .getOrCreate()

df = spark.createDataFrame([(1, 'foo'), (2, 'bar')], ["ID", "Value"])
df.show()

spark.stop()
