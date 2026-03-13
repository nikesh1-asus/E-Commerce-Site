from django.db import models
from django.urls import reverse
from category.models import Category

class Product(models.Model):
    product_name = models.CharField(max_length=255, unique=True)
    slug =         models.SlugField(max_length= 500, unique=True)
    description =  models.TextField(max_length=550,blank=True)
    image =        models.ImageField(upload_to='photos/products')
    price =        models.DecimalField(max_digits=10, decimal_places=2)
    stock =        models.IntegerField()
    is_available = models.BooleanField(default=True, )
    category =     models.ForeignKey(Category,on_delete=models.CASCADE)
    created_at =   models.DateTimeField(auto_now_add=True )
    updated_at =   models.DateTimeField(auto_now=True )

    def get_url(self):
        return reverse('product_detail', args=[self.category.slug, self.slug])

    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"

    def __str__(self):
        return self.product_name