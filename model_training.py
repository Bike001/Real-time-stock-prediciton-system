from pyspark.ml import Pipeline
from pyspark.ml.feature import StandardScaler, VectorAssembler
from pyspark.ml.regression import LinearRegression
from pyspark.ml.tuning import CrossValidator, ParamGridBuilder
from pyspark.ml.evaluation import RegressionEvaluator
from data_preparation import create_spark_session, load_and_preprocess_data

def train_model(data_path):
    try:
        print("Script started")
        df = load_and_preprocess_data(data_path)
        print("Data loaded and preprocessed")
        
        train_data, test_data = df.randomSplit([0.8, 0.2], seed=42)
        assembler = VectorAssembler(inputCols=df.columns[:-1], outputCol="features")
        scaler = StandardScaler(inputCol="features", outputCol="scaledFeatures")
        lr = LinearRegression(featuresCol="scaledFeatures", labelCol="label")
        
        pipeline = Pipeline(stages=[assembler, scaler, lr])
        print("Starting model training...")
        
        paramGrid = (ParamGridBuilder()
                     .addGrid(lr.regParam, [0.1, 0.01, 0.001])
                     .addGrid(lr.elasticNetParam, [0.0, 0.5, 1.0])
                     .build())
        evaluator = RegressionEvaluator(metricName="rmse")
        cv = CrossValidator(estimator=pipeline, estimatorParamMaps=paramGrid, evaluator=evaluator, numFolds=5)
        
        cvModel = cv.fit(train_data)
        model_dir = "/Users/yusoo/Downloads/kafka_2.13-3.7.0/stock/mymodel"
        cvModel.bestModel.write().overwrite().save(model_dir)  # Use overwrite to replace existing directory
        print(f"Model saved successfully in {model_dir}")
    except Exception as e:
        print("Error during training or saving the model:", e)

if __name__ == "__main__":
    data_path = "/Users/yusoo/Downloads/kafka_2.13-3.7.0/AAPL.csv"  # Make sure this path points to your actual data
    train_model(data_path)
