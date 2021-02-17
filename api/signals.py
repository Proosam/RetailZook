from django.db.models.signals import post_save,pre_save
from django.dispatch import receiver
from api.POS.models import SalesSub,PurchaseSub,Product

@receiver(post_save, sender=SalesSub)
def updateStockSales(sender, instance, created, **kwargs):
    if created:
        print("Signal Triggered")
        quantity = instance.quantity
        stock = Product.objects.get(id=instance.product.id)
        stock.available_stock -= quantity
        stock.save()

@receiver(post_save, sender=PurchaseSub)
def updateStockPurchase(sender, instance, created, **kwargs):
    if created:
        quantity = instance.quantity
        stock = Product.objects.get(id=instance.product.id)
        stock.available_stock += quantity
        stock.save()