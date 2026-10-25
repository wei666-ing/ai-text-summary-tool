# =========================================
# utils.py：工具函数库
# 数据管理小工具的所有工具函数都放这里
# main.py 通过 import 导入这些函数
# =========================================
import os
import json
import shutil

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
    """新增一条键值对（key/value不能为空，key不能重复）"""
    if not key:
        return False, "错误：key不能为空！"
    if not value:
        return False, "错误：值不能为空！"
    if key in data_dict:
        return False, "键已经存在，不能重复添加"
    data_dict[key] = value
    return True, "新增记录成功"


def batch_add(data_dict, *args):
    """
    批量新增数据
    args 格式要求：key1,val1,key2,val2,key3,val3……成对传入
    返回：成功信息列表、失败信息列表
    """
    success_list = []
    fail_list = []
    if len(args) % 2 != 0:
        fail_list.append("参数数量不对，必须成对：key,value,key,value...")
        return success_list, fail_list
    for i in range(0, len(args), 2):
        k = args[i]
        v = args[i + 1]
        ok, msg = add_info(data_dict, k, v)
        if ok:
            success_list.append(f"{k}:{v}")
        else:
            fail_list.append(f"{k}:{v} → {msg}")
    return success_list, fail_list


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
    """把字典保存为json文件，保存前自动备份"""
    # 先备份旧文件
    if os.path.exists(file_path):
        ok, msg = backup_file(file_path)
        if not ok:
            print(msg)

    try:
        with open(file_path, "w", encoding="utf-8") as f:
            json.dump(data_dict, f, ensure_ascii=False, indent=2)
        return True, "json保存成功（已自动备份）"
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

def list_all_files(folder_path):
    """列出文件夹里所有文件和子目录"""
    try:
        file_list = os.listdir(folder_path)
        return True, file_list
    except Exception as e:
        return False, f"读取目录失败：{e}"

def backup_file(file_path, **kwargs):
    """备份文件
    kwargs里面可以传 suffix 自定义备份后缀，默认 .bak
    """
    suffix = kwargs.get("suffix", ".bak")
    if not os.path.exists(file_path):
        return False, "源文件不存在，无需备份"
    try:
        backup_path = file_path + suffix
        shutil.copy(file_path, backup_path)
        return True, f"备份成功，副本：{backup_path}"
    except Exception as e:
        return False, f"备份失败：{e}"
    
def find_data(data_dict, keyword):
    """按关键词搜索，返回所有value包含关键词的条目（字典推导式）"""
    if not keyword:
        return {}
    return {k: v for k, v in data_dict.items() if keyword in v}


class DataManager:
    """数据管理器：把数据文件操作封装成类
    用法：
        dm = DataManager("data.json")   # 创建对象，自动加载数据
        dm.add("name", "小明")           # 添加
        dm.show_all()                    # 展示全部
        dm.save()                        # 保存到文件
    """

    def __init__(self, file_path):
        self.file_path = file_path   # 数据文件路径，存在对象身上
        self.data = {}               # 内存中的数据
        self._load()                 # 初始化时自动加载

    def _load(self):
        """内部方法：加载文件（前面加_表示"内部用，不对外"）"""
        if not os.path.exists(self.file_path):
            print("提示：数据文件不存在，已自动新建空白数据")
            return
        try:
            with open(self.file_path, "r", encoding="utf-8") as f:
                self.data = json.load(f)
        except json.JSONDecodeError:
            print("警告：文件JSON格式损坏，使用空白数据")
        except Exception as e:
            print(f"读取失败：{e}")

    def add(self, key, value):
        """新增一条键值对（key/value不能为空，key不能重复）"""
        if not key:
            return False, "错误：key不能为空！"
        if not value:
            return False, "错误：值不能为空！"
        if key in self.data:
            return False, "键已经存在，不能重复添加"
        self.data[key] = value
        return True, "新增记录成功"

    def batch_add(self, *args):
        """批量新增：args成对传入 key1,val1,key2,val2..."""
        success_list = []
        fail_list = []
        if len(args) % 2 != 0:
            fail_list.append("参数数量不对，必须成对：key,value,key,value...")
            return success_list, fail_list
        for i in range(0, len(args), 2):
            ok, msg = self.add(args[i], args[i + 1])
            if ok:
                success_list.append(f"{args[i]}:{args[i + 1]}")
            else:
                fail_list.append(f"{args[i]}:{args[i + 1]} → {msg}")
        return success_list, fail_list

    def modify(self, key, new_value):
        """修改已有键的值"""
        if not key:
            return False, "错误：key不能为空！"
        if not new_value:
            return False, "错误：值不能为空！"
        if key not in self.data:
            return False, "键不存在，无法修改"
        self.data[key] = new_value
        return True, "修改成功"

    def delete(self, key):
        """删除指定key"""
        if not key:
            return False, "错误：key不能为空！"
        if key not in self.data:
            return False, "键不存在，无法删除"
        del self.data[key]
        return True, "删除成功"

    def query(self, key):
        """查询单个key，不存在返回None"""
        return self.data.get(key, None)

    def search(self, keyword):
        """按关键词搜索value，返回新字典（字典推导式）"""
        if not keyword:
            return {}
        return {k: v for k, v in self.data.items() if keyword in v}

    def show_all(self):
        """展示全部数据"""
        if not self.data:
            return "暂无任何数据"
        return "\n".join([f"{k}: {v}" for k, v in self.data.items()])

    def save(self):
        """保存到文件，保存前自动备份"""
        if os.path.exists(self.file_path):
            backup_path = self.file_path + ".bak"
            shutil.copy(self.file_path, backup_path)
        try:
            with open(self.file_path, "w", encoding="utf-8") as f:
                json.dump(self.data, f, ensure_ascii=False, indent=2)
            return True, "json保存成功（已自动备份）"
        except Exception as e:
            return False, f"保存失败：{e}"

    def list_files(self, folder_path):
        """列出文件夹里所有文件和子目录"""
        try:
            return True, os.listdir(folder_path)
        except Exception as e:
            return False, f"读取目录失败：{e}"
