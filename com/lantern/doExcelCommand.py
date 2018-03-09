from readExcelCommand import read_excel
from selenium import webdriver


class CommonClass:
    @classmethod
    def set_driver(cls, driver):
        cls.driver = driver

    @classmethod
    def get_driver(cls):
        return cls.driver


# 浏览器打开事件
def l_open_chrome(y, z):
    driver = webdriver.Chrome()
    driver.get(y)
    CommonClass().set_driver(driver)
    print('i open', y)


# 点击事件
def l_click(y, z):
    if y.split('=')[0] == 'id':
        CommonClass().get_driver().find_element_by_id(y.split('"')[1]).click()
    print('i click', y.split('"')[1])


# 输入事件
def l_input(y, z):
    if y.split('=')[0] == 'id':
        CommonClass().get_driver().find_element_by_id(y.split('"')[1]).send_keys(z)
    print('i input', y.split('"')[1])


def switch(x, y, z):
    return action_map.get(x)(y, z)


def do_close():
    CommonClass().get_driver().close()
    print('i close')


def do_by_selenium():

    actions = read_excel()
    # 获取动作标志 用于后续动作处理
    # action_title = actions[0]

    # 获取指令
    for action in actions[1:]:
        switch(action[3], action[4], action[5])


action_map = {'open chrome': l_open_chrome,
              'click': l_click,
              'input' : l_input}

if __name__ == '__main__':
    try:
        do_by_selenium()
    except Exception as e:
        print(e)
    finally:
        do_close()

