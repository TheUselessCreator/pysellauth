class ProductsModule:
    def __init__(self, client):
        self.client = client

    def list(self, shop_id: int | str, params: dict = None):
        """Retrieve all products for a shop"""
        return self.client.request(
            method="GET",
            endpoint=f"/v1/shops/{shop_id}/products",
            json=params,
        )

    def get(self, shop_id: int | str, product_id: str):
        """Retrieve a specific product"""
        return self.client.request(
            method="GET",
            endpoint=f"/v1/shops/{shop_id}/products/{product_id}",
        )

    def create(self, shop_id: int | str, data: dict):
        """Create a new product"""
        return self.client.request(
            method="POST",
            endpoint=f"/v1/shops/{shop_id}/products",
            json=data,
        )

    def update(self, shop_id: int | str, product_id: str, data: dict):
        """Update a specific product"""
        return self.client.request(
            method="PUT",
            endpoint=f"/v1/shops/{shop_id}/products/{product_id}/update",
            json=data,
        )

    def delete(self, shop_id: int | str, product_id: str):
        """Delete a product"""
        return self.client.request(
            method="DELETE",
            endpoint=f"/v1/shops/{shop_id}/products/{product_id}",
        )

    def clone(self, shop_id: int | str, product_id: str):
        """Clone a product"""
        return self.client.request(
            method="POST",
            endpoint=f"/v1/shops/{shop_id}/products/{product_id}/clone",
        )

    def update_stock(self, shop_id: int | str, product_id: str, variant_id: str, data: dict = None):
        """Update stock count of a product variant"""
        return self.client.request(
            method="PUT",
            endpoint=f"/v1/shops/{shop_id}/products/{product_id}/stock/{variant_id}",
            json=data,
        )

    def get_deliverables(self, shop_id: int | str, product_id: str, variant_id: str):
        """Retrieve deliverables for a product or variant"""
        return self.client.request(
            method="GET",
            endpoint=f"/v1/shops/{shop_id}/products/{product_id}/deliverables/{variant_id}",
        )

    def append_deliverables(self, shop_id: int | str, product_id: str, variant_id: str, data: dict):
        """Append deliverables to a product or variant"""
        return self.client.request(
            method="PUT",
            endpoint=f"/v1/shops/{shop_id}/products/{product_id}/deliverables/append/{variant_id}",
            json=data,
        )

    def overwrite_deliverables(self, shop_id: int | str, product_id: str, variant_id: str, data: dict):
        """Overwrite deliverables for a product or variant"""
        return self.client.request(
            method="PUT",
            endpoint=f"/v1/shops/{shop_id}/products/{product_id}/deliverables/overwrite/{variant_id}",
            json=data,
        )

    def update_order(self, shop_id: int | str, sorted_ids: list[dict]):
        """Update order of products and groups"""
        return self.client.request(
            method="PUT",
            endpoint=f"/v1/shops/{shop_id}/products/sort",
            json={"sortedIds": sorted_ids},
        )

    # Bulk updates
    def bulk_update_disabled_payment_methods(self, shop_id: int | str, data: dict):
        return self.client.request(
            method="PUT",
            endpoint=f"/v1/shops/{shop_id}/products/bulk-update/disabled-payment-methods",
            json=data,
        )

    def bulk_update_custom_fields(self, shop_id: int | str, data: dict):
        return self.client.request(
            method="PUT",
            endpoint=f"/v1/shops/{shop_id}/products/bulk-update/custom-fields",
            json=data,
        )

    def bulk_update_discord_integration(self, shop_id: int | str, data: dict):
        return self.client.request(
            method="PUT",
            endpoint=f"/v1/shops/{shop_id}/products/bulk-update/discord-integration",
            json=data,
        )

    def bulk_update_description(self, shop_id: int | str, data: dict):
        return self.client.request(
            method="PUT",
            endpoint=f"/v1/shops/{shop_id}/products/bulk-update/description",
            json=data,
        )

    def bulk_update_instructions(self, shop_id: int | str, data: dict):
        return self.client.request(
            method="PUT",
            endpoint=f"/v1/shops/{shop_id}/products/bulk-update/instructions",
            json=data,
        )

    def bulk_update_out_of_stock_message(self, shop_id: int | str, data: dict):
        return self.client.request(
            method="PUT",
            endpoint=f"/v1/shops/{shop_id}/products/bulk-update/out-of-stock-message",
            json=data,
        )

    def bulk_update_security(self, shop_id: int | str, data: dict):
        return self.client.request(
            method="PUT",
            endpoint=f"/v1/shops/{shop_id}/products/bulk-update/security",
            json=data,
        )

    def bulk_update_badges(self, shop_id: int | str, data: dict):
        return self.client.request(
            method="PUT",
            endpoint=f"/v1/shops/{shop_id}/products/bulk-update/badges",
            json=data,
        )

    def bulk_update_status(self, shop_id: int | str, data: dict):
        return self.client.request(
            method="PUT",
            endpoint=f"/v1/shops/{shop_id}/products/bulk-update/status",
            json=data,
        )

    def bulk_update_visibility(self, shop_id: int | str, data: dict):
        return self.client.request(
            method="PUT",
            endpoint=f"/v1/shops/{shop_id}/products/bulk-update/visibility",
            json=data,
        )

    def bulk_update_live_stats(self, shop_id: int | str, data: dict):
        return self.client.request(
            method="PUT",
            endpoint=f"/v1/shops/{shop_id}/products/bulk-update/live-stats",
            json=data,
        )

    def bulk_update_feedback_coupon(self, shop_id: int | str, data: dict):
        return self.client.request(
            method="PUT",
            endpoint=f"/v1/shops/{shop_id}/products/bulk-update/feedback-coupon",
            json=data,
        )

    def bulk_update_volume_discounts(self, shop_id: int | str, data: dict):
        return self.client.request(
            method="PUT",
            endpoint=f"/v1/shops/{shop_id}/products/bulk-update/volume-discounts",
            json=data,
        )

    def bulk_update_redirect_url(self, shop_id: int | str, data: dict):
        return self.client.request(
            method="PUT",
            endpoint=f"/v1/shops/{shop_id}/products/bulk-update/redirect-url",
            json=data,
        )

    def bulk_update_deliverables_type(self, shop_id: int | str, data: dict):
        return self.client.request(
            method="PUT",
            endpoint=f"/v1/shops/{shop_id}/products/bulk-update/deliverables-type",
            json=data,
        )

    def bulk_update_deliverables_label(self, shop_id: int | str, data: dict):
        return self.client.request(
            method="PUT",
            endpoint=f"/v1/shops/{shop_id}/products/bulk-update/deliverables-label",
            json=data,
        )
