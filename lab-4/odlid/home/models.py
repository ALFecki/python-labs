from django.db import models
import datetime


class ProductCategory(models.Model):
    name = models.CharField(max_length=200, 
                            help_text='Enter category name')
    
    image = models.ImageField(upload_to='resources/images', blank=True)
    

class ProductModel(models.Model):
    name = models.CharField(max_length=200, 
                            help_text='Enter model name')
    
    def year_choices():
        return [(r,r) for r in range(1999, datetime.date.today().year+1)]

    def current_year():
        return datetime.date.today().year

    year_of_manufacture = models.IntegerField(choices=year_choices, default=current_year)


class Product(models.Model):
    name = models.CharField(max_length=200,
                            help_text='Enter product name')
    
    code = models.IntegerField(help_text='Enter product code')

    model = models.ForeignKey(ProductModel, on_delete=models.CASCADE)
    cost = models.IntegerField(help_text='Enter product cost')

    in_prod = models.BooleanField(help_text='Enter is product in production')
    
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)
    
    


    
    


