from django.db import models
from django.template.defaultfilters import slugify
from django.urls import reverse
# Create your models here.
class categ(models.Model):
    name=models.CharField(max_length=250,unique=True)
    slug=models.SlugField(max_length=250,unique=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'
    def get_url(self):
        return reverse('flipapp:prod_cat',args=[self.slug])

    def __str__(self):
        return '{}'.format(self.name)

class products(models.Model):
    name = models.CharField(max_length=250,unique=True)
    slug = models.SlugField(max_length=250,unique=True)
    desc = models.TextField(blank=True)
    img = models.ImageField(upload_to='product')
    category=models.ForeignKey(categ,on_delete=models.CASCADE)
    price = models.IntegerField()
    stock= models.IntegerField()
    available= models.BooleanField()

    def get_url(self):
        return reverse('flipapp:details', args=[self.category.slug,self.slug])

    def __str__(self):
        return '{}'.format(self.name)



