class BlacklistModule:
    def __init__(self, client):
        self.client = client

    def list(self, shop_id: int | str):
        return self.client.request(
            method="GET",
            endpoint=f"/v1/shops/{shop_id}/blacklist",
        )

    def create(
        self,
        shop_id: int | str,
        value: str,
        type: str,
        match_type: str,
        reason: str | None = None,
    ):
        body = {
            "value": value,
            "type": type,
            "match_type": match_type,
        }

        if reason is not None:
            body["reason"] = reason

        return self.client.request(
            method="POST",
            endpoint=f"/v1/shops/{shop_id}/blacklist",
            data=body,
        )

    def get(self, shop_id: int | str, blacklist_id: str):
        return self.client.request(
            method="GET",
            endpoint=f"/v1/shops/{shop_id}/blacklist/{blacklist_id}",
        )

    def delete(self, shop_id: int | str, blacklist_id: str):
        return self.client.request(
            method="DELETE",
            endpoint=f"/v1/shops/{shop_id}/blacklist/{blacklist_id}",
        )

    def update(
        self,
        shop_id: int | str,
        blacklist_id: str,
        value: str,
        type: str,
        match_type: str,
        reason: str | None = None,
    ):
        body = {
            "value": value,
            "type": type,
            "match_type": match_type,
        }

        if reason is not None:
            body["reason"] = reason

        return self.client.request(
            method="PUT",
            endpoint=f"/v1/shops/{shop_id}/blacklist/{blacklist_id}/update",
            data=body,
        )
