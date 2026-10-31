# 数据管理小工具 (Data Manager)

一个基于 Python 的控制台数据管理工具，支持 **JSON / CSV 双格式持久化**、自动备份、日志记录、配置化运行，并已打包为可直接分发的 exe。

## ✨ 功能特性

- **12 项数据管理功能**：增 / 删 / 改 / 查、展示全部、批量添加、关键词搜索
- **JSON / CSV 双格式**：数据保存为 JSON，支持 CSV 一键导入 / 导出
- **自动备份**：每次保存前自动生成 `.bak` 备份副本
- **日志系统**：基于 `logging`，控制台 + 文件双输出（`app.log`）
- **配置化**：数据文件名、备份后缀、日志级别等全部由 `config.json` 控制，改配置不改代码
- **异常处理**：文件缺失 / 格式损坏时友好提示，程序不崩溃
- **单元测试**：基于 `pytest`，10 个用例覆盖核心逻辑
- **exe 打包**：基于 PyInstaller，无需 Python 环境即可运行

## 🛠 技术栈

Python 3 · 面向对象（封装 / 继承）· json / csv / os / shutil / logging · pytest · PyInstaller

## 📁 项目结构

```
ai-text-summary-tool/
├── main.py          # 主程序（菜单逻辑）
├── utils.py         # DataManager / CSVDataManager 类 + 工具函数
├── test_utils.py    # pytest 单元测试
├── config.json      # 配置文件
├── requirements.txt # 开发 / 测试依赖
├── data.json        # 数据文件（运行时生成）
├── app.log          # 日志文件（运行时生成）
└── dist/
    └── 数据管理工具.exe   # 打包后的可执行文件
```

## 🚀 快速开始

### 方式一：源码运行（需要 Python 3.8+）

```bash
pip install -r requirements.txt
python main.py
```

### 方式二：运行 exe（无需 Python）

1. 进入 `dist/` 目录
2. 双击 `数据管理工具.exe`（或命令行运行）

> 注意：exe 需要和 `config.json` 放在同一目录（已默认放好）

## ⚙️ 配置说明

编辑 `config.json`：

```json
{
    "data_file": "data.json",
    "backup_suffix": ".bak",
    "log_level": "INFO",
    "csv_export": "data_export.csv"
}
```

| 配置项 | 说明 |
|---|---|
| `data_file` | 数据文件路径（默认 data.json） |
| `backup_suffix` | 自动备份后缀（默认 .bak） |
| `log_level` | 日志级别：DEBUG / INFO / WARNING / ERROR |
| `csv_export` | CSV 导出文件名（默认 data_export.csv） |

## ✅ 运行测试

```bash
python -m pytest -v
```

## 📦 打包为 exe

```bash
pip install pyinstaller
pyinstaller --onefile --name 数据管理工具 main.py
```

打包后把 `dist/数据管理工具.exe` 与 `config.json` 一起分发即可。

## 📝 菜单功能

```
1. 查询数据        7. 查看当前工作目录
2. 修改数据        8. 查看目录下全部文件
3. 删除数据        9. 批量添加多条数据
4. 保存数据到文件  10. 按关键词搜索数据
5. 添加新数据      11. 导出数据为CSV文件
6. 展示全部数据    12. 从CSV文件导入数据
0. 退出程序
```

## 📄 License

MIT
