class CouponsModule:
    def __init__(self, client):
        self.client = client

    def list(self, shop_id: int | str):
        """Get all coupons"""
        return self.client.request(
            method="GET",
            endpoint=f"/v1/shops/{shop_id}/coupons",
        )

    def get(self, shop_id: int | str, coupon_id: str):
        """Get a specific coupon"""
        return self.client.request(
            method="GET",
            endpoint=f"/v1/shops/{shop_id}/coupons/{coupon_id}",
        )

    def create(
        self,
        shop_id: int | str,
        code: str,
        global_: bool,
        discount: float,
        type: str,
        disable_if_volume_discount: bool,
        max_uses: int | None = None,
        max_uses_per_customer: int | None = None,
        min_invoice_price: float | None = None,
        start_date: str | None = None,
        expiration_date: str | None = None,
        allowed_emails: list[str] | None = None,
        items: list[dict] | None = None,
    ):
        """Create a new coupon"""
        body = {
            "code": code,
            "global": global_,
            "discount": discount,
            "type": type,
            "disable_if_volume_discount": disable_if_volume_discount,
        }

        optional_fields = {
            "max_uses": max_uses,
            "max_uses_per_customer": max_uses_per_customer,
            "min_invoice_price": min_invoice_price,
            "start_date": start_date,
            "expiration_date": expiration_date,
            "allowed_emails": allowed_emails,
            "items": items,
        }

        for k, v in optional_fields.items():
            if v is not None:
                body[k] = v

        return self.client.request(
            method="POST",
            endpoint=f"/v1/shops/{shop_id}/coupons",
            data=body,
        )

    def update(
        self,
        shop_id: int | str,
        coupon_id: str,
        code: str,
        global_: bool,
        discount: float,
        type: str,
        disable_if_volume_discount: bool,
        max_uses: int | None = None,
        max_uses_per_customer: int | None = None,
        min_invoice_price: float | None = None,
        start_date: str | None = None,
        expiration_date: str | None = None,
        allowed_emails: list[str] | None = None,
        items: list[dict] | None = None,
    ):
        """Update a coupon"""
        body = {
            "code": code,
            "global": global_,
            "discount": discount,
            "type": type,
            "disable_if_volume_discount": disable_if_volume_discount,
        }

        optional_fields = {
            "max_uses": max_uses,
            "max_uses_per_customer": max_uses_per_customer,
            "min_invoice_price": min_invoice_price,
            "start_date": start_date,
            "expiration_date": expiration_date,
            "allowed_emails": allowed_emails,
            "items": items,
        }

        for k, v in optional_fields.items():
            if v is not None:
                body[k] = v

        return self.client.request(
            method="PUT",
            endpoint=f"/v1/shops/{shop_id}/coupons/{coupon_id}/update",
            data=body,
        )

    def delete(self, shop_id: int | str, coupon_id: str):
        """Delete a specific coupon"""
        return self.client.request(
            method="DELETE",
            endpoint=f"/v1/shops/{shop_id}/coupons/{coupon_id}",
        )

    def delete_used(self, shop_id: int | str):
        """Delete all used coupons"""
        return self.client.request(
            method="DELETE",
            endpoint=f"/v1/shops/{shop_id}/coupons/used",
        )
