class ImagesModule:
    def __init__(self, client):
        self.client = client

    def list(self, shop_id: int | str):
        """Retrieve all images for a shop"""
        return self.client.request(
            method="GET",
            endpoint=f"/v1/shops/{shop_id}/images",
        )

    def upload(self, shop_id: int | str, image_path: str):
        """Upload a new image"""
        with open(image_path, "rb") as f:
            files = {"image": f}
            return self.client.request(
                method="POST",
                endpoint=f"/v1/shops/{shop_id}/images",
                files=files,
            )

    def delete(self, shop_id: int | str, image_id: str):
        """Delete a specific image"""
        return self.client.request(
            method="DELETE",
            endpoint=f"/v1/shops/{shop_id}/images/{image_id}",
        )
