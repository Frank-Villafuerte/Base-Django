from rest_framework.serializers import ModelSerializer
from solucionesMovilesApp.models import BitacoraActividad, Contrato, MaeCliente, ReqMantenimiento, RolUsuario, Usuario


class BitacoraActividadSerializer(ModelSerializer):

    class Meta:
        model = BitacoraActividad
        fields = '__all__'


class ContratoSerializer(ModelSerializer):

    class Meta:
        model = Contrato
        fields = '__all__'


class MaeClienteSerializer(ModelSerializer):

    class Meta:
        model = MaeCliente
        fields = '__all__'


class ReqMantenimientoSerializer(ModelSerializer):

    class Meta:
        model = ReqMantenimiento
        fields = '__all__'


class RolUsuarioSerializer(ModelSerializer):

    class Meta:
        model = RolUsuario
        fields = '__all__'


class UsuarioSerializer(ModelSerializer):

    class Meta:
        model = Usuario
        fields = '__all__'
