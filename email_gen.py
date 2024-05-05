import random

class EmailGeniration:
    @staticmethod
    def email_generation():
        email = "antonkazantcev05" + str(random.randint(1, 999)) + "yandex.ru"
        return email