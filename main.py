# =========================================
# 数据管理小工具：读取/查询/修改/新增/删除/保存
# =========================================

def read_file_to_dict(file_path):
    """读取 key=value 格式的文本文件，返回字典"""
    data_dict = {}
    try:
        # 打开文件，utf-8编码读取
        with open(file_path, "r", encoding="utf-8") as f:
            lines = f.readlines()
            # 循环每一行文本
            for line in lines:
                # 去掉每行前后换行、空格
                line = line.strip()
                # 如果是空行，跳过这一行
                if not line:
                    continue
                # 以等号分割一行文本，分成 key 和 value
                key, value = line.split("=")
                # 存入字典
                data_dict[key] = value
        return data_dict
    except FileNotFoundError:
        print("文件不存在！")
        return None
    except ValueError:
        print("该行格式错误，需要 key=value")
        return None


def get_value(data_dict, key):
    """根据key查询字典的值"""
    if key in data_dict:
        return data_dict[key]
    else:
        return "该键不存在"


def modify_info(data_dict, key, new_value):
    """修改已有键的值"""
    if key in data_dict:
        data_dict[key] = new_value
        return True, "修改成功"
    else:
        return False, "键不存在，无法修改"


def add_info(data_dict, key, value):
    """新增一条键值对（键不能重复）"""
    if key in data_dict:
        return False, "键已经存在，不能重复添加"
    data_dict[key] = value
    return True, "新增记录成功"


def delete_info(data_dict, key):
    """删除指定的键值对"""
    if key in data_dict:
        del data_dict[key]
        return True, "删除成功"
    else:
        return False, "键不存在，无法删除"


def save_dict_to_file(data_dict, file_path):
    """把字典保存到文件（每行 key:value 格式）"""
    try:
        with open(file_path, "w", encoding="utf-8") as f:
            for k, v in data_dict.items():
                f.write(f"{k}:{v}\n")
        return True, "保存成功"
    except Exception as e:
        return False, f"保存失败：{e}"


def load_dict_from_file(file_path):
    """从文件读取 key:value 数据，还原成字典"""
    data_dict = {}
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                k, v = line.split(":", 1)
                data_dict[k] = v
        return True, data_dict
    except Exception as e:
        return False, f"读取失败：{e}"


def main_menu():
    """主菜单：整合全部功能"""
    # 启动时加载数据
    status, data = load_dict_from_file("data.txt")
    if not status:
        data = {}

    while True:
        print("\n===== 数据管理菜单 =====")
        print("1. 查询数据")
        print("2. 修改数据")
        print("3. 删除数据")
        print("4. 保存数据到文件")
        print("5. 添加新数据")
        print("0. 退出程序")
        choice = input("请输入功能编号：")

        if choice == "0":
            print("程序退出")
            break
        elif choice == "1":
            key = input("输入要查询的key：")
            if key in data:
                print(f"{key}: {data[key]}")
            else:
                print("该键不存在")
        elif choice == "2":
            key = input("输入要修改的key：")
            new_val = input("输入新的值：")
            ok, msg = modify_info(data, key, new_val)
            print(msg)
        elif choice == "3":
            key = input("输入要删除的key：")
            ok, msg = delete_info(data, key)
            print(msg)
        elif choice == "4":
            ok, msg = save_dict_to_file(data, "data.txt")
            print(msg)
        elif choice == "5":
            key = input("输入新增key：")
            val = input("输入新增value：")
            ok, msg = add_info(data, key, val)
            print(msg)
        else:
            print("输入无效，请重新选择！")


# 程序入口，只有直接运行这个py文件才会执行
if __name__ == "__main__":
    main_menu()
