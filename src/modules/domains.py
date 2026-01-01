class DomainsModule:
    def __init__(self, client):
        self.client = client

    def list(self, shop_id: int | str):
        """Retrieve all domains for a shop"""
        return self.client.request(
            method="GET",
            endpoint=f"/v1/shops/{shop_id}/domains",
        )

    def create(self, shop_id: int | str, domain_name: str):
        """Create a new domain for the shop"""
        return self.client.request(
            method="POST",
            endpoint=f"/v1/shops/{shop_id}/domains",
            data={"domain": domain_name},
        )

    def get(self, shop_id: int | str, domain_id: int | str):
        """Retrieve a specific domain by its ID"""
        return self.client.request(
            method="GET",
            endpoint=f"/v1/shops/{shop_id}/domains/{domain_id}",
        )

    def delete(self, shop_id: int | str, domain_id: int | str):
        """Delete a specific domain by its ID"""
        return self.client.request(
            method="DELETE",
            endpoint=f"/v1/shops/{shop_id}/domains/{domain_id}",
        )
