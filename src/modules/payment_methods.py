class PaymentMethodsModule:
    def __init__(self, client):
        self.client = client

    def list(self, shop_id: int | str):
        """Retrieve all payment methods for a shop"""
        return self.client.request(
            method="GET",
            endpoint=f"/v1/shops/{shop_id}/payment-methods",
        )

    def get(self, shop_id: int | str, payment_method_id: int):
        """Retrieve a specific payment method"""
        return self.client.request(
            method="GET",
            endpoint=f"/v1/shops/{shop_id}/payment-methods/{payment_method_id}",
        )

    def create(self, shop_id: int | str, data: dict):
        """Create a new payment method"""
        return self.client.request(
            method="POST",
            endpoint=f"/v1/shops/{shop_id}/payment-methods",
            json=data,
        )

    def update(self, shop_id: int | str, payment_method_id: int, data: dict):
        """Update a specific payment method"""
        return self.client.request(
            method="PUT",
            endpoint=f"/v1/shops/{shop_id}/payment-methods/{payment_method_id}",
            json=data,
        )

    def delete(self, shop_id: int | str, payment_method_id: int):
        """Delete a specific payment method"""
        return self.client.request(
            method="DELETE",
            endpoint=f"/v1/shops/{shop_id}/payment-methods/{payment_method_id}",
        )

    def toggle(self, shop_id: int | str, payment_method_id: int):
        """Toggle the active status of a payment method"""
        return self.client.request(
            method="POST",
            endpoint=f"/v1/shops/{shop_id}/payment-methods/{payment_method_id}/toggle",
        )

    def update_order(self, shop_id: int | str, payment_methods: list[dict]):
        """Update the order of payment methods"""
        payload = {"paymentMethods": payment_methods}
        return self.client.request(
            method="PUT",
            endpoint=f"/v1/shops/{shop_id}/payment-methods/order",
            json=payload,
        )
