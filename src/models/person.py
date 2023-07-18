from abc import ABC, abstractmethod


class Person(ABC):

    def __init__(self, name, surname, email, password, sex, date_of_birth):
        self.name = name
        self.surname = surname
        self.email = email
        self.password = password
        self.sex = sex
        self.date_of_birth = date_of_birth

    @abstractmethod
    def get_details(self):
        pass