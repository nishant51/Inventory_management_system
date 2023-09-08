from django.db import models
from django.contrib.auth.models import User 

CATEGORY = (
    ('ELECTRONIC','ELECTRONIC'),
    ('STATIONARY','STATIONARY'),
    ('HARDWARE','HARDWARE'),
    ('FOOD','FOOD'),
    ('ORNAMENTS','ORNAMENTS'),
)
# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=50 ,null= True)
    category = models.CharField(max_length=20, choices = CATEGORY,null=True)
    quanitiy = models.PositiveIntegerField(null=True)

    class Meta:
        verbose_add_plural:'Product'

    def __str__(self):
        return f'{self.name} of quantity {self.quanitiy}'
    
class Order(models.Model):
    name = models.ForeignKey(Product,on_delete=models.CASCADE,null=True)
    costumer = models.ForeignKey(User,models.CASCADE,null=True)
    orderquantity = models.PositiveIntegerField(null=True)
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_add_plural:'Order'

    def __str__(self):
        return f'{self.costumer}-{self.name}'