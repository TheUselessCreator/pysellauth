class TicketsModule:
    def __init__(self, client):
        self.client = client

    def list(self, shop_id: int | str, **filters):
        """Retrieve all tickets for a shop with optional filters (page, perPage, statuses, etc.)"""
        return self.client.request(
            method="GET",
            endpoint=f"/v1/shops/{shop_id}/tickets",
            data=filters
        )

    def get(self, shop_id: int | str, ticket_id: str):
        """Retrieve a specific ticket"""
        return self.client.request(
            method="GET",
            endpoint=f"/v1/shops/{shop_id}/tickets/{ticket_id}"
        )

    def create(self, shop_id: int | str, customer_id: str, subject: str, invoice_id: str = None):
        """Create a new ticket"""
        data = {"customer_id": customer_id, "subject": subject, "invoice_id": invoice_id}
        return self.client.request(
            method="POST",
            endpoint=f"/v1/shops/{shop_id}/tickets",
            data=data
        )

    def close(self, shop_id: int | str, ticket_id: str):
        """Close a ticket"""
        return self.client.request(
            method="POST",
            endpoint=f"/v1/shops/{shop_id}/tickets/{ticket_id}/close"
        )

    def reopen(self, shop_id: int | str, ticket_id: str):
        """Reopen a ticket"""
        return self.client.request(
            method="POST",
            endpoint=f"/v1/shops/{shop_id}/tickets/{ticket_id}/reopen"
        )

    def archive(self, shop_id: int | str, ticket_id: str):
        """Archive a ticket"""
        return self.client.request(
            method="POST",
            endpoint=f"/v1/shops/{shop_id}/tickets/{ticket_id}/archive"
        )

    def unarchive(self, shop_id: int | str, ticket_id: str):
        """Unarchive a ticket"""
        return self.client.request(
            method="POST",
            endpoint=f"/v1/shops/{shop_id}/tickets/{ticket_id}/unarchive"
        )

    def send_message(self, shop_id: int | str, ticket_id: str, content: str):
        """Send a message to a ticket"""
        return self.client.request(
            method="POST",
            endpoint=f"/v1/shops/{shop_id}/tickets/{ticket_id}/messages",
            data={"content": content}
        )

    def delete_message(self, shop_id: int | str, ticket_id: str, message_id: str):
        """Delete a specific message from a ticket"""
        return self.client.request(
            method="DELETE",
            endpoint=f"/v1/shops/{shop_id}/tickets/{ticket_id}/messages/{message_id}"
        )
