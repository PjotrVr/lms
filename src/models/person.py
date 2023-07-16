from abc import ABC, abstractmethod


class Person(ABC):

    def __init__(self, name, surname, email, password):
        self.name = name
        self.surname = surname
        self.email = email

    @abstractmethod
    def get_details(self):
        pass