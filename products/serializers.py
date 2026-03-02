from rest_framework import serializers
from .models import Category,Product,Review



class CategoryListSeializers(serializers.ModelSerializer):
    product_count = serializers.SerializerMethodField()
    class Meta():
        model = Category
        fields = 'name product_count'.split()

    def get_product_count(self,category):
        return category.products.count()

class CategoryDetailSeializers(serializers.ModelSerializer):
    class Meta():
        model = Category
        fields = '__all__'




class ProductListSerializer(serializers.ModelSerializer):
    rating = serializers.SerializerMethodField()
    class Meta():
        model = Product
        fields = 'title price rating reviews'.split()
    def get_rating(self,product):
        return product.medium_rating()

class ProductDetailSerializer(serializers.ModelSerializer):
    class Meta():
        model = Product
        fields = '__all__'



class  ProductSerialializer(serializers.ModelSerializer):
    rating = serializers.SerializerMethodField()
    class Meta:
        model = Product
        fields = 'title rating'.split()
    def get_rating(self,product):
        return product.medium_rating()

class ReviewListSerializers(serializers.ModelSerializer):
    product = ProductSerialializer()
    class Meta():
        model = Review
        fields = 'text product'.split()

class ReviewDetailSerializers(serializers.ModelSerializer):
    class Meta():
        model = Review
        fields = '__all__'