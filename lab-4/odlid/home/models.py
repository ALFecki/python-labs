from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
import datetime
from django.urls import reverse


class ProductCategory(models.Model):
    name = models.CharField(max_length=200, 
                            help_text='Enter category name')
    
    image = models.ImageField(upload_to='resources/images', blank=True, null=True)

    def get_url(self):
        return reverse('home:toys_list_by_category', args=[str(self.id)])
    

class ProductModel(models.Model):
    name = models.CharField(max_length=200, 
                            help_text='Enter model name')
    
    def year_choices(self):
        return [(r,r) for r in range(1999, datetime.date.today().year+1)]

    def current_year(self):
        return datetime.date.today().year
    
    def max_value_current_year(self, value):
        return MaxValueValidator(self.current_year())(value) 

    year_of_manufacture = models.IntegerField(validators=[MinValueValidator(1984), max_value_current_year])


class Product(models.Model):
    name = models.CharField(max_length=200,
                            help_text='Enter product name')
    
    code = models.IntegerField(help_text='Enter product code')

    model = models.ForeignKey(ProductModel, on_delete=models.CASCADE, null=True)
    cost = models.IntegerField(help_text='Enter product cost')

    in_prod = models.BooleanField(help_text='Enter is product in production')
    
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE, null=True)
    
    


    
    


