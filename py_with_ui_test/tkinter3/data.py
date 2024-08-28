import pandas as pd
from typing import List, Dict
from exceptions import UserNotFoundError, PermissionError

class UserData:
    def __init__(self) -> None:
        self.users = pd.DataFrame([
            {"id": "123456", "name": "Alice", "username": "alice123", "email": "alice@example.com", "role": "Admin", "enabled": True, "permissions": ["read", "write"]},
            {"id": "234567", "name": "Bob", "username": "bob234", "email": "bob@example.com", "role": "User", "enabled": False, "permissions": ["read"]},
            {"id": "345678", "name": "Charlie", "username": "charlie345", "email": "charlie@example.com", "role": "Manager", "enabled": True, "permissions": ["write"]}
        ])

    def search_users(self, search_value: str) -> List[Dict[str, any]]:
        try:
            filtered_df = self.users[
                self.users["name"].str.contains(search_value, case=False) |
                self.users["username"].str.contains(search_value, case=False) |
                self.users["id"].str.contains(search_value) |
                self.users["email"].str.contains(search_value, case=False) |
                self.users["role"].str.contains(search_value, case=False)
            ]
            return filtered_df.to_dict(orient="records")
        except Exception as e:
            print(f"Error searching users: {e}")
            return []

    def get_permissions(self, user_id: str) -> List[str]:
        try:
            user_row = self.users.loc[self.users["id"] == user_id]
            if user_row.empty:
                raise UserNotFoundError(f"User with ID {user_id} not found.")
            return user_row.iloc[0]["permissions"]
        except Exception as e:
            print(f"Error getting permissions: {e}")
            return []

    def add_permission(self, user_id: str, permission: str) -> None:
        try:
            index = self.users.index[self.users["id"] == user_id].tolist()
            if not index:
                raise UserNotFoundError(f"User with ID {user_id} not found.")
            current_permissions = self.users.at[index[0], "permissions"]
            if permission in current_permissions:
                raise PermissionError(f"Permission '{permission}' already exists for user {user_id}.")
            current_permissions.append(permission)
            self.users.at[index[0], "permissions"] = current_permissions
        except Exception as e:
            print(f"Error adding permission: {e}")

    def remove_permission(self, user_id: str, permission: str) -> None:
        try:
            index = self.users.index[self.users["id"] == user_id].tolist()
            if not index:
                raise UserNotFoundError(f"User with ID {user_id} not found.")
            current_permissions = self.users.at[index[0], "permissions"]
            if permission not in current_permissions:
                raise PermissionError(f"Permission '{permission}' not found for user {user_id}.")
            current_permissions.remove(permission)
            self.users.at[index[0], "permissions"] = current_permissions
        except Exception as e:
            print(f"Error removing permission: {e}")
