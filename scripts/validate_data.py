from pyspark.sql import SparkSession
from pyspark.sql.functions import col
from tqdm import tqdm

def validate_data_quality(spark, data_path):
    # 读取数据
    df = spark.read.format("avro").load(data_path)
    
    # 定义验证规则
    validations = [
        {
            "name": "user_id_not_null",
            "condition": col("user_id").isNotNull(),
            "message": "user_id must not be null"
        },
        {
            "name": "rating_range",
            "condition": (col("rating").isNull()) | ((col("rating") >= 1) & (col("rating") <= 5)),
            "message": "rating must be between 1 and 5"
        },
        {
            "name": "timestamp_not_null",
            "condition": col("timestamp").isNotNull(),
            "message": "timestamp must not be null"
        }
    ]
    
    # 执行验证
    validation_results = []
    for validation in tqdm(validations, desc="Validating data"):
        invalid_count = df.filter(~validation["condition"]).count()
        validation_results.append({
            "name": validation["name"],
            "failed_records": invalid_count,
            "message": validation["message"]
        })
    
    return validation_results
