from generate_synthetic_data import generate_synthetic_data
from validate_data import validate_data_quality
from performance_test import run_performance_tests
from pyspark.sql import SparkSession
import logging
from datetime import datetime

def main():
    # 设置日志记录
    logging.basicConfig(
        filename=f'logs/datalake_results_{datetime.now().strftime("%Y%m%d_%H%M%S")}.log',
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s'
    )
    
    # 初始化 Spark，添加avro支持
    spark = SparkSession.builder \
        .appName("DataLakeProject") \
        .config("spark.jars.packages", "org.apache.spark:spark-avro_2.12:3.5.0") \
        .getOrCreate()
    
    # 配置
    schema_path = "/data/wuyifan/agent_with_tool_calling/DataLakeProject/schemas/user_interation.avsc"
    output_path = "data/synthetic_data.avro"
    num_records = 100000  # 生成100万条记录
    
    try:
        # 生成合成数据
        generate_synthetic_data(num_records, output_path, schema_path)
        logging.info(f"Successfully generated {num_records} records to {output_path}")
        
        # 验证数据质量
        validation_results = validate_data_quality(spark, output_path)
        logging.info(f"Validation Results: {validation_results}")
        
        # 运行性能测试
        performance_results = run_performance_tests(spark, output_path)
        logging.info(f"Performance Results: {performance_results}")
        
    except Exception as e:
        logging.error(f"Error occurred: {str(e)}")
        raise e
    finally:
        spark.stop()

if __name__ == "__main__":
    main()