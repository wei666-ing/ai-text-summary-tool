# =========================================
# 数据管理小工具：主程序（面向对象版本 + logging日志）
# 数据管理全部封装在 utils.py 的 DataManager 类里
# =========================================
import os
from utils import CSVDataManager, logger

# 不管程序从哪里运行，都能定位到项目目录和data.json的绝对路径
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_FILE = os.path.join(BASE_DIR, "data.json")


def main_menu():
    """主菜单：整合全部功能"""
    # 创建数据管理器对象，自动加载数据
    dm = CSVDataManager(DATA_FILE)

    while True:
        print("\n===== 数据管理菜单 =====")
        print("1. 查询数据")
        print("2. 修改数据")
        print("3. 删除数据")
        print("4. 保存数据到文件")
        print("5. 添加新数据")
        print("6. 展示全部数据")
        print("7. 查看当前工作目录")
        print("8. 查看目录下全部文件")
        print("9. 批量添加多条数据")
        print("10. 按关键词搜索数据")
        print("11. 导出数据为CSV文件")
        print("12. 从CSV文件导入数据")
        print("0. 退出程序")
        choice = input("请输入功能编号：").strip()
        if choice not in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12"]:
            logger.warning("请输入0~12之间有效的功能编号！")
            continue

        if choice == "0":
            logger.info("程序退出")
            break
        elif choice == "1":
            key = input("输入要查询的key：").strip()
            val = dm.query(key)
            if val is not None:
                logger.info(f"{key}: {val}")
            else:
                logger.warning("该键不存在")
        elif choice == "2":
            key = input("输入要修改的key：").strip()
            new_val = input("输入新的值：").strip()
            ok, msg = dm.modify(key, new_val)
            logger.info(msg)
        elif choice == "3":
            key = input("输入要删除的key：").strip()
            ok, msg = dm.delete(key)
            logger.info(msg)
        elif choice == "4":
            ok, msg = dm.save()
            logger.info(msg)
        elif choice == "5":
            key = input("输入新增key：").strip()
            val = input("输入新增value：").strip()
            ok, msg = dm.add(key, val)
            logger.info(msg)
        elif choice == "6":
            logger.info("\n" + dm.show_all())
        elif choice == "7":
            logger.info(f"当前工作目录：{os.getcwd()}")
        elif choice == "8":
            ok, res = dm.list_files(os.getcwd())
            if ok:
                logger.info("当前目录内文件列表：")
                for item in res:
                    logger.info(f"- {item}")
            else:
                logger.warning(res)
        elif choice == "9":
            print("批量添加，输入格式示例：name 小明 age 20 city 广州")
            raw = input("请一次性输入key value，空格隔开：")
            parts = raw.split()
            succ, fail = dm.batch_add(*parts)
            if succ:
                logger.info(f"✅ 添加成功：{succ}")
            if fail:
                logger.warning(f"❌ 添加失败：{fail}")
        elif choice == "10":
            kw = input("输入搜索关键词：").strip()
            result = dm.search(kw)
            if result:
                logger.info("🔍 搜索到以下记录：")
                for k, v in result.items():
                    logger.info(f"{k}: {v}")
            else:
                logger.warning("没有找到包含该关键词的记录")
        elif choice == "11":
            csv_path = os.path.join(os.path.dirname(DATA_FILE), "data_export.csv")
            ok, msg = dm.export_csv(csv_path)
            logger.info(msg)
        elif choice == "12":
            csv_path = os.path.join(os.path.dirname(DATA_FILE), "data_export.csv")
            mode = input("选择导入模式：1=合并(重复跳过) 2=覆盖全部：").strip()
            overwrite = (mode == "2")
            ok, msg = dm.import_csv(csv_path, overwrite=overwrite)
            logger.info(msg)
        else:
            logger.warning("输入无效，请重新选择！")


# 程序入口，只有直接运行这个py文件才会执行
if __name__ == "__main__":
    main_menu()
