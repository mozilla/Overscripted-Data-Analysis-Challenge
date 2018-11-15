import sys
from pyspark.sql import SparkSession, functions, types

spark = SparkSession.builder.appName('URL extractor').getOrCreate()

assert sys.version_info >= (3, 4) # make sure we have Python 3.4+
assert spark.version >= '2.1' # make sure we have Spark 2.1+

data = spark.read.parquet('/mnt/Data/UCOSP_DATA/sample_full_data/*')

#data = spark.read.csv('url_master_list.csv', header=True,
#                      inferSchema=True)
data.select('script_url').distinct().show(truncate=False)
