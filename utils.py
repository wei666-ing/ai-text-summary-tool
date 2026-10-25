# =========================================
# utils.py：工具函数库
# 数据管理小工具的所有工具函数都放这里
# main.py 通过 import 导入这些函数
# =========================================
import os
import json


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
    if not key:
        return False, "错误：key不能为空！"
    if not new_value:
        return False, "错误：值不能为空！"
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
    """删除指定key"""
    if not key:
        return False, "错误：key不能为空！"
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


def save_json(data_dict, file_path):
    """把字典保存为json文件"""
    try:
        with open(file_path, "w", encoding="utf-8") as f:
            json.dump(data_dict, f, ensure_ascii=False, indent=2)
        return True, "json保存成功"
    except Exception as e:
        return False, f"保存失败：{e}"


def load_json(file_path):
    """读取json文件，返回字典"""
    # 先判断文件是否存在
    if not os.path.exists(file_path):
        print("提示：数据文件不存在，已自动新建空白数据")
        return True, {}

    try:
        with open(file_path, "r", encoding="utf-8") as f:
            data = json.load(f)
        return True, data
    except json.JSONDecodeError:
        print("警告：文件JSON格式损坏，使用空白数据")
        return True, {}
    except Exception as e:
        print(f"读取失败：{e}")
        return False, {}


def show_all_data(data_dict):
    """展示字典全部数据"""
    if not data_dict:
        return "暂无任何数据"
    res = ""
    for k, v in data_dict.items():
        res += f"{k}: {v}\n"
    return res
