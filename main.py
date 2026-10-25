# =========================================
# 数据管理小工具：主程序（只负责菜单逻辑）
# 工具函数都放在 utils.py，这里用 import 导入
# =========================================
import os
from utils import save_json, load_json, add_info, modify_info, delete_info, show_all_data, list_all_files

# 不管程序从哪里运行，都能定位到项目目录和data.json的绝对路径
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_FILE = os.path.join(BASE_DIR, "data.json")


def main_menu():
    """主菜单：整合全部功能"""
    # 启动时加载数据
    status, data = load_json(DATA_FILE)

    if not status:
        data = {}

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
        print("0. 退出程序")
        choice = input("请输入功能编号：").strip()
        if choice not in ["0", "1", "2", "3", "4", "5", "6", "7", "8"]:
            print("请输入0~8之间有效的功能编号！")
            continue

        if choice == "0":
            print("程序退出")
            break
        elif choice == "1":
            key = input("输入要查询的key：").strip()
            if key in data:
                print(f"{key}: {data[key]}")
            else:
                print("该键不存在")
        elif choice == "2":
            key = input("输入要修改的key：").strip()
            new_val = input("输入新的值：").strip()
            ok, msg = modify_info(data, key, new_val)
            print(msg)
        elif choice == "3":
            key = input("输入要删除的key：").strip()
            ok, msg = delete_info(data, key)
            print(msg)

        elif choice == "4":
            ok, msg = save_json(data, DATA_FILE)
            print(msg)
        elif choice == "5":
            key = input("输入新增key：").strip()
            val = input("输入新增value：").strip()
            ok, msg = add_info(data, key, val)
            print(msg)
        elif choice == "6":
            print(show_all_data(data))
        elif choice == "7":
            print("当前工作目录：", os.getcwd())
        elif choice == "8":
            ok, res = list_all_files(os.getcwd())
            if ok:
                print("当前目录内文件列表：")
                for item in res:
                    print("-", item)
            else:
                print(res)
        else:
            print("输入无效，请重新选择！")



# 程序入口，只有直接运行这个py文件才会执行
if __name__ == "__main__":
    main_menu()
