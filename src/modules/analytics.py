class AnalyticsModule:
    def __init__(self, client):
        self.client = client

    def get(self, shop_id: int | str):
        """
        Retrieves revenue, orders and customers analytics in a given timeframe.

        GET /v1/shops/{shopId}/analytics
        """
        return self.client.request(
            method="GET",
            endpoint=f"/v1/shops/{shop_id}/analytics",
        )

    def graph(self, shop_id: int | str):
        """
        Retrieves graphable analytics data.

        GET /v1/shops/{shop_id}/analytics/graph
        """
        return self.client.request(
            method="GET",
            endpoint=f"/v1/shops/{shop_id}/analytics/graph",
        )

    def top_products(self, shop_id: int | str):
        """
        Retrieves the top 5 products by revenue.

        GET /v1/shops/{shop_id}/analytics/top-products
        """
        return self.client.request(
            method="GET",
            endpoint=f"/v1/shops/{shop_id}/analytics/top-products",
        )

    def top_customers(self, shop_id: int | str):
        """
        Retrieves the top 5 customers by revenue.

        GET /v1/shops/{shop_id}/analytics/top-customers
        """
        return self.client.request(
            method="GET",
            endpoint=f"/v1/shops/{shop_id}/analytics/top-customers",
        )
