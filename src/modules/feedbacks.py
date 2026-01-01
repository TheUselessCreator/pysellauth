class FeedbacksModule:
    def __init__(self, client):
        self.client = client

    def list(self, shop_id: int | str):
        """Retrieve all feedbacks for a shop"""
        return self.client.request(
            method="GET",
            endpoint=f"/v1/shops/{shop_id}/feedbacks",
        )

    def get(self, shop_id: int | str, feedback_id: str):
        """Retrieve a specific feedback"""
        return self.client.request(
            method="GET",
            endpoint=f"/v1/shops/{shop_id}/feedbacks/{feedback_id}",
        )

    def reply(self, shop_id: int | str, feedback_id: str, reply_text: str):
        """Reply to a specific feedback"""
        return self.client.request(
            method="POST",
            endpoint=f"/v1/shops/{shop_id}/feedbacks/{feedback_id}/reply",
            data={"reply": reply_text},
        )

    def dispute(self, shop_id: int | str, feedback_id: str, reason: str):
        """Dispute a specific feedback"""
        return self.client.request(
            method="POST",
            endpoint=f"/v1/shops/{shop_id}/feedbacks/{feedback_id}/dispute",
            data={"reason": reason},
        )
