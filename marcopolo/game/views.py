from .models import Usuario, Carta, Punto 
from rest_framework import viewsets
from rest_framework.response import Response
from .serializers import UsuarioSerializer


class UsuarioViewSet(viewsets.ViewSet):
    def list(self, request):
    	p = request.GET
    	user = Usuario.objects.get(email=p['email'])
    	res = {
    		'id': user.id,
    		'email': user.email,
    		'nombre': user.first_name 

    	}
		# print "Entro a get"
		# queryset = Usuario.objects.all()
		# serializer = UsuarioSerializer(queryset,many=True)

        return Response (res)


class Registro(viewsets.ModelViewSet):
    pass