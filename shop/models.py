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
        verbose_name_plural ='categories'

    def get_url(self):
        return reverse('prod_cat',args=[self.slug])                                                                     #slug fields melil kaanikaanulla urls

    def __str__(self):
        return '{}'.format(self.name)                                                                                   #category name classilek return cheyikunnu admin panelil categori tablil category name varaan vendi
# ------------------------------------------------------------------------------------

class products(models.Model):
    name=models.CharField(max_length=159,unique=True)
    slug=models.SlugField(max_length=250,unique=True)
    img=models.ImageField(upload_to='product')
    desc=models.TextField()
    stock=models.IntegerField()
    available=models.BooleanField()
    price=models.IntegerField()
    category=models.ForeignKey(categ,on_delete=models.CASCADE)

    def get_url(self):
        return reverse('detail_page',args=[self.category.slug,self.slug])                                               #slug fields melil kaanikaanulla urls

    def __str__(self):
        return '{}'.format(self.name)
