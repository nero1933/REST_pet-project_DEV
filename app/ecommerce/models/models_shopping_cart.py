from django.db import models
from django.core.validators import MinValueValidator


class ShoppingCart(models.Model):
    user = models.ForeignKey('users.UserProfile', related_name='users', on_delete=models.CASCADE)

    def __str__(self):
        return f'Shopping Cart: {self.user}'


class ShoppingCartItem(models.Model):
    cart = models.ForeignKey('ShoppingCart', related_name='shopping_cart_item', on_delete=models.CASCADE)
    product_item_size_quantity = models.ForeignKey('ProductItemSizeQuantity', on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(validators=[MinValueValidator(1)])
