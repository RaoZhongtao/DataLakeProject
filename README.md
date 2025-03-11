# DataLakeProject

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

main.py 主程序入口

# 主要职责：
- 初始化 Spark 环境
- 协调各个模块的执行流程
- 配置关键参数
- 记录执行结果和日志

generate_synthetic_data.py - 数据生成模块
# 主要职责：
- 根据指定的 Avro schema 生成合成测试数据
- 控制数据生成的数量和质量
- 将生成的数据保存为 Avro 格式

validate_data.py- 数据质量验证模块
# 主要职责：
- 验证生成数据的质量和完整性
- 检查数据是否符合预定义的规则
- 生成数据质量报告

performance_test.py - 性能测试模块
# 主要职责：
- 测试数据处理性能
- 评估查询效率
- 生成性能测试报告

user_interation.avsc - Schema 定义
# 主要职责：
- 定义数据结构和格式
- 指定字段类型和约束
- 确保数据的一致性