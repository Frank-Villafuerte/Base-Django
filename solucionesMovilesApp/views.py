from rest_framework.viewsets import ModelViewSet
from solucionesMovilesApp.serializers import BitacoraActividadSerializer, ContratoSerializer, MaeClienteSerializer, ReqMantenimientoSerializer, RolUsuarioSerializer, UsuarioSerializer
from solucionesMovilesApp.models import BitacoraActividad, Contrato, MaeCliente, ReqMantenimiento, RolUsuario, Usuario
from rest_framework import viewsets, status
from rest_framework.response import Response

class BitacoraActividadViewSet(ModelViewSet):
    queryset = BitacoraActividad.objects.order_by('pk')
    serializer_class = BitacoraActividadSerializer

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.bit_estadoregistro = 'I'  # Marcar el estado como inactivo en lugar de eliminar
        instance.save()
        return Response(status=status.HTTP_204_NO_CONTENT)

class ContratoViewSet(ModelViewSet):
    queryset = Contrato.objects.order_by('pk')
    serializer_class = ContratoSerializer

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.con_estadoregistro = 'I'  # Marcar el estado como inactivo en lugar de eliminar
        instance.save()
        return Response(status=status.HTTP_204_NO_CONTENT)

class MaeClienteViewSet(ModelViewSet):
    queryset = MaeCliente.objects.order_by('pk')
    serializer_class = MaeClienteSerializer

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.cli_estadoregistro = 'I'  # Marcar el estado como inactivo en lugar de eliminar
        instance.save()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ReqMantenimientoViewSet(ModelViewSet):
    queryset = ReqMantenimiento.objects.order_by('pk')
    serializer_class = ReqMantenimientoSerializer

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.req_estadoregistro = 'I'  # Marcar el estado como inactivo en lugar de eliminar
        instance.save()
        return Response(status=status.HTTP_204_NO_CONTENT)

class RolUsuarioViewSet(ModelViewSet):
    queryset = RolUsuario.objects.order_by('pk')
    serializer_class = RolUsuarioSerializer

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.rol_estadoregistro = 'I'  # Marcar el estado como inactivo en lugar de eliminar
        instance.save()
        return Response(status=status.HTTP_204_NO_CONTENT)

class UsuarioViewSet(ModelViewSet):
    queryset = Usuario.objects.order_by('pk')
    serializer_class = UsuarioSerializer

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.usr_estadoregistro = 'I'  # Marcar el estado como inactivo en lugar de eliminar
        instance.save()
        return Response(status=status.HTTP_204_NO_CONTENT)
