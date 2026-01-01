class CustomersModule:
    def __init__(self, client):
        self.client = client

    def list(
        self,
        shop_id: int | str,
        page: int | None = None,
        per_page: int | None = None,
        order_column: str | None = None,
        order_direction: str | None = None,
        id: str | None = None,
        email: str | None = None,
        discord_id: str | None = None,
        discord_username: str | None = None,
        subscribed: str | None = None,
    ):
        """Retrieve all customers for a shop with optional filters"""
        body = {}

        if page is not None:
            body["page"] = page
        if per_page is not None:
            body["perPage"] = per_page
        if order_column is not None:
            body["orderColumn"] = order_column
        if order_direction is not None:
            body["orderDirection"] = order_direction
        if id is not None:
            body["id"] = id
        if email is not None:
            body["email"] = email
        if discord_id is not None:
            body["discord_id"] = discord_id
        if discord_username is not None:
            body["discord_username"] = discord_username
        if subscribed is not None:
            body["subscribed"] = subscribed

        return self.client.request(
            method="GET",
            endpoint=f"/v1/shops/{shop_id}/customers",
            data=body,
        )

    def edit_balance(
        self,
        shop_id: int | str,
        customer_id: str,
        amount: float,
        description: str | None = None,
    ):
        """Add or deduct balance for a customer"""
        body = {"amount": amount}
        if description is not None:
            body["description"] = description

        return self.client.request(
            method="POST",
            endpoint=f"/v1/shops/{shop_id}/customers/{customer_id}/balance",
            data=body,
        )
