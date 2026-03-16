from faker import Faker


class PayloadBuilder:
    def __init__(self) -> None:
        self.fake = Faker()

    def build_user_payload(self) -> dict:
        return {
            "firstName": self.fake.first_name(),
            "lastName": self.fake.last_name(),
            "age": self.fake.random_int(min=18, max=65),
            "email": self.fake.email(),
            "phone": self.fake.phone_number(),
        }

    def build_login_payload(self) -> dict:
        return {
            "username": "emilys",
            "password": "emilyspass",
        }

    def build_partial_user_payload(self) -> dict:
        return {
            "firstName": self.fake.first_name(),
        }