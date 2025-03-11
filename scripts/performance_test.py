from pyspark.sql import SparkSession
from time import time
from tqdm import tqdm

def run_performance_tests(spark, data_path):
    results = []
    
    # 读取数据
    start_time = time()
    df = spark.read.format("avro").load(data_path)
    df.cache()
    load_time = time() - start_time
    
    # 定义测试查询
    queries = [
        {
            "name": "Count by event_type",
            "query": lambda df: df.groupBy("event_type").count()
        },
        {
            "name": "Average rating by content",
            "query": lambda df: df.groupBy("content_id").agg({"rating": "avg"})
        },
        {
            "name": "Daily active users",
            "query": lambda df: df.selectExpr("date_trunc('day', from_unixtime(timestamp/1000)) as date", "user_id").distinct()
        }
    ]
    
    # 执行查询测试
    for query in tqdm(queries, desc="Running performance tests"):
        start_time = time()
        query["query"](df).collect()
        query_time = time() - start_time
        results.append({
            "query_name": query["name"],
            "execution_time": query_time
        })
    
    return {
        "load_time": load_time,
        "query_results": results
    }
