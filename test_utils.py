import os
import json
from utils import (
    add_info, modify_info, delete_info,
    save_json, load_json, show_all_data,
    backup_file
)

def test_add_info():
    data = {}
    # 正常添加
    ok, msg = add_info(data, "name", "小明")
    assert ok == True
    assert data["name"] == "小明"
    # 重复key
    ok, msg = add_info(data, "name", "小红")
    assert ok == False
    # 空key
    ok, msg = add_info(data, "", "测试")
    assert ok == False
    print("✅ add_info 测试通过")

def test_modify_info():
    data = {"age": 20}
    # 正常修改
    ok, msg = modify_info(data, "age", 25)
    assert ok == True
    assert data["age"] == 25
    # 不存在的key
    ok, msg = modify_info(data, "height", 180)
    assert ok == False
    # 空key
    ok, msg = modify_info(data, "", 100)
    assert ok == False
    print("✅ modify_info 测试通过")

def test_delete_info():
    data = {"city": "广州"}
    # 正常删除
    ok, msg = delete_info(data, "city")
    assert ok == True
    assert "city" not in data
    # 删除不存在的key
    ok, msg = delete_info(data, "abc")
    assert ok == False
    # 空key
    ok, msg = delete_info(data, "")
    assert ok == False
    print("✅ delete_info 测试通过")

def test_json_save_load():
    test_file = "test_temp.json"
    test_data = {"a": 1, "b": "测试"}
    # 保存
    ok, msg = save_json(test_data, test_file)
    assert ok == True
    assert os.path.exists(test_file)
    # 读取
    ok, data = load_json(test_file)
    assert ok == True
    assert data["a"] == 1
    assert data["b"] == "测试"
    # 清理
    os.remove(test_file)
    print("✅ json 保存读取 测试通过")

def test_backup_file():
    test_file = "test_backup.txt"
    with open(test_file, "w", encoding="utf-8") as f:
        f.write("测试内容")
    # 正常备份
    ok, msg = backup_file(test_file)
    assert ok == True
    assert os.path.exists(test_file + ".bak")
    # 清理
    os.remove(test_file)
    os.remove(test_file + ".bak")
    print("✅ backup_file 测试通过")

if __name__ == "__main__":
    print("开始运行工具函数测试...\n")
    test_add_info()
    test_modify_info()
    test_delete_info()
    test_json_save_load()
    test_backup_file()
    print("\n🎉 全部测试通过！")
