from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
import datetime
from django.urls import reverse


class ProductCategory(models.Model):
    name = models.CharField(max_length=200, 
                            help_text='Enter category name')
    
    image = models.ImageField(upload_to='static/images', blank=True, null=True)

    def get_url(self):
        return reverse('home:toys_list_by_category', args=[str(self.id)])
    
    def __str__(self) -> str:
        return self.name.__str__()
    

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

    def __str__(self) -> str:
        return self.name.__str__()


class Product(models.Model):
    name = models.CharField(max_length=200,
                            help_text='Enter product name')
    
    code = models.IntegerField(help_text='Enter product code')

    image = models.ImageField(upload_to='static/images', blank=True, null=True)

    model = models.ForeignKey(ProductModel, on_delete=models.CASCADE, null=True)
    cost = models.FloatField(help_text='Enter product cost')

    in_prod = models.BooleanField(help_text='Enter is product in production')
    
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE, null=True)

    def get_detail_url(self):
        return reverse('home:detail', args=[str(self.id)])
    
    def get_edit_url(self):
        return reverse('home:edit', args=[str(self.id)])
    
    def get_delete_url(self):
        return reverse('home:delete', args=[str(self.id)])
    
    


    
    


