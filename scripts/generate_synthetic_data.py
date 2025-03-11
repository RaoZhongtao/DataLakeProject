from faker import Faker
import random
from datetime import datetime, timedelta
import json
from tqdm import tqdm
import avro.schema
from avro.datafile import DataFileWriter
from avro.io import DatumWriter

fake = Faker()

def generate_synthetic_data(num_records, output_path, schema_path):
    # 读取 Avro schema
    schema = avro.schema.parse(open(schema_path).read())
    
    # 创建 Avro 写入器
    writer = DataFileWriter(open(output_path, "wb"), DatumWriter(), schema)
    
    # 生成数据
    for _ in tqdm(range(num_records), desc="Generating synthetic data"):
        record = {
            "user_id": fake.uuid4(),
            "event_type": random.choice(["CLICK", "RATING", "VIEW"]),
            "timestamp": int(datetime.now().timestamp() * 1000),
            "content_id": fake.uuid4(),
            "rating": random.randint(1, 5) if random.random() > 0.5 else None,
            "watch_time": random.randint(0, 7200) if random.random() > 0.3 else None,
            "device_type": random.choice(["mobile", "desktop", "tablet"])
        }
        writer.append(record)
    
    writer.close()
