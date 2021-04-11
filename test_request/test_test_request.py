from test_request import test_request


class Test_Api:
    data = {
        "method": "get",
        "url": "http://127.0.0.1:9999/demo.txt",
        "headers": None
    }

    def test_send(self):
        api = test_request.Api()
        api.send(self.data)
