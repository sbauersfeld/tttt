from databricks.sdk.runtime import spark
from pyspark.sql.functions import col

from lib import double

@udf
def triple(row_num):
  x = row_num + 1
  return double(x) + x

spark.range(5).select(triple(col("id")).alias("result")).display()
