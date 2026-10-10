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
