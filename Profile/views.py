from django.shortcuts import render

from django.shortcuts import get_object_or_404
from django.http import Http404

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics

from Profile.models import modelProfile, Ciudad, Genero, Ocupacion, Estado, EstadoCivil

from Profile.serializer import modelProfileSerializer
from Profile.serializer import CiudadSerializer
from Profile.serializer import GeneroSerializer
from Profile.serializer import OcupacionSerializer
from Profile.serializer import EstadoSerializer
from Profile.serializer import EstadoCivilSerializer

class modelProfileList(APIView):
	def get(self, request, format=None):
		print("Metodo get filter")
		queryset = modelProfile.objects.filter(delete=False)
		#many = True Si aplica  si el retorno multiples objetos
		serializer = modelProfileSerializer(queryset, many=True)
		return Response(serializer.data)
	
	def post(self, request, format=None):
		serializer = modelProfileSerializer(data = request.data)
		if serializer.is_valid():  
			serializer.save()
			datas = serializer.data
			return Response(datas)
		return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

class CiudadList(APIView):
	def get(self, request, format=None):
		print("Metodo get filter")
		queryset = Ciudad.objects.filter(delete = False)
		#many = True Si aplica  si el retorno multiples objetos
		serializer = CiudadSerializer(queryset, many=True)
		return Response(serializer.data)
	
	def post(self, request, format=None):
		serializer = CiudadSerializer(data = request.data)
		if serializer.is_valid():  
			serializer.save()
			datas = serializer.data
			return Response(datas)
		return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)


class GeneroList(APIView):
	def get(self, request, format=None):
		print("Metodo get filter")
		queryset = Genero.objects.filter(delete = False)
		#many = True Si aplica  si el retorno multiples objetos
		serializer = GeneroSerializer(queryset, many=True)
		return Response(serializer.data)
	
	def post(self, request, format=None):
		serializer = GeneroSerializer(data = request.data)
		if serializer.is_valid():  
			serializer.save()
			datas = serializer.data
			return Response(datas)
		return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

class OcupacionList(APIView):
	def get(self, request, format=None):
		print("Metodo get filter")
		queryset = Ocupacion.objects.filter(delete = False)
		#many = True Si aplica  si el retorno multiples objetos
		serializer = OcupacionSerializer(queryset, many=True)
		return Response(serializer.data)
	
	def post(self, request, format=None):
		serializer = OcupacionSerializer(data = request.data)
		if serializer.is_valid():  
			serializer.save()
			datas = serializer.data
			return Response(datas)
		return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

class EstadoList(APIView):
	def get(self, request, format=None):
		print("Metodo get filter")
		queryset = Estado.objects.filter(delete = False)
		#many = True Si aplica  si el retorno multiples objetos
		serializer = EstadoSerializer(queryset, many=True)
		return Response(serializer.data)
	
	def post(self, request, format=None):
		serializer = EstadoSerializer(data = request.data)
		if serializer.is_valid():  
			serializer.save()
			datas = serializer.data
			return Response(datas)
		return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

class EstadoCivilList(APIView):
	def get(self, request, format=None):
		print("Metodo get filter")
		queryset = EstadoCivil.objects.filter(delete = False)
		#many = True Si aplica  si el retorno multiples objetos
		serializer = EstadoCivilSerializer(queryset, many=True)
		return Response(serializer.data)
	
	def post(self, request, format=None):
		serializer = EstadoCivilSerializer(data = request.data)
		if serializer.is_valid():  
			serializer.save()
			datas = serializer.data
			return Response(datas)
		return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)