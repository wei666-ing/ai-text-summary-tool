def read_text_file(file_path):
    """读取txt文件，返回文件文本内容"""
    with open(file_path,"r",encoding="utf-8") as f:
        content = f.read()
    return content

# 调用函数
if __name__ == "__main__":
    text = read_text_file("test.txt")
    print(text)
