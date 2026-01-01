class GroupsModule:
    def __init__(self, client):
        self.client = client

    def list(self, shop_id: int | str):
        """Retrieve all groups for a shop"""
        return self.client.request(
            method="GET",
            endpoint=f"/v1/shops/{shop_id}/groups",
        )

    def create(
        self,
        shop_id: int | str,
        name: str,
        visibility: str,
        products: list[str],
        image_id: str = None,
        badge_color: str = None,
        badge_text: str = None,
    ):
        """Create a new group"""
        data = {
            "name": name,
            "visibility": visibility,
            "products": products,
            "image_id": image_id,
            "badge_color": badge_color,
            "badge_text": badge_text,
        }
        return self.client.request(
            method="POST",
            endpoint=f"/v1/shops/{shop_id}/groups",
            data=data,
        )

    def get(self, shop_id: int | str, group_id: str):
        """Retrieve a specific group"""
        return self.client.request(
            method="GET",
            endpoint=f"/v1/shops/{shop_id}/groups/{group_id}",
        )

    def update(
        self,
        shop_id: int | str,
        group_id: str,
        name: str,
        visibility: str,
        products: list[str],
        image_id: str = None,
        badge_color: str = None,
        badge_text: str = None,
    ):
        """Update a specific group"""
        data = {
            "name": name,
            "visibility": visibility,
            "products": products,
            "image_id": image_id,
            "badge_color": badge_color,
            "badge_text": badge_text,
        }
        return self.client.request(
            method="PUT",
            endpoint=f"/v1/shops/{shop_id}/groups/{group_id}/update",
            data=data,
        )

    def delete(self, shop_id: int | str, group_id: str):
        """Delete a specific group"""
        return self.client.request(
            method="DELETE",
            endpoint=f"/v1/shops/{shop_id}/groups/{group_id}",
        )
