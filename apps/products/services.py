import requests
from apps.comments.models import Comment
from django.db.models import Avg
from apps.products.models import Product


def get_usd_price():
   url = 'https://cbu.uz/uz/arkhiv-kursov-valyut/json/'
   response = requests.get(url=url)
   return float(response.json()[0]['Rate'])


def change_product_avg_rating(product_id):
   rating = Comment.objects.filter(product_id=product_id).aggregate(rat_avg = Avg('rating'))['rat_avg']
   Product.objects.filter(pk=product_id).update(rating=rating)