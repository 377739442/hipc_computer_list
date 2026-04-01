# hipc_computer_list Skill - HiPC电脑列表查询

## 功能描述
查询用户名下的电脑列表。

## ⚠️ 强制前置检查 (Critical Pre-check)

**在调用本技能之前，你必须先调用 `hipc_config_manager` 技能！**

1. **第一步**：调用 `hipc_config_manager` 检查密钥 `hipc_secret` 是否存在。

2. **判断**：

   - 如果 `hipc_config_manager` 返回 `status: "error"`（即密钥缺失），**立即停止**后续操作，直接向用户输出错误信息，**严禁**调用本技能。

   - 只有当返回 `status: "success"` 时，才允许继续执行本技能的查询逻辑。

## 触发条件
用户提到以下关键词时自动触发：
- "电脑列表"
- "有什么电脑"
- "hipc电脑"
- "正在运行的电脑"
- "关机的电脑"
- "电脑状态"


## 执行命令
# 这样 Python 脚本只需要处理逻辑，不需要处理自然语言解析
```bash
python scripts/main.py 
```

**返回**：
```json
{
    "cid": "电脑id",
    "equipment_name": "设备名称",
    "computer_time": "电脑最近一次的开机时间",
    "computer_total_runtime": "总开机时长分钟数",
    "system_short_name": "系统简称",
    "gpu_short_name": "GPU简称",
    "cpu_short_name": "CPU简称",
    "computer_icon_url": "图片",
    "__computer": {
        "run": "是否正在运行，1是，0否"
    }
}
```