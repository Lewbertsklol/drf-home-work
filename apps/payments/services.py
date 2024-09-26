import requests
from django.conf import settings


def create_product(product):
    """Product is any object with name and price filed required"""
    requests.post(
        "https://api.stripe.com/v1/products",
        headers={"Authorization": f"Bearer {settings.STRIPE_TEST_API_KEY}"},
        data={
            "id": product.id,
            "name": product.name,
        },
    )
    price_id = requests.post(
        "https://api.stripe.com/v1/prices",
        headers={"Authorization": f"Bearer {settings.STRIPE_TEST_API_KEY}"},
        data={
            "currency": "rub",
            "unit_amount": product.price,
            "product": product.id,
        },
    ).json()["id"]
    payment_url = requests.post(
        "https://api.stripe.com/v1/checkout/sessions",
        headers={"Authorization": f"Bearer {settings.STRIPE_TEST_API_KEY}"},
        data={
            "mode": "payment",
            "line_items[0][price]": price_id,
            "line_items[0][quantity]": 1,
            "success_url": f"http://{settings.BASE_URL}/payments/",
        },
    ).json()["url"]
    return payment_url
