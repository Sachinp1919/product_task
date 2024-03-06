from rest_framework.views import APIView
from .models import Product
from .serializers import ProductSerializer
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
import pandas as pd


class ProductGetAPI(APIView):
    def post(self,request):
        try:
            input_file = request.data.get('file')
            df = pd.read_excel(input_file)
            df.dropna(how='all', axis=1, inplace=True)
            if 'product_manufacturing_date' in df.columns:
                df['product_manufacturing_date'] = df['product_manufacturing_date'].dt.date
            if 'product_expiry_date' in df.columns:
                df['product_expiry_date'] = df['product_expiry_date'].dt.date
            product_list = df.to_dict(orient='records')
            serializer = ProductSerializer(data=product_list, many=True)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(data=serializer.data, status=201)
        except Exception as e:
            return Response(data={'details':'There is an error fetching data'}, status=400)
        
    def get(self, request):
        try:
            product = Product.objects.all()
            serializer = ProductSerializer(product, many=True)
            return Response(data=serializer.data, status=200)
        except:
            return Response(data=serializer.errors, status=400)
        
class ProductCreateAPI(APIView):
    def post(self, request):
        try:
            serializer = ProductSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(data=serializer.data, status=201)
        except:
            return Response(data=serializer.errors, status=400)




class ProductDetailsAPI(APIView):
    def get(self, request, pk=None):
        try:
            product = Product.objects.get(pk=pk)
            serializer = ProductSerializer(product)
            return Response(data=serializer.data, status=200)
        except:
            return Response(data={'details':'there is an error fetching data'})
        
    def put(self, request, pk=None):
        try:
            product = Product.objects.get(pk=pk)
            serializer = ProductSerializer(data=request.data, instance=product)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(data=serializer.data, status=205)
        except Product.DoesNotExist as e:
            return Response(data={'data':'not found data'}, status=404)
        except:
            return Response(data=serializer.errors, status=400)
        
    def patch(self, request, pk=None):
        try:
            product = Product.objects.get(pk=pk)
            serializer = ProductSerializer(data=request.data, instance=product, partial=True)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(data=serializer.data, status=205)
        except:
            return Response(data=serializer.errors, status=400)
        
    def delete(self, request, pk=None):
        try:
            product = Product.objects.get(pk=pk)
            product.delete()
            return Response(data=None, status=204)
        except:
            return Response(data={'details':'Not found'}, status=400)
        


            


