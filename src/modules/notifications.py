class NotificationsModule:
    def __init__(self, client):
        self.client = client

    def get_latest(self, shop_id: int | str):
        """Retrieve the latest notifications for a shop"""
        return self.client.request(
            method="GET",
            endpoint=f"/v1/shops/{shop_id}/notifications/latest",
        )

    def get_page(self, shop_id: int | str):
        """Retrieve a paginated list of notifications"""
        return self.client.request(
            method="GET",
            endpoint=f"/v1/shops/{shop_id}/notifications/page",
        )

    def mark_as_read(self, shop_id: int | str):
        """Mark all notifications as read"""
        return self.client.request(
            method="POST",
            endpoint=f"/v1/shops/{shop_id}/notifications/mark-as-read",
        )

    def get_settings(self, shop_id: int | str):
        """Retrieve notification settings for a shop"""
        return self.client.request(
            method="GET",
            endpoint=f"/v1/shops/{shop_id}/notifications/settings",
        )

    def update_settings(self, shop_id: int | str, settings: dict):
        """Update notification settings for a shop"""
        return self.client.request(
            method="POST",
            endpoint=f"/v1/shops/{shop_id}/notifications/settings",
            json=settings,
        )
