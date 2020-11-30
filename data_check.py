import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job



## @params: [JOB_NAME]
args = getResolvedOptions(sys.argv, ['JOB_NAME'])

sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

#load table from S3
fod = glueContext.create_dynamic_frame.from_catalog(database = "demo-db-dblp-acm", table_name = "fodors_zagats_csv")
fodm = glueContext.create_dynamic_frame.from_catalog(database = "demo-db-dblp-acm", table_name = "fodors_marked_csv")


#create temp table in spark
fod.toDF().createOrReplaceTempView("fodors_zagats")
fodm.toDF().createOrReplaceTempView("fodors_marked_csv")

logger = logger = glueContext.get_logger()

# execute fodors_zagats CR rule
# fodrule1 = foda.fromDF(spark.sql("SELECT * FROM fodors_zagats LIMIT 5"), glueContext, "fodrule1")
logger.info(spark.sql("SELECT * FROM fodors_zagats LIMIT 5"), glueContext, "fodrule1")

# fodrule1 = foda.fromDF(spark.sql("SELECT t0.id,t0.name FROM fodors_zagats AS t0 INNER JOIN fodors_zagat_tablea AS t1 ON t0.city = t1.city"), glueContext, "fodrule1")
# glueContext.write_dynamic_frame.from_options(frame = fodrule1, connection_type = "s3", connection_options = {"path": "s3://podrulediscoveranalysis/result/CR3/fodors_zagats"}, format = "csv")


job.commit()