# =========================================
# 数据管理小工具：主程序（只负责菜单逻辑）
# 工具函数都放在 utils.py，这里用 import 导入
# =========================================
import os
from utils import save_json, load_json, add_info, modify_info, delete_info, show_all_data


def main_menu():
    """主菜单：整合全部功能"""
    # 启动时加载数据
    status, data = load_json("data.json")

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
        print("0. 退出程序")
        choice = input("请输入功能编号：").strip()
        valid_choices = ["0","1","2","3","4","5","6","7"]
        if choice not in valid_choices:
            print("请输入0~6之间有效的功能编号！")
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
            if not key:
                print("错误：key不能为空！")
            elif key not in data:
                print(f"错误：key【{key}】不存在，无法修改")
            else:
                new_val = input("输入新的值：").strip()
                if not new_val:
                    print("错误：值不能为空！")
                else:
                    data[key] = new_val
                    print("修改成功！")
        elif choice == "3":
            key = input("输入要删除的key：").strip()
            if not key:
                print("错误：key不能为空！")
            elif key not in data:
                print(f"错误：key【{key}】不存在，无法删除")
            else:
                del data[key]
                print("删除成功！")
        elif choice == "4":
            ok, msg = save_json(data, "data.json")
            print(msg)
        elif choice == "5":
            key = input("输入新增key：").strip()
            val = input("输入新增value：").strip()
            if not key or not val:
                print("错误：key 和 value 都不能为空！")
            elif key in data:
                print(f"错误：key【{key}】已经存在，不能重复添加！")
            else:
                ok, msg = add_info(data, key, val)
                print(msg)
        elif choice == "6":
            print(show_all_data(data))
        elif choice == "7":
            print("当前工作目录：", os.getcwd())
        else:
            print("输入无效，请重新选择！")


# 程序入口，只有直接运行这个py文件才会执行
if __name__ == "__main__":
    main_menu()
