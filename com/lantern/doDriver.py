class CommonClass:
    @classmethod
    def set_driver(cls, driver):
        cls.driver = driver

    @classmethod
    def get_driver(cls):
        return cls.driver
