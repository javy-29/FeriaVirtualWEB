from django.contrib import admin
from .models import Administrador,Saldo,BodegaEmpresa,BodegaProductor,ClienteExterno,ClienteInterno,Consultor,Contrato,ContratoVenta,DetallePedido,Estado,OfertaProduc,OfertaTransp,Pago,PedidoVenta,ProcesoVenta,Producto,Productor,RelSoliProducto,Reportes,Rol,SeccionEsta,SolicitudVenta,Subasta,Transportista, ProcesoInterno
# Register your models here.
admin.site.register(Administrador)
admin.site.register(BodegaEmpresa)
admin.site.register(BodegaProductor)
admin.site.register(ClienteExterno)
admin.site.register(ClienteInterno)
admin.site.register(Consultor)
admin.site.register(Contrato)
admin.site.register(ContratoVenta)
admin.site.register(DetallePedido)
admin.site.register(Estado)
admin.site.register(OfertaProduc)
admin.site.register(OfertaTransp)
admin.site.register(Pago)
admin.site.register(PedidoVenta)
admin.site.register(ProcesoVenta)
admin.site.register(ProcesoInterno)
admin.site.register(Producto)
admin.site.register(Productor)
admin.site.register(RelSoliProducto)
admin.site.register(Reportes)
admin.site.register(Rol)
admin.site.register(Saldo)
admin.site.register(SeccionEsta)
admin.site.register(SolicitudVenta)
admin.site.register(Subasta)
admin.site.register(Transportista)