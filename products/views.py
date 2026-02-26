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
)
from .models import Category,Product,Review

@api_view(['GET'])
def category_list_api_view(req):
    category = Category.objects.all()
    data = CategoryListSeializers(category,many=True).data
    return Response(status=status.HTTP_200_OK,
                    data=data)

@api_view(['GET'])
def category_detail_api_view(req,id):
    try:
        category = Category.objects.get(id=id)
    except Category.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND,
                        data={'error':'category is not found!'})
    data = CategoryDetailSeializers(category,many=False).data
    return Response(status=status.HTTP_200_OK,
                    data=data)



@api_view(['GET'])
def product_list_api_view(req):
    products = Product.objects.all()
    data = ProductListSerializer(products,many=True).data
    return Response(status=status.HTTP_200_OK,
                    data=data)

@api_view(['GET'])
def product_detail_api_view(req,id):
    try:
        product = Product.objects.get(id=id)
    except Product.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND,
                        data={'error':'Product is not found!'})
    data = ProductDetailSerializer(product,many=False).data
    return Response(status=status.HTTP_200_OK,
                    data=data)



@api_view(['GET'])
def reviews_list_api_view(req):
    reviews = Review.objects.all()
    data = ReviewListSerializers(reviews,many=True).data
    return Response(status=status.HTTP_200_OK,
                    data=data)

@api_view(['GET'])
def review_detail_api_view(req,id):
    try:
        review = Review.objects.get(id=id)
    except Review.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND,
                        data={'error':'review is not found!'})
    data = ReviewDetailSerializers(review,many=False).data
    return Response(status=status.HTTP_200_OK,
                    data=data)