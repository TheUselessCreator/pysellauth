from .modules.analytics import AnalyticsModule
from .modules.blacklist import BlacklistModule
from .modules.blog_posts import BlogPostsModule
from .modules.checkout import CheckoutModule
from .modules.coupons import CouponsModule
from .modules.crypto_wallet import CryptoWalletModule
from .modules.custom_fields import CustomFieldsModule
from .modules.customers import CustomersModule
from .modules.domains import DomainsModule
from .modules.feedbacks import FeedbacksModule
from .modules.groups import GroupsModule
from .modules.images import ImagesModule
from .modules.invoices import InvoicesModule
from .modules.notifications import NotificationsModule
from .modules.payment_methods import PaymentMethodsModule
from .modules.products import ProductsModule
from .modules.shops import ShopsModule
from .modules.tickets import TicketsModule

exports = {
    "analytics": AnalyticsModule,
    "blacklist": BlacklistModule,
    "blog_posts": BlogPostsModule,
    "checkout": CheckoutModule,
    "coupons": CouponsModule,
    "crypto_wallet": CryptoWalletModule,
    "custom_fields": CustomFieldsModule,
    "customers": CustomersModule,
    "domains": DomainsModule,
    "feedbacks": FeedbacksModule,
    "groups": GroupsModule,
    "images": ImagesModule,
    "invoices": InvoicesModule,
    "notifications": NotificationsModule,
    "payment_methods": PaymentMethodsModule,
    "products": ProductsModule,
    "shops": ShopsModule,
    "tickets": TicketsModule,
}
