from src.clients.base_client import BaseClient


class UsersClient(BaseClient):
    def get_all_users(self):
        return self.get("/users")

    def get_single_user(self, user_id: int):
        return self.get(f"/users/{user_id}")

    def create_user(self, payload: dict):
        return self.post("/users/add", json=payload)

    def update_user_put(self, user_id: int, payload: dict):
        return self.put(f"/users/{user_id}", json=payload)

    def update_user_patch(self, user_id: int, payload: dict):
        return self.patch(f"/users/{user_id}", json=payload)

    def delete_user(self, user_id: int):
        return self.delete(f"/users/{user_id}")