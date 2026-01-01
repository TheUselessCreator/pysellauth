class InvoicesModule:
    def __init__(self, client):
        self.client = client

    def list(self, shop_id: int | str, params: dict = None):
        """Retrieve all invoices for a shop with optional filters"""
        return self.client.request(
            method="GET",
            endpoint=f"/v1/shops/{shop_id}/invoices",
            json=params,
        )

    def get(self, shop_id: int | str, invoice_id: str):
        """Retrieve a specific invoice"""
        return self.client.request(
            method="GET",
            endpoint=f"/v1/shops/{shop_id}/invoices/{invoice_id}",
        )

    def archive(self, shop_id: int | str, invoice_id: str):
        """Mark an invoice as archived"""
        return self.client.request(
            method="POST",
            endpoint=f"/v1/shops/{shop_id}/invoices/{invoice_id}/archive",
        )

    def unarchive(self, shop_id: int | str, invoice_id: str):
        """Mark an invoice as unarchived"""
        return self.client.request(
            method="POST",
            endpoint=f"/v1/shops/{shop_id}/invoices/{invoice_id}/unarchive",
        )

    def cancel(self, shop_id: int | str, invoice_id: str):
        """Cancel an invoice"""
        return self.client.request(
            method="POST",
            endpoint=f"/v1/shops/{shop_id}/invoices/{invoice_id}/cancel",
        )

    def refund(self, shop_id: int | str, invoice_id: str):
        """Refund an invoice"""
        return self.client.request(
            method="POST",
            endpoint=f"/v1/shops/{shop_id}/invoices/{invoice_id}/refund",
        )

    def unrefund(self, shop_id: int | str, invoice_id: str):
        """Unmark an invoice as refunded"""
        return self.client.request(
            method="POST",
            endpoint=f"/v1/shops/{shop_id}/invoices/{invoice_id}/unrefund",
        )

    def update_dashboard_note(self, shop_id: int | str, invoice_id: str, note: str):
        """Update the invoice dashboard note"""
        return self.client.request(
            method="PUT",
            endpoint=f"/v1/shops/{shop_id}/invoices/{invoice_id}/dashboard-note",
            json={"note": note},
        )

    def get_pdf(self, shop_id: int | str, invoice_id: str):
        """Retrieve the PDF of the invoice"""
        return self.client.request(
            method="GET",
            endpoint=f"/v1/shops/{shop_id}/invoices/{invoice_id}/pdf",
        )

    def process(self, shop_id: int | str, invoice_id: str):
        """Process an invoice"""
        return self.client.request(
            method="GET",
            endpoint=f"/v1/shops/{shop_id}/invoices/{invoice_id}/process",
        )

    def replace_delivered(self, shop_id: int | str, invoice_id: str, invoice_item_id: int, replacements: dict):
        """Replace delivered items in an invoice"""
        payload = {"invoice_item_id": invoice_item_id, "replacements": replacements}
        return self.client.request(
            method="POST",
            endpoint=f"/v1/shops/{shop_id}/invoices/{invoice_id}/replace-delivered",
            json=payload,
        )
