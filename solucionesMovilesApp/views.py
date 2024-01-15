from rest_framework import status, filters
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend
from solucionesMovilesApp.models import BitacoraActividad, Contrato, MaeCliente, ReqMantenimiento, RolUsuario, Usuario
from solucionesMovilesApp.serializers import BitacoraActividadSerializer, ContratoSerializer, MaeClienteSerializer, ReqMantenimientoSerializer, RolUsuarioSerializer, UsuarioSerializer

class BitacoraActividadViewSet(ModelViewSet):
    queryset = BitacoraActividad.objects.order_by('pk')
    serializer_class = BitacoraActividadSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    search_fields = ['bit_descripcionactividad']

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.bit_estadoregistro = '*'  # Marcar el estado como eliminado
        instance.save()
        return Response(status=status.HTTP_204_NO_CONTENT)

    @action(detail=True, methods=['post'])
    def activate(self, request, pk=None):
        instance = self.get_object()
        instance.bit_estadoregistro = 'A'  # Marcar el estado como activo
        instance.save()
        serializer = self.get_serializer(instance)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @action(detail=True, methods=['post'])
    def inactivate(self, request, pk=None):
        instance = self.get_object()
        instance.bit_estadoregistro = 'I'  # Marcar el estado como inactivo
        instance.save()
        serializer = self.get_serializer(instance)
        return Response(serializer.data, status=status.HTTP_200_OK)

class ContratoViewSet(ModelViewSet):
    queryset = Contrato.objects.order_by('pk')
    serializer_class = ContratoSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    search_fields = ['con_tipocontrato']

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.con_estadoregistro = '*'  # Marcar el estado como eliminado
        instance.save()
        return Response(status=status.HTTP_204_NO_CONTENT)

    @action(detail=True, methods=['post'])
    def activate(self, request, pk=None):
        instance = self.get_object()
        instance.con_estadoregistro = 'A'  # Marcar el estado como activo
        instance.save()
        serializer = self.get_serializer(instance)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @action(detail=True, methods=['post'])
    def inactivate(self, request, pk=None):
        instance = self.get_object()
        instance.con_estadoregistro = 'I'  # Marcar el estado como inactivo
        instance.save()
        serializer = self.get_serializer(instance)
        return Response(serializer.data, status=status.HTTP_200_OK)


class MaeClienteViewSet(ModelViewSet):
    queryset = MaeCliente.objects.order_by('pk')
    serializer_class = MaeClienteSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    search_fields = ['cli_nombreempresa', 'cli_infocontacto']

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.cli_estadoregistro = '*'  # Marcar el estado como eliminado
        instance.save()
        return Response(status=status.HTTP_204_NO_CONTENT)

    @action(detail=True, methods=['post'])
    def activate(self, request, pk=None):
        instance = self.get_object()
        instance.cli_estadoregistro = 'A'  # Marcar el estado como activo
        instance.save()
        serializer = self.get_serializer(instance)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @action(detail=True, methods=['post'])
    def inactivate(self, request, pk=None):
        instance = self.get_object()
        instance.cli_estadoregistro = 'I'  # Marcar el estado como inactivo
        instance.save()
        serializer = self.get_serializer(instance)
        return Response(serializer.data, status=status.HTTP_200_OK)

class ReqMantenimientoViewSet(ModelViewSet):
    queryset = ReqMantenimiento.objects.order_by('pk')
    serializer_class = ReqMantenimientoSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    search_fields = ['req_descripcion', 'req_estado']

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.req_estadoregistro = '*'  # Marcar el estado como eliminado
        instance.save()
        return Response(status=status.HTTP_204_NO_CONTENT)

    @action(detail=True, methods=['post'])
    def activate(self, request, pk=None):
        instance = self.get_object()
        instance.req_estadoregistro = 'A'  # Marcar el estado como activo
        instance.save()
        serializer = self.get_serializer(instance)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @action(detail=True, methods=['post'])
    def inactivate(self, request, pk=None):
        instance = self.get_object()
        instance.req_estadoregistro = 'I'  # Marcar el estado como inactivo
        instance.save()
        serializer = self.get_serializer(instance)
        return Response(serializer.data, status=status.HTTP_200_OK)


class RolUsuarioViewSet(ModelViewSet):
    queryset = RolUsuario.objects.order_by('pk')
    serializer_class = RolUsuarioSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    search_fields = ['rol_nombrerol', 'rol_descripcion']

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.rol_estadoregistro = '*'  # Marcar el estado como eliminado
        instance.save()
        return Response(status=status.HTTP_204_NO_CONTENT)

    @action(detail=True, methods=['post'])
    def activate(self, request, pk=None):
        instance = self.get_object()
        instance.rol_estadoregistro = 'A'  # Marcar el estado como activo
        instance.save()
        serializer = self.get_serializer(instance)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @action(detail=True, methods=['post'])
    def inactivate(self, request, pk=None):
        instance = self.get_object()
        instance.rol_estadoregistro = 'I'  # Marcar el estado como inactivo
        instance.save()
        serializer = self.get_serializer(instance)
        return Response(serializer.data, status=status.HTTP_200_OK)


class UsuarioViewSet(ModelViewSet):
    queryset = Usuario.objects.order_by('pk')
    serializer_class = UsuarioSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    search_fields = ['usr_nombreusuario', 'usr_apellidousuario', 'usr_dni', 'usr_celular']

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.usr_estadoregistro = '*'  # Marcar el estado como eliminado
        instance.save()
        return Response(status=status.HTTP_204_NO_CONTENT)

    @action(detail=True, methods=['post'])
    def activate(self, request, pk=None):
        instance = self.get_object()
        instance.usr_estadoregistro = 'A'  # Marcar el estado como activo
        instance.save()
        serializer = self.get_serializer(instance)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @action(detail=True, methods=['post'])
    def inactivate(self, request, pk=None):
        instance = self.get_object()
        instance.usr_estadoregistro = 'I'  # Marcar el estado como inactivo
        instance.save()
        serializer = self.get_serializer(instance)
        return Response(serializer.data, status=status.HTTP_200_OK)

