import requests
import json


class TestWeworkAccess:
    def test_get_token1(self):
        corpid = "ww26bf94849a402142"
        corpsecret = "jQANeZEIjOQjfqnlWoEt4kQ6lEeltfgZC0dGAUqId80"
        corpsecret1 = "3gQ87rLMSkpRdPg3Gyw1fyZIjR5D9jmwednSJ-dOxYA"
        res = requests.get(f"https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid={corpid}&corpsecret={corpsecret}")
        # print(res.text)
        try:
            return res.json()['access_token']
        except Exception as e:
            raise ValueError("requests token error")

    def test_get_token(self):
        params = {"corpid": "ww26bf94849a402142",
                  "corpsecret": "jQANeZEIjOQjfqnlWoEt4kQ6lEeltfgZC0dGAUqId80"}

        res = requests.get(f"https://qyapi.weixin.qq.com/cgi-bin/gettoken", params=params)
        # print(res.text)
        try:
            return res.json()['access_token']
        except Exception as e:
            raise ValueError("requests token error")

    def test_add(self):
        data = {
            "userid": "zhangsan1",
            "name": "张三1",
            "mobile": "13800000001",
            "department": [1]
        }
        data2 = {
            "userid": "zhangsan2",
            "name": "张三2",
            "alias": "jackzhang",
            "mobile": "+86 13800000002",
            "department": [1, 2],
            "order": [10, 40],
            "position": "产品经理",
            "gender": "1",
            "email": "zhangsan@gzdev.com",
            "is_leader_in_dept": [1, 0],
            "enable": 1,
            "avatar_mediaid": "2-G6nrLmr5EC3MNb_-zL1dDdzkd0p7cNliYu9V5w7o8K0",
            "telephone": "020-123456",
            "address": "广州市海珠区新港中路",
            "main_department": 1,
            "extattr": {
                "attrs": [
                    {
                        "type": 0,
                        "name": "文本名称",
                        "text": {
                            "value": "文本"
                        }
                    },
                    {
                        "type": 1,
                        "name": "网页名称",
                        "web": {
                            "url": "http://www.test.com",
                            "title": "标题"
                        }
                    }
                ]
            },
            "to_invite": "true",
            "external_position": "高级产品经理",
            "external_profile": {
                "external_corp_name": "企业简称",
                "external_attr": [
                    {
                        "type": 0,
                        "name": "文本名称",
                        "text": {
                            "value": "文本"
                        }
                    },
                    {
                        "type": 1,
                        "name": "网页名称",
                        "web": {
                            "url": "http://www.test.com",
                            "title": "标题"
                        }
                    },
                    {
                        "type": 2,
                        "name": "测试app",
                        "miniprogram": {
                            "appid": "wx8bd8012614784fake",
                            "pagepath": "/index",
                            "title": "my miniprogram"
                        }
                    }
                ]
            }
        }

        res = requests.post(f"https://qyapi.weixin.qq.com/cgi-bin/user/create?access_token={self.test_get_token()}",
                            json=data2)
        print(res.text)

    def test_get(self):
        params = {
            "access_token": self.test_get_token(),
            "userid": "zhangsan"
        }

        res = requests.get("https://qyapi.weixin.qq.com/cgi-bin/user/get",
                           params=params)
        print(res.json())

    def test_update(self):
        data = {
            "userid": "zhangsan",
            "name": "wangwu"
        }

        res = requests.post(f"https://qyapi.weixin.qq.com/cgi-bin/user/update?access_token={self.test_get_token()}",
                            json=data)
        print(res.json())

    def test_delete(self):
        params = {
            "userid": "zhangsan",
            "access_token": self.test_get_token()
        }

        res = requests.get("https://qyapi.weixin.qq.com/cgi-bin/user/delete",
                           params=params)

        print(res.json())
