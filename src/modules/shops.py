class ShopsModule:
    def __init__(self, client):
        self.client = client

    def list(self):
        """Retrieve all shops."""
        return self.client.request(
            method="GET",
            endpoint="/v1/shops"
        )

    def create(self, name: str, subdomain: str, logo: str = None):
        """Create a new shop. Logo is optional (file path)."""
        data = {"name": name, "subdomain": subdomain}
        files = {"logo": logo} if logo else None
        return self.client.request(
            method="POST",
            endpoint="/v1/shops/create",
            data=data,
            files=files
        )

    def get(self, shop_id: int | str):
        """Retrieve a specific shop."""
        return self.client.request(
            method="GET",
            endpoint=f"/v1/shops/{shop_id}"
        )

    def update(self, shop_id: int | str, **kwargs):
        """Update a specific shop. Pass any allowed parameters as kwargs."""
        return self.client.request(
            method="PUT",
            endpoint=f"/v1/shops/{shop_id}/update",
            data=kwargs
        )

    def delete(self, shop_id: int | str, name: str, password: str):
        """Delete a specific shop."""
        return self.client.request(
            method="DELETE",
            endpoint=f"/v1/shops/{shop_id}",
            data={"name": name, "password": password}
        )

    def stats(self, shop_id: int | str):
        """Retrieve shop statistics."""
        return self.client.request(
            method="GET",
            endpoint=f"/v1/shops/{shop_id}/stats"
        )
