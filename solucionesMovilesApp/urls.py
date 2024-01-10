from rest_framework.routers import SimpleRouter
from solucionesMovilesApp import views


router = SimpleRouter()

router.register(r'bitacoraactividad', views.BitacoraActividadViewSet)
router.register(r'contrato', views.ContratoViewSet)
router.register(r'maecliente', views.MaeClienteViewSet)
router.register(r'reqmantenimiento', views.ReqMantenimientoViewSet)
router.register(r'rolusuario', views.RolUsuarioViewSet)
router.register(r'usuario', views.UsuarioViewSet)

urlpatterns = router.urls
