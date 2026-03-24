from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class Product(models.Model):
    title = models.CharField(max_length=1000)
    description = models.CharField(max_length=1000)
    price = models.IntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE,blank=True,null=True,related_name='products')
    def medium_rating(self):
        reviews = self.reviews.all()
        if not reviews:
            return 0
        rating = [i.stars for i in reviews]
        return round(sum(rating)/len(rating),1)
    
    def __str__(self):
        return self.title



class Review(models.Model):
    text = models.CharField(max_length=10000)
    product = models.ForeignKey(Product,on_delete=models.CASCADE,related_name='reviews')
    STARS = (
        (i,i * '⭐') for i in range(1,6)
    )
    stars = models.IntegerField(choices=STARS,default=5)

    def __str__(self):
        return f'{self.product}-{self.stars}'
    