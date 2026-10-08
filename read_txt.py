def read_text_file(file_path):
    """读取txt文件，返回文件文本内容"""
    try:
        with open(file_path,"r",encoding="utf-8") as f:
            content = f.read()
        return content
    except FileNotFoundError:
        print(f"错误：找不到文件 {file_path}")
        return None
    except Exception as e:
        print(f"读取文件出错：{e}")
        return None

if __name__ == "__main__":
    text = read_text_file("test.txt")
    if text:
        print(text)
