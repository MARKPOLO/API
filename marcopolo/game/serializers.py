from .models import Usuario, Punto, Carta
from rest_framework import serializers

class UsuarioSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Usuario
        fields = ('email', 'first_name', 'last_name')


class CartaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Carta
        fields = ('nombre', 'ataque', 'defensa', 'imagen', 'localizaicon')


class PuntoSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Punto
		fields = ('latitud', 'longitud', 'activo')

