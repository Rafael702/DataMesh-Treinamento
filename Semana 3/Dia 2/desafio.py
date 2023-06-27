from pyspark.sql import SparkSession

sparkContext = SparkSession.builder.appName('sparkOf').getOrCreate()
data = [("Alice", 25), ("Bob", 30), ("Charlie", 35)]
rdd = sparkContext.parallelize(data)
filteredRDD = rdd.filter(rdd._2 > 30)
count = filteredRDD.count()
print(count)