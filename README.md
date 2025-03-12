English Version

# DataLakeProject

![image](https://github.com/user-attachments/assets/ce56445d-5d56-4cc4-8ae8-9e743cf0611d)

## Overview ✨
DataLakeProject is a scalable data pipeline designed to ingest, validate, and test user interaction data in a robust, production-grade environment. Leveraging Apache Spark and Apache Avro, this project ensures consistent data processing and seamless schema evolution, making it adaptable to future requirements such as adding new fields like “watch_time.”

![image](https://github.com/user-attachments/assets/7ed88cc9-ee72-4e86-b167-8ac8ec9124c7)


## Key Features 
- **Schema Design**  
  - Defines user interaction data (e.g., clicks, ratings) using Apache Avro (or Protobuf).  
  - Ensures forward and backward compatibility for effortless schema evolution.

- **Data Pipeline CI/CD**  
  - Integrates a GitHub Actions pipeline to automate data quality checks (e.g., nulls, range validations) on every commit.  
  - Maintains high data integrity through continuous integration.

- **Synthetic Data Testing**  
  - Generates synthetic data using tools like Faker or Synthetic Data Vault to simulate a 10x scale of real-world usage.  
  - Tests data ingestion and query performance using Spark (or Trino), identifying potential bottlenecks and optimizing throughput.

## Project Structure 🗂️
```
DataLakeProject/
├── schemas/
│   └── user_interation.avsc    # Avro schema definition file
├── scripts/
│   ├── main.py                 # Main entry point: initializes Spark, configures parameters, orchestrates module execution, and logs results
│   ├── generate_synthetic_data.py  # Module to generate synthetic test data based on the Avro schema
│   ├── validate_data.py        # Module for validating data quality and generating reports
│   └── performance_test.py     # Module for testing data processing performance and query efficiency
├── data/                       # Directory for storing generated data (e.g., synthetic_data.avro)
└── logs/                       # Directory for execution logs and reports
```

## Requirements & Deliverables 🛠️
- **Schema Definition:**  
  - Create an Avro/Protobuf schema for user interaction data ensuring forward/backward compatibility.

- **CI/CD Pipeline:**  
  - Implement a GitHub Actions workflow to continuously validate data quality by checking for null values, proper ranges, and other integrity constraints.

- **Synthetic Data & Performance Testing:**  
  - Generate synthetic data at 10x scale to simulate production environments.  
  - Evaluate data ingestion and query performance with Apache Spark (or Trino).

- **Deliverables:**  
  - A GitHub repository containing the schema and CI/CD pipeline code.  
  - A one-page report summarizing the scalability test results.

## Getting Started 🌱

### Prerequisites
- **Python 3.7+**  
- **Apache Spark** (properly configured)  
- Required Python packages (listed in `requirements.txt`)

### Setup & Execution
1. **Clone the Repository:**
   ```bash
   git clone https://github.com/yourusername/DataLakeProject.git
   cd DataLakeProject
   ```

2. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Pipeline Modules:**
   - **Generate Synthetic Data:**
     ```bash
     python scripts/generate_synthetic_data.py
     ```
   - **Validate Data Quality:**
     ```bash
     python scripts/validate_data.py
     ```
   - **Execute Performance Tests:**
     ```bash
     python scripts/performance_test.py
     ```
   - **Run the Complete Workflow:**
     ```bash
     python scripts/main.py
     ```

4. **Review Logs & Reports:**
   - Check the `logs/` directory for detailed execution logs and performance test reports.

## Contributing 🤝
Contributions are welcome! Please fork the repository, create a feature branch, and submit a pull request. For major changes, open an issue to discuss your ideas before proceeding.

## License 📄
This project is licensed under the MIT License.

---

DataLakeProject provides a flexible, high-performance solution for managing large-scale user interaction data. Enjoy exploring, and feel free to contribute to make it even better!

---

中文版

# DataLakeProject
```
DataLakeProject/
├── schemas/
│   └── user_interation.avsc    # Avro schema 定义文件
├── scripts/
│   ├── main.py                 # 主程序入口
│   ├── generate_synthetic_data.py  # 生成合成数据
│   ├── validate_data.py        # 数据质量验证
│   └── performance_test.py     # 性能测试
├── data/                       # 数据存储目录
│   └── synthetic_data.avro     # 生成的测试数据
└── logs/                       # 日志存储目录
```
# main.py 主程序入口主要职责：
- 初始化 Spark 环境
- 协调各个模块的执行流程
- 配置关键参数
- 记录执行结果和日志

# generate_synthetic_data.py - 数据生成模块主要职责：
- 根据指定的 Avro schema 生成合成测试数据
- 控制数据生成的数量和质量
- 将生成的数据保存为 Avro 格式

# validate_data.py- 数据质量验证模块主要职责：
- 验证生成数据的质量和完整性
- 检查数据是否符合预定义的规则
- 生成数据质量报告

# performance_test.py - 性能测试模块主要职责：
- 测试数据处理性能
- 评估查询效率
- 生成性能测试报告

# user_interation.avsc - Schema 定义主要职责：
- 定义数据结构和格式
- 指定字段类型和约束
- 确保数据的一致性
