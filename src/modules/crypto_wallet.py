class CryptoWalletModule:
    def __init__(self, client):
        self.client = client

    def payouts(self, shop_id: int | str):
        """Retrieve the crypto wallets payout history"""
        return self.client.request(
            method="GET",
            endpoint=f"/v1/shops/{shop_id}/payouts",
        )

    def balances(self, shop_id: int | str):
        """Retrieve the current balances of the crypto wallets"""
        return self.client.request(
            method="GET",
            endpoint=f"/v1/shops/{shop_id}/payouts/balances",
        )

    def payout(self, shop_id: int | str, currency: str, address: str, amount: float):
        """Payout crypto from the wallet"""
        body = {
            "currency": currency,
            "address": address,
            "amount": amount,
        }
        return self.client.request(
            method="POST",
            endpoint=f"/v1/shops/{shop_id}/payouts/payout",
            data=body,
        )

    def transactions(self, shop_id: int | str):
        """Retrieve the transaction history for the crypto wallets"""
        return self.client.request(
            method="GET",
            endpoint=f"/v1/shops/{shop_id}/payouts/transactions",
        )
