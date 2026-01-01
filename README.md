# PySellAuth

**PySellAuth** is a Python wrapper for the [SellAuth API](https://sellauth.com), allowing developers to manage shops, products, payments, customers, tickets, feedbacks, and more directly from Python.

## Features

- Full access to SellAuth API through Python.
- Supports all modules including Shops, Products, Customers, Tickets, Feedbacks, Payments, Analytics, and more.
- Typed methods and clear API calls.
- Easy authentication using your API token.

## Installation

```bash
pip install pysellauth
````

## Initialization

```python
from pysellauth import SellAuthClient

# Initialize the client with your API token
client = SellAuthClient(api_key="YOUR_API_KEY_HERE")
```

## Modules Overview

### Analytics

* `analytics.get_stats(shop_id)`: Retrieve analytics for a shop.

### Blacklist

* `blacklist.list(shop_id)`: List all blacklist rules.
* `blacklist.add(shop_id, **kwargs)`: Add a new blacklist rule.
* `blacklist.remove(shop_id, blacklist_id)`: Remove a blacklist rule.

### Blog Posts

* `blog.list(shop_id)`: List all blog posts.
* `blog.create(shop_id, title, content)`: Create a blog post.
* `blog.update(shop_id, post_id, **kwargs)`: Update a blog post.
* `blog.delete(shop_id, post_id)`: Delete a blog post.

### Checkout

* `checkout.process(shop_id, data)`: Handle checkout requests.

### Coupons

* `coupons.list(shop_id)`: List all coupons.
* `coupons.create(shop_id, code, discount, **kwargs)`: Create a coupon.
* `coupons.update(shop_id, coupon_id, **kwargs)`: Update a coupon.
* `coupons.delete(shop_id, coupon_id)`: Delete a coupon.

### Crypto Wallet

* `crypto.list_wallets(shop_id)`: List crypto wallets.
* `crypto.add_wallet(shop_id, currency, address)`: Add a new wallet.
* `crypto.remove_wallet(shop_id, wallet_id)`: Remove a wallet.

### Custom Fields

* `custom_fields.list(shop_id)`: List custom fields.
* `custom_fields.create(shop_id, name, field_type)`: Add a custom field.
* `custom_fields.update(shop_id, field_id, **kwargs)`: Update a custom field.
* `custom_fields.delete(shop_id, field_id)`: Delete a custom field.

### Customers

* `customers.list(shop_id)`: List all customers.
* `customers.get(shop_id, customer_id)`: Retrieve a customer.
* `customers.create(shop_id, **kwargs)`: Create a customer.
* `customers.update(shop_id, customer_id, **kwargs)`: Update a customer.
* `customers.delete(shop_id, customer_id)`: Delete a customer.

### Domains

* `domains.list(shop_id)`: List custom domains.
* `domains.add(shop_id, domain)`: Add a new domain.
* `domains.remove(shop_id, domain_id)`: Remove a domain.

### Feedbacks

* `feedbacks.list(shop_id)`: List all feedbacks.
* `feedbacks.get(shop_id, feedback_id)`: Retrieve a feedback.
* `feedbacks.reply(shop_id, feedback_id, reply_text)`: Reply to a feedback.
* `feedbacks.dispute(shop_id, feedback_id, reason)`: Dispute a feedback.

### Groups

* `groups.list(shop_id)`: List all groups.
* `groups.create(shop_id, name)`: Create a group.
* `groups.update(shop_id, group_id, **kwargs)`: Update a group.
* `groups.delete(shop_id, group_id)`: Delete a group.

### Images

* `images.upload(shop_id, file_path)`: Upload an image.
* `images.delete(shop_id, image_id)`: Delete an image.

### Invoices

* `invoices.list(shop_id)`: List invoices.
* `invoices.create(shop_id, **kwargs)`: Create invoice.
* `invoices.update(shop_id, invoice_id, **kwargs)`: Update invoice.
* `invoices.delete(shop_id, invoice_id)`: Delete invoice.

### Notifications

* `notifications.list(shop_id)`: List notifications.
* `notifications.send(shop_id, message, **kwargs)`: Send notification.

### Payment Methods

* `payment_methods.list(shop_id)`: List payment methods.
* `payment_methods.add(shop_id, type, **kwargs)`: Add a payment method.
* `payment_methods.update(shop_id, method_id, **kwargs)`: Update payment method.
* `payment_methods.delete(shop_id, method_id)`: Delete payment method.

### Payment Processors

* `payment_processors.list(shop_id)`: List payment processors.
* `payment_processors.add(shop_id, name, **kwargs)`: Add processor.
* `payment_processors.update(shop_id, processor_id, **kwargs)`: Update processor.
* `payment_processors.delete(shop_id, processor_id)`: Delete processor.

### Products

* `products.list(shop_id)`: List all products.
* `products.get(shop_id, product_id)`: Retrieve a product.
* `products.create(shop_id, **kwargs)`: Create a product.
* `products.update(shop_id, product_id, **kwargs)`: Update a product.
* `products.delete(shop_id, product_id)`: Delete a product.

### Shops

* `shops.list()`: List all shops.
* `shops.get(shop_id)`: Retrieve a shop.
* `shops.create(name, subdomain, logo=None)`: Create a shop.
* `shops.update(shop_id, **kwargs)`: Update a shop.
* `shops.delete(shop_id, password, name)`: Delete a shop.
* `shops.stats(shop_id)`: Get shop statistics.

### Tickets

* `tickets.list(shop_id, **filters)`: List tickets.
* `tickets.get(shop_id, ticket_id)`: Retrieve a ticket.
* `tickets.create(shop_id, customer_id, subject, invoice_id=None)`: Create ticket.
* `tickets.close(shop_id, ticket_id)`: Close ticket.
* `tickets.reopen(shop_id, ticket_id)`: Reopen ticket.
* `tickets.archive(shop_id, ticket_id)`: Archive ticket.
* `tickets.unarchive(shop_id, ticket_id)`: Unarchive ticket.
* `tickets.send_message(shop_id, ticket_id, content)`: Send a message.
* `tickets.delete_message(shop_id, ticket_id, message_id)`: Delete a message.

## Contributing

1. Fork the repository
2. Create a feature branch: `git checkout -b feature-name`
3. Make changes
4. Commit: `git commit -m "Add feature"`
5. Push: `git push origin feature-name`
6. Open a Pull Request

## License

MIT License
