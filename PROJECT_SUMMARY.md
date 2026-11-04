# 项目整理总览（2026-10-31 更新）

## 一、核心项目：数据管理小工具（Data Manager）

> 一个基于 Python 的控制台数据管理工具，从零学习 Python 逐步迭代到工程化成品，最终双平台托管。

### 1. 项目概述
- **学习方式**：B站视频理论学习 + 逐功能实战迭代（共 29 个 Git 提交，记录完整成长轨迹）
- **最终形态**：12 项功能的控制台应用，支持 JSON/CSV 双格式持久化、自动备份、日志、配置化、单元测试、exe 打包
- **简历定位**：完整展示 Python 基础 → 面向对象 → 工程化（测试/日志/配置/打包）全链路能力

### 2. 功能清单（12 项菜单）
| 编号 | 功能 | 编号 | 功能 |
|---|---|---|---|
| 1 | 查询数据 | 7 | 查看当前工作目录 |
| 2 | 修改数据 | 8 | 查看目录下全部文件 |
| 3 | 删除数据 | 9 | 批量添加多条数据 |
| 4 | 保存数据到文件 | 10 | 按关键词搜索数据 |
| 5 | 添加新数据 | 11 | 导出数据为CSV文件 |
| 6 | 展示全部数据 | 12 | 从CSV文件导入数据 |
| 0 | 退出程序 | | |

### 3. 技术栈与工程能力
- **语言**：Python 3（面向对象：封装/继承）
- **标准库**：json、csv、os、shutil、logging
- **测试**：pytest（10 个用例，tmp_path + 参数化）
- **配置化**：config.json（数据文件名/备份后缀/日志级别/CSV导出名）
- **打包分发**：PyInstaller → `dist/数据管理工具.exe`（8.3MB，无需 Python 环境）
- **版本控制**：Git，双远程（Gitee + GitHub）

### 4. 项目文件结构
```
D:\ai-text-summary-tool\
├── main.py            # 主程序：菜单逻辑 + 配置加载 + exe兼容路径
├── utils.py           # DataManager / CSVDataManager 类 + 工具函数 + 日志
├── test_utils.py      # pytest 单元测试（10 passed）
├── config.json        # 配置文件
├── requirements.txt   # 依赖清单（pytest / pyinstaller）
├── README.md          # 项目文档（GitHub 主页展示）
├── .gitignore         # 忽略规则
├── data.json          # 运行时数据（自动生成 + .bak 备份）
├── app.log            # 日志文件（自动生成）
└── dist\              # 打包产物（数据管理工具.exe + config.json）
```

### 5. 双平台仓库（已同步到最新提交）
- **GitHub**：https://github.com/wei666-ing/ai-text-summary-tool
- **Gitee**：https://gitee.com/wei-gudu/ai-text-summary-tool

---

## 二、Git 提交历史（29 个提交，完整成长轨迹）

### 阶段A：基础功能迭代（1–10号 + 校验 + 异常 + os）
- JSON 持久化 → 展示全部 → 输入校验（空key/空value/重复key）→ 菜单编号校验
- 文件读取异常捕获（try-except）→ os.path.exists 预判 → os 模块（工作目录/文件列表）
- 代码模块化拆分（utils.py）→ 路径修复（__file__ 定位数据文件）

### 阶段B：工程化功能
- shutil 自动备份 → 单元测试（手写 assert）→ *args/**kwargs（批量添加/自定义后缀）
- 推导式 + 关键词搜索（10号功能）

### 阶段C：面向对象 + 继承
- DataManager 类（12 个方法）→ CSVDataManager 子类（CSV 导入导出）

### 阶段D：工程四件套
- logging 日志 → config.json 配置化 → pytest 重写测试（10 passed）→ PyInstaller exe 打包

### 阶段E：双平台托管
- 推送 Gitee → 创建并推送 GitHub → 完善 README + requirements.txt

---

## 三、学习路线进度（阶段2：数据基础）

### 当前进度
| 模块 | 状态 | 练习文件 |
|---|---|---|
| NumPy 基础（数组/索引/运算/统计） | ✅ 已完成 | `numpy_demo.py` |
| NumPy 进阶（变形/拼接/布尔索引/广播/随机数） | ✅ 已完成 | `numpy_advanced.py` |
| Pandas 入门（DataFrame/筛选/缺失值/CSV读写） | ✅ 已完成 | `pandas_demo.py` |
| Matplotlib 可视化 | ⏳ 待开始 | `matplotlib_demo.py` |
| Pandas 进阶（loc/iloc/groupby/merge/apply） | ⏳ 待开始 | `pandas_advanced_demo.py` |

> 说明：练习文件统一命名 `*_demo.py` / `*_advanced.py`，已被 .gitignore 忽略，**不提交到 GitHub 仓库**（保持正式项目仓库干净）。学习记录以本文件为准。

### 后续规划
- **主线A**：数据结构与算法（线性表/查找/排序/树）+ LeetCode 每日一题
- **主线B**：机器学习基础（吴恩达课程 + sklearn 实战）
- **可选**：README 加运行截图、tkinter GUI 升级、Linux 基础

---

## 四、待办与建议
- [ ] Matplotlib 可视化练习（下一步）
- [ ] 数据管理项目 README 加运行截图
- [ ] 数据结构与算法：LeetCode 热题100 启动
- [ ] 机器学习入门（吴恩达 + sklearn 小项目）
