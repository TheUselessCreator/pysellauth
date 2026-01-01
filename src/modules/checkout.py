class CheckoutModule:
    def __init__(self, client):
        self.client = client

    def create(
        self,
        shop_id: int | str,
        cart: list[dict],
        ip: str | None = None,
        country_code: str | None = None,
        user_agent: str | None = None,
        asn: int | None = None,
        email: str | None = None,
        discord_user_id: str | None = None,
        discord_user_username: str | None = None,
        discord_access_token: str | None = None,
        discord_refresh_token: str | None = None,
        coupon: str | None = None,
        gateway: str | None = None,
        newsletter: bool | None = None,
        affiliate: str | None = None,
    ):
        """
        Create a new checkout session for the shop.
        POST /v1/shops/{shop_id}/checkout
        """
        body = {
            "cart": cart,
        }

        optional_fields = {
            "ip": ip,
            "country_code": country_code,
            "user_agent": user_agent,
            "asn": asn,
            "email": email,
            "discord_user_id": discord_user_id,
            "discord_user_username": discord_user_username,
            "discord_access_token": discord_access_token,
            "discord_refresh_token": discord_refresh_token,
            "coupon": coupon,
            "gateway": gateway,
            "newsletter": newsletter,
            "affiliate": affiliate,
        }

        for key, value in optional_fields.items():
            if value is not None:
                body[key] = value

        return self.client.request(
            method="POST",
            endpoint=f"/v1/shops/{shop_id}/checkout",
            data=body,
        )
