from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import (
    ReviewListSerializers,
    ProductListSerializer,
    ReviewDetailSerializers,
    ProductDetailSerializer,
    CategoryListSeializers,
    CategoryDetailSeializers,
    CategoryValidateSerializer,
    ProductValidateSerializer,
    ReviewValidateSerializer
)
from .models import Category,Product,Review

@api_view(['GET','POST'])
def category_list_api_view(req):
    if req.method == 'GET':
        category = Category.objects.all()
        data = CategoryListSeializers(category,many=True).data
        return Response(status=status.HTTP_200_OK,
                        data=data)
    elif req.method == 'POST':
        serializer = CategoryValidateSerializer(data=req.data)
        serializer.is_valid(raise_exception=True)

        name = serializer.validated_data.get('name')

        category = Category.objects.create(
            name=name
        )
        return Response(status=status.HTTP_201_CREATED)


@api_view(['GET','PUT','DELETE'])
def category_detail_api_view(req,id):
    try:
        category = Category.objects.get(id=id)
    except Category.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND,
                        data={'error':'category is not found!'})
    if req.method == 'GET':
        data = CategoryDetailSeializers(category,many=False).data
        return Response(status=status.HTTP_200_OK,
                        data=data)
    
    elif req.method == 'DELETE':
        category.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    elif req.method == 'PUT':
        category.name = req.data.get('name')
        category.save()
        return Response(status=status.HTTP_200_OK)


@api_view(['GET','POST'])
def product_list_api_view(req):
    
    if req.method == 'GET':
        products = Product.objects.all()
        data = ProductListSerializer(products,many=True).data
        return Response(status=status.HTTP_200_OK,
                        data=data)
    elif req.method == 'POST':
        serializer = ProductValidateSerializer(data=req.data)
        serializer.is_valid(raise_exception=True)

        title = serializer.validated_data.get('title')
        description = serializer.validated_data.get('description')
        price = serializer.validated_data.get('price')
        category_id = serializer.validated_data.get('category_id')

        product = Product.objects.create(
            title=title,
            description=description,
            price=price,
            category_id=category_id
        )
        return Response(status=status.HTTP_201_CREATED)

@api_view(['GET','PUT','DELETE'])
def product_detail_api_view(req,id):
    try:
        product = Product.objects.get(id=id)
    except Product.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND,
                        data={'error':'Product is not found!'})
    
    if req.method == 'GET':
        data = ProductDetailSerializer(product,many=False).data
        return Response(status=status.HTTP_200_OK,
                        data=data)

    elif req.method == 'DELETE':
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    elif req.method == 'PUT':
        product.title = req.data.get('title')
        product.description = req.data.get('description')
        product.price = req.data.get('price')
        product.category_id = req.data.get('category_id')


@api_view(['GET','POST'])
def reviews_list_api_view(req):
    if req.method == 'GET':
        reviews = Review.objects.all()
        data = ReviewListSerializers(reviews,many=True).data
        return Response(status=status.HTTP_200_OK,
                        data=data)
    elif req.method == 'POST':
        serializer = ReviewValidateSerializer(data=req.data)
        serializer.is_valid(raise_exception=True)

        text = serializer.validated_data.get('text')
        product_id = serializer.validated_data.get('product_id')
        stars = serializer.validated_data.get('stars')

        review = Review.objects.create(
            text=text,
            product_id=product_id,
            stars=stars
        )

        return Response(status=status.HTTP_201_CREATED )



@api_view(['GET','PUT','DELETE'])
def review_detail_api_view(req,id):
    try:
        review = Review.objects.get(id=id)
    except Review.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND,
                        data={'error':'review is not found!'})
    met = req.method
    if met == 'GET':
        data = ReviewDetailSerializers(review,many=False).data
        return Response(status=status.HTTP_200_OK,
                        data=data)
    
    elif met == 'DELETE':
        review.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    elif met == 'PUT':
        review.text = req.data.get('text')
        review.product_id = req.data.get('product_id')
        review.stars = req.data.get('stars')
        review.save()
        return Response(status=status.HTTP_201_CREATED)