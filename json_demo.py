import json

# 1. Python字典（模拟API请求参数）
request_data = {
    "model": "gpt-demo",
    "prompt": "帮我总结下面这段文字",
    "content": "人工智能正在快速发展，Python是常用开发语言。"
}

print("Python字典：")
print(request_data)
print(type(request_data))

# 2. 字典转json字符串（发给API接口）
json_str = json.dumps(request_data, ensure_ascii=False)
print("\n转为JSON字符串：")
print(json_str)
print(type(json_str))

# 3. json字符串转回Python字典（接收API返回结果）
back_dict = json.loads(json_str)
print("\nJSON转回字典：")
print(back_dict)
print(type(back_dict))
# 读取字典里面的值
print("\n取出content字段：", back_dict["content"])

