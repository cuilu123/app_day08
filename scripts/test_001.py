import allure
import pytest

class Test_allure:
    @pytest.allure.severity(pytest.allure.severity_level.BLOCKER)
    @allure.step(title="这是一个测试步骤1")
    def test_00l(self):
        print("test_001_1")
        allure.attach("标题", "具体内容")
        assert True

    @pytest.allure.severity(pytest.allure.severity_level.CRITICAL)
    @allure.step(title="这是一个测试步骤2")
    def test_002(self):
        print("test_001_2")
        allure.attach("用户名","张三")
        allure.attach("密码", "123456")
        assert False

    @pytest.allure.severity(pytest.allure.severity_level.NORMAL)
    @allure.step(title="这是一个测试步骤03")
    def test_003(self):
        print("test_001_3")
        assert True

    @pytest.allure.severity(pytest.allure.severity_level.MINOR)
    @allure.step(title="这是一个测试步骤04")
    def test_004(self):
        print("test_001_4")
        assert True

    @pytest.allure.severity(pytest.allure.severity_level.TRIVIAL)
    @allure.step(title="这是一个测试步骤05")
    def test_005(self):
        print("test_001_5")
        assert True

