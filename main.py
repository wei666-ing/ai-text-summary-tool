def read_file_to_dict(file_path):
    # 创建空字典，用来存放解析出来的数据
    data_dict = {}
    try:
        # 打开文件，utf-8编码读取
        with open(file_path, "r", encoding="utf-8") as f:
            # 读取所有行
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
        # 读取解析完成，返回字典
        return data_dict
    except FileNotFoundError:
        # 文件找不到的时候触发
        print("文件不存在！")
        return None
    except ValueError:
        # 某一行没有等号，分割失败触发
        print("该行格式错误，需要 key=value")
        return None

# 程序入口，只有直接运行这个py文件才会执行
if __name__ == "__main__":
    # 读取同目录下的 info.txt
    res = read_file_to_dict("info.txt")
    print(res)
def read_file_to_dict(file_path):
    # 创建空字典，用来存放解析出来的数据
    data_dict = {}
    try:
        # 打开文件，utf-8编码读取
        with open(file_path, "r", encoding="utf-8") as f:
            # 读取所有行
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
        # 读取解析完成，返回字典
        return data_dict
    except FileNotFoundError:
        # 文件找不到的时候触发
        print("文件不存在！")
        return None
    except ValueError:
        # 某一行没有等号，分割失败触发
        print("该行格式错误，需要 key=value")
        return None

# 新增：根据key查询字典的值
def get_value(data_dict, key):
    if key in data_dict:
        return data_dict[key]
    else:
        return "该键不存在"

# 程序入口，只有直接运行这个py文件才会执行
if __name__ == "__main__":
    # 读取同目录下的 info.txt
    res = read_file_to_dict("info.txt")
    if res:
        print(get_value(res, "name"))
        print(get_value(res, "hobby"))
def modify_info(data_dict, key, new_value):
    if key in data_dict:
        data_dict[key] = new_value
        return True, "修改成功"
    else:
        return False, "键不存在，无法修改"
info = {"name":"小明","age":18}
status, msg = modify_info(info, "height", 180)
print(msg)
print(info)
def delete_info(data_dict, key):
    if key in data_dict:
        del data_dict[key]
        return True, "删除成功"
    else:
        return False, "键不存在，无法删除"
# 删除功能测试
info_test = {"name":"小明","age":18,"city":"广州"}
status, msg = delete_info(info_test, "city")
print(msg)
print(info_test)

# 测试删除不存在的key
status2, msg2 = delete_info(info_test, "height")
print(msg2)
print(info_test)
def save_dict_to_file(data_dict, file_path):
    try:
        with open(file_path, "w", encoding="utf-8") as f:
            # 遍历字典，一行一条写入
            for k, v in data_dict.items():
                f.write(f"{k}:{v}\n")
        return True, "保存成功"
    except Exception as e:
        return False, f"保存失败：{e}"
# 保存文件测试
save_data = {"name":"小明","age":18,"city":"广州"}
status, msg = save_dict_to_file(save_data, "data.txt")
print(msg)


