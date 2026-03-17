from rest_framework import serializers
from .models import Category,Product,Review
from rest_framework.exceptions import ValidationError



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


class CategoryValidateSerializer(serializers.Serializer):
    name = serializers.CharField(min_length=3,max_length=155)

class ProductValidateSerializer(serializers.Serializer):
    title = serializers.CharField()
    description = serializers.CharField(max_length = 300)
    price = serializers.IntegerField(min_value=1)
    category_id = serializers.IntegerField()

    def validate_category_id(self, category_id):
        try:
            Category.objects.get(id=category_id)
        except Category.DoesNotExist:
            raise ValidationError('Category is not exist')
        return category_id
    

class ReviewValidateSerializer(serializers.Serializer):
    text = serializers.CharField(max_length=500)
    product_id = serializers.IntegerField()
    stars = serializers.IntegerField(min_value=1,max_value=6)

    def validate_product_id(self, product_id):
        try:
            Product.objects.get(id=product_id)
        except Product.DoesNotExist:
            raise ValidationError('Product is not exist!')
        return product_id