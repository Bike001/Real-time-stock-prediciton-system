from pyspark.sql import SparkSession
from pyspark.sql.window import Window
import pyspark.sql.functions as F
from pyspark.ml.feature import VectorAssembler

def create_spark_session():
    return SparkSession.builder.master("local[*]").appName("StockPricePrediction").getOrCreate()

def load_and_preprocess_data(file_path):
    spark = create_spark_session()
    df = spark.read.csv(file_path, header=True, inferSchema=True).select("Date", "Open")
    df = df.repartition(10)  # Good practice to specify partitions
    windowSpec = Window.orderBy("Date")  # No frame is needed for lag and lead functions
    
    for i in range(1, 21):
        df = df.withColumn(f"lag_{i}", F.lag("Open", i).over(windowSpec))
    df = df.withColumn("label", F.lead("Open", 1).over(windowSpec))
    df = df.dropna()
    feature_cols = [f"lag_{i}" for i in range(1, 21)] + ["label"]
    df = df.select(*feature_cols)
    return df


