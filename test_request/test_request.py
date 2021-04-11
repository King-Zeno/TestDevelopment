import requests
import yaml


class Api:
    env = yaml.safe_load(open("env.yaml"))

    def send(self, data: dict):
        # 替换
        data["url"] = str(data["url"]).replace(data["url"], self.env["testing-studio"][self.env["default"]])
        # .replace("testing-studio", self.env["testing-studio"][self.env["default"]])
        data["url"] = "123"
        res = requests.request(data["method"], data["url"], headers=data["headers"])
        return res
