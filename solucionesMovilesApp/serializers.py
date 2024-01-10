from rest_framework.serializers import ModelSerializer
from solucionesMovilesApp.models import BitacoraActividad, Contrato, MaeCliente, ReqMantenimiento, RolUsuario, Usuario


class BitacoraActividadSerializer(ModelSerializer):

    class Meta:
        model = BitacoraActividad
        depth = 2
        fields = '__all__'


class ContratoSerializer(ModelSerializer):

    class Meta:
        model = Contrato
        depth = 2
        fields = '__all__'


class MaeClienteSerializer(ModelSerializer):

    class Meta:
        model = MaeCliente
        depth = 2
        fields = '__all__'


class ReqMantenimientoSerializer(ModelSerializer):

    class Meta:
        model = ReqMantenimiento
        depth = 2
        fields = '__all__'


class RolUsuarioSerializer(ModelSerializer):

    class Meta:
        model = RolUsuario
        depth = 2
        fields = '__all__'


class UsuarioSerializer(ModelSerializer):

    class Meta:
        model = Usuario
        depth = 2
        fields = '__all__'
