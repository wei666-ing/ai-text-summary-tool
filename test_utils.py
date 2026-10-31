"""utils 工具函数与 DataManager 类的单元测试（pytest 版）

运行方式：python -m pytest -v
特点：
- pytest 自动发现 test_ 开头的函数，不需要手动调用
- tmp_path 是 pytest 内置 fixture：每个测试自动建独立临时目录、自动清理
- @pytest.mark.parametrize 一组参数自动跑多次
"""
import os
import pytest

from utils import (
    add_info, modify_info, delete_info,
    save_json, load_json, backup_file,
    DataManager,
)


# ===== 纯逻辑函数测试 =====

def test_add_info():
    data = {}
    # 正常添加
    ok, msg = add_info(data, "name", "小明")
    assert ok is True
    assert data["name"] == "小明"
    # 重复key
    ok, msg = add_info(data, "name", "小红")
    assert ok is False
    # 空key
    ok, msg = add_info(data, "", "测试")
    assert ok is False


def test_modify_info():
    data = {"age": 20}
    ok, msg = modify_info(data, "age", 25)
    assert ok is True
    assert data["age"] == 25
    ok, msg = modify_info(data, "height", 180)
    assert ok is False
    ok, msg = modify_info(data, "", 100)
    assert ok is False


def test_delete_info():
    data = {"city": "广州"}
    ok, msg = delete_info(data, "city")
    assert ok is True
    assert "city" not in data
    ok, msg = delete_info(data, "abc")
    assert ok is False
    ok, msg = delete_info(data, "")
    assert ok is False


# ===== 文件相关测试（tmp_path：临时目录，测完自动清理）=====

def test_json_save_load(tmp_path):
    test_file = str(tmp_path / "test_temp.json")
    test_data = {"a": 1, "b": "测试"}
    ok, msg = save_json(test_data, test_file)
    assert ok is True
    assert os.path.exists(test_file)
    ok, data = load_json(test_file)
    assert ok is True
    assert data["a"] == 1
    assert data["b"] == "测试"


def test_backup_file(tmp_path):
    test_file = str(tmp_path / "test_backup.txt")
    with open(test_file, "w", encoding="utf-8") as f:
        f.write("测试内容")
    # 默认后缀
    ok, msg = backup_file(test_file)
    assert ok is True
    assert os.path.exists(test_file + ".bak")
    # 自定义后缀（**kwargs）
    ok, msg = backup_file(test_file, suffix=".backup")
    assert ok is True
    assert os.path.exists(test_file + ".backup")


# ===== DataManager 类测试 =====

def test_datamanager_crud(tmp_path):
    test_file = str(tmp_path / "test_dm.json")
    dm = DataManager(test_file)
    ok, msg = dm.add("name", "小明")
    assert ok is True
    ok, msg = dm.add("name", "小红")   # 重复拦截
    assert ok is False
    ok, msg = dm.modify("name", "小李")
    assert ok is True
    assert dm.data["name"] == "小李"
    assert dm.query("name") == "小李"
    result = dm.search("李")
    assert "name" in result
    assert "name: 小李" in dm.show_all()
    ok, msg = dm.delete("name")
    assert ok is True
    assert "name" not in dm.data
    ok, msg = dm.save()
    assert ok is True
    assert os.path.exists(test_file)


def test_datamanager_batch_add(tmp_path):
    dm = DataManager(str(tmp_path / "batch.json"))
    succ, fail = dm.batch_add("a", "1", "b", "2")
    assert len(succ) == 2
    assert len(fail) == 0
    # 奇数参数报错
    succ, fail = dm.batch_add("a", "1", "b")
    assert len(succ) == 0
    assert len(fail) == 1


# ===== 参数化测试（pytest特色：一组参数自动跑多次）=====

@pytest.mark.parametrize("key,value,expected", [
    ("", "v", False),      # 空key → 失败
    ("k", "", False),      # 空value → 失败
    ("k", "v", True),      # 正常 → 成功
])
def test_add_parametrized(tmp_path, key, value, expected):
    dm = DataManager(str(tmp_path / "param.json"))
    ok, msg = dm.add(key, value)
    assert ok is expected
