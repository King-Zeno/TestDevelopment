import allure


@allure.link("http://www.baidu.com", name="链接")
def test_eith_link():
    print("这是一条加了链接的测试")
    pass


TEST_CASE_LINK = 'http://github.com/qameta/allure-integrations/issues/8#issucomment-268313637'


@allure.testcase(TEST_CASE_LINK, '登录用例')
def test_with_testcase_link():
    print("这是一条测试用例的链接，链接到测试用例")
    pass


@allure.issue('148', '这是一个issue')
def test_with_issue_link():
    pass
