# 按 Shift+F10 执行或将其替换为您的代码。
# 按 双击 Shift 在所有地方搜索类、文件、工具窗口、操作和设置。
import os
from http.client import responses

import requests
import json


class Computer:

    def __init__(self):
        # 获取当前脚本所在的目录
        baseDir = os.path.expanduser("~")
        # 拼接出配置文件的绝对路径
        configFile = os.path.join(baseDir, "hipc_config.json")
        if os.path.exists(configFile):
            with open(configFile, 'r', encoding='utf-8') as f:
                data = json.load(f)
                self.host = data["host"]
                self.token = data["hipc_secret"]
        else:
            raise FileNotFoundError(configFile)

    def curl_post(self, url):
        try:
            response = requests.post(
                url=url,
                headers={
                    "Content-Type": "application/json",
                    "token": self.token,
                    "source": 'agent',
                },
                json={
                    "order_field": "computer_time",
                    "order_type": "desc"
                })
            if response.ok:
                res = response.json()
                if res["code"] == 100:
                    return res['data']  # 返回解析后的 JSON 数据
                else:
                    raise ValueError(res["message"])
            else:
                return {"error": f"HTTP {response.status_code}", "detail": response.text}
        except ValueError as e:
            return {"error": "SYSTEM ERROR", "detail": str(e)}
        except requests.exceptions.ConnectionError as e:
            return {"error": "Network Error", "detail": str(e)}

    def get_list(self):
        url = f"https://{self.host}/v1/userequipment/get_list"
        res = self.curl_post(url)
        return res


# 按装订区域中的绿色按钮以运行脚本。
if __name__ == '__main__':
    try:
        computer = Computer()
        res =computer.get_list()
        print(res)
    except FileNotFoundError as e:
        print({"error": "配置文件不存在，请是用 hipc_config_manager 技能设置", "detail": str(e)})

# 访问 https://www.jetbrains.com/help/pycharm/ 获取 PyCharm 帮助
