from rest_framework import routers, serializers, viewsets

from Profile.models import modelProfile, Ciudad, Genero, Ocupacion, Estado, EstadoCivil

class modelProfileSerializer(serializers.ModelSerializer):
	class Meta:
		model = modelProfile
		fields = ('__all__')

class modelProfileGetSerializer(serializers.ModelSerializer):
    class Meta:
        model = modelProfile
        fields = ('nombre','apPat','apMat','edad')

class CiudadSerializer(serializers.ModelSerializer):
	class Meta:
		model = Ciudad
		fields = ('__all__')

class GeneroSerializer(serializers.ModelSerializer):
	class Meta:
		model = Genero
		fields = ('__all__')

class OcupacionSerializer(serializers.ModelSerializer):
	class Meta:
		model = Ocupacion
		fields = ('__all__')

class EstadoSerializer(serializers.ModelSerializer):
	class Meta:
		model = Estado
		fields = ('__all__')

class EstadoCivilSerializer(serializers.ModelSerializer):
	class Meta:
		model = EstadoCivil
		fields = ('__all__')