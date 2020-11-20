# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Administrador(models.Model):
    rut_admin = models.CharField(primary_key=True, max_length=15)
    nom_admin = models.CharField(max_length=20, blank=True, null=True)
    apellidop_admin = models.CharField(max_length=15, blank=True, null=True)
    apellidom_admin = models.CharField(max_length=15, blank=True, null=True)
    telefono_admin = models.BigIntegerField(blank=True, null=True)
    correo_admin = models.CharField(max_length=30, blank=True, null=True)
    pass_admin = models.CharField(max_length=30, blank=True, null=True)
    rol_id_rol = models.ForeignKey('Rol', models.DO_NOTHING, db_column='rol_id_rol')

    class Meta:
        managed = False
        db_table = 'administrador'
    
    def __str__(self):
        return '{}'.format(self.rut_admin)


class BodegaEmpresa(models.Model):
    id_bode = models.BigIntegerField(primary_key=True)
    venta_recibida = models.CharField(max_length=1, blank=True, null=True)
    subasta_id_subasta = models.ForeignKey('Subasta', models.DO_NOTHING, db_column='subasta_id_subasta')
    bodega_productor_id_bprod = models.ForeignKey('BodegaProductor', models.DO_NOTHING, db_column='bodega_productor_id_bprod')

    class Meta:
        managed = False
        db_table = 'bodega_empresa'


class BodegaProductor(models.Model):
    id_bprod = models.BigIntegerField(primary_key=True)
    producto_envasado = models.CharField(max_length=2, blank=True, null=True)
    producto_refrigerado = models.CharField(max_length=2, blank=True, null=True)
    cantidad_disponible = models.BigIntegerField(blank=True, null=True)
    producto_id_prod = models.ForeignKey('Producto', models.DO_NOTHING, db_column='producto_id_prod')

    class Meta:
        managed = False
        db_table = 'bodega_productor'


class ClienteExterno(models.Model):
    rut_cliente = models.CharField(primary_key=True, max_length=15)
    nom_cliente = models.CharField(max_length=20, blank=True, null=True)
    apellidop_cliente = models.CharField(max_length=15, blank=True, null=True)
    apellidom_cliente = models.CharField(max_length=15, blank=True, null=True)
    direccion_residencial = models.CharField(max_length=50, blank=True, null=True)
    ciudad_residencial = models.CharField(max_length=15, blank=True, null=True)
    correo_electronico = models.CharField(max_length=50, blank=True, null=True)
    numero_telefonico = models.BigIntegerField(blank=True, null=True)
    pass_cliente = models.CharField(max_length=30, blank=True, null=True)
    rol_id_rol = models.ForeignKey('Rol', models.DO_NOTHING, db_column='rol_id_rol')
    auth_user_username = models.CharField(max_length=150)


    class Meta:
        managed = False
        db_table = 'cliente_externo'
        
    def __str__(self):
        return '{}'.format(self.rut_cliente)
    
    


class ClienteInterno(models.Model):
    rut_cli_ex = models.CharField(primary_key=True, max_length=30)
    nom_clien_in = models.CharField(max_length=30, blank=True, null=True)
    rol_id_rol = models.ForeignKey('Rol', models.DO_NOTHING, db_column='rol_id_rol')
    apellidop_clien_in = models.CharField(max_length=20, blank=True, null=True)
    apellidom_clientein = models.CharField(max_length=20, blank=True, null=True)
    direccion_clien_in = models.CharField(max_length=30, blank=True, null=True)
    ciudad_clien_in = models.CharField(max_length=40, blank=True, null=True)
    correo_clien_in = models.CharField(max_length=40, blank=True, null=True)
    numero_cliente_in = models.BigIntegerField(blank=True, null=True)
    pass_cliente = models.CharField(max_length=30, blank=True, null=True)
    auth_user_username = models.CharField(max_length=150)

    class Meta:
        managed = False
        db_table = 'cliente_interno'
    
    def __str__(self):
        return '{}'.format(self.rut_cli_ex)


class Consultor(models.Model):
    rut_consultor = models.CharField(primary_key=True, max_length=15)
    nom_consultor = models.CharField(max_length=30, blank=True, null=True)
    apellidop_consultor = models.CharField(max_length=15, blank=True, null=True)
    apellidom_consultor = models.CharField(max_length=15, blank=True, null=True)
    correo_consultor = models.CharField(max_length=30, blank=True, null=True)
    numero_consultor = models.BigIntegerField(blank=True, null=True)
    pass_consultor = models.CharField(max_length=30, blank=True, null=True)
    rol_id_rol = models.ForeignKey('Rol', models.DO_NOTHING, db_column='rol_id_rol')

    class Meta:
        managed = False
        db_table = 'consultor'


class Contrato(models.Model):
    id_contra = models.BigIntegerField(primary_key=True)
    nume_contrato = models.BigIntegerField(blank=True, null=True)
    fecha_inicio = models.DateField(blank=True, null=True)
    fecha_vencimiento = models.DateField(blank=True, null=True)
    vigencia = models.CharField(max_length=2, blank=True, null=True)
    productor_rut_produc = models.ForeignKey('Productor', models.DO_NOTHING, db_column='productor_rut_produc')

    class Meta:
        managed = False
        db_table = 'contrato'


class ContratoVenta(models.Model):
    id_cont = models.BigIntegerField(primary_key=True)
    num_contrato_venta = models.BigIntegerField(blank=True, null=True)
    fecha_inicio = models.DateField(blank=True, null=True)
    fecha_termino = models.DateField(blank=True, null=True)
    vigencia = models.CharField(max_length=2, blank=True, null=True)
    solicitud_venta_id_soli = models.ForeignKey('SolicitudVenta', models.DO_NOTHING, db_column='solicitud_venta_id_soli')

    class Meta:
        managed = False
        db_table = 'contrato_venta'
    
    def __str__(self):
        return '{}'.format(self.num_contrato_venta)


class DetallePedido(models.Model):
    id_deta = models.BigIntegerField(primary_key=True)
    productos = models.CharField(max_length=300, blank=True, null=True)
    cantidad = models.BigIntegerField(blank=True, null=True)
    subtotal = models.BigIntegerField(blank=True, null=True)
    fecha_entrega = models.DateField(blank=True, null=True)
    fecha_emision = models.DateField(blank=True, null=True)
    pedido_venta_cod_pedido = models.ForeignKey('PedidoVenta', models.DO_NOTHING, db_column='pedido_venta_cod_pedido')
    estado_id_estado = models.ForeignKey('Estado', models.DO_NOTHING, db_column='estado_id_estado')

    class Meta:
        managed = False
        db_table = 'detalle_pedido'


class Estado(models.Model):
    id_estado = models.BigIntegerField(primary_key=True)
    descripcion = models.CharField(max_length=1, blank=True, null=True)
    fecha_estado = models.DateField(blank=True, null=True)
    seccion_esta_id_sesta = models.ForeignKey('SeccionEsta', models.DO_NOTHING, db_column='seccion_esta_id_sesta')

    class Meta:
        managed = False
        db_table = 'estado'


class OfertaProduc(models.Model):
    codigo_op = models.FloatField(primary_key=True)
    producto_id_prod = models.ForeignKey('Producto', models.DO_NOTHING, db_column='producto_id_prod')
    productor_rut_produc = models.ForeignKey('Productor', models.DO_NOTHING, db_column='productor_rut_produc')

    class Meta:
        managed = False
        db_table = 'oferta_produc'


class OfertaTransp(models.Model):
    cod_ot = models.FloatField(primary_key=True)
    precio_oferta = models.FloatField(blank=True, null=True)
    descripcion = models.CharField(max_length=1, blank=True, null=True)
    transportista_rut_transp = models.ForeignKey('Transportista', models.DO_NOTHING, db_column='transportista_rut_transp')

    class Meta:
        managed = False
        db_table = 'oferta_transp'


class Pago(models.Model):
    id_pago = models.BigIntegerField(primary_key=True)
    medio_pago = models.CharField(max_length=15, blank=True, null=True)
    fecha_pago = models.DateField(blank=True, null=True)
    numero_transaccion = models.CharField(max_length=1, blank=True, null=True)
    pedido_venta_cod_pedido = models.ForeignKey('PedidoVenta', models.DO_NOTHING, db_column='pedido_venta_cod_pedido')

    class Meta:
        managed = False
        db_table = 'pago'


class PedidoVenta(models.Model):
    cod_pedido = models.BigIntegerField(primary_key=True)
    cantidad = models.FloatField(blank=True, null=True)
    comision_empresa = models.BigIntegerField(blank=True, null=True)
    costo_transportista = models.BigIntegerField(blank=True, null=True)
    costo_aduana = models.BigIntegerField(db_column='costo__aduana', blank=True, null=True)  # Field renamed because it contained more than one '_' in a row.
    costo_servicio = models.BigIntegerField(blank=True, null=True)
    costo_total = models.BigIntegerField(blank=True, null=True)
    proceso_venta_id_proceso = models.ForeignKey('ProcesoVenta', models.DO_NOTHING, db_column='proceso_venta_id_proceso')

    class Meta:
        managed = False
        db_table = 'pedido_venta'


class ProcesoInterno(models.Model):
    codigo_proceso = models.BigIntegerField(primary_key=True)
    cliente_interno_rut_cli_ex = models.ForeignKey(ClienteInterno, models.DO_NOTHING, db_column='cliente_interno_rut_cli_ex')
    saldo_saldo = models.ForeignKey('Saldo', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'proceso_interno'


class ProcesoVenta(models.Model):
    id_proceso = models.BigIntegerField(primary_key=True)
    informacion_venta = models.CharField(max_length=300, blank=True, null=True)
    contrato_venta_id_cont = models.ForeignKey(ContratoVenta, models.DO_NOTHING, db_column='contrato_venta_id_cont')


    class Meta:
        managed = False
        db_table = 'proceso_venta'


class Producto(models.Model):
    id_prod = models.BigIntegerField(primary_key=True)
    nom_prod = models.CharField(max_length=30, blank=True, null=True)
    precio_prod = models.BigIntegerField(blank=True, null=True)
    peso_prod = models.FloatField(blank=True, null=True)
    calidad_prod = models.CharField(max_length=2, blank=True, null=True)
    productor_rut_produc = models.ForeignKey('Productor', models.DO_NOTHING, db_column='productor_rut_produc')

    class Meta:
        managed = False
        db_table = 'producto'

    def __str__(self):
        return '{}'.format(self.productor_rut_produc)


class Productor(models.Model):
    rut_produc = models.CharField(primary_key=True, max_length=15)
    nom_produc = models.CharField(max_length=20, blank=True, null=True)
    apellidop_produc = models.CharField(max_length=15, blank=True, null=True)
    apellidom_produc = models.CharField(max_length=15, blank=True, null=True)
    direccion_produc = models.CharField(max_length=50, blank=True, null=True)
    ciudad_produc = models.CharField(max_length=40, blank=True, null=True)
    telefono_produc = models.BigIntegerField(blank=True, null=True)
    correo_produc = models.CharField(max_length=30, blank=True, null=True)
    pass_produc = models.CharField(max_length=30, blank=True, null=True)
    rol_id_rol = models.ForeignKey('Rol', models.DO_NOTHING, db_column='rol_id_rol')
    auth_user_username = models.CharField(max_length=150)

    class Meta:
        managed = False
        db_table = 'productor'

    def __str__(self):
        return '{}'.format(self.rut_produc)


class RelSoliProducto(models.Model):
    id_rel_soli_produc = models.BigIntegerField(primary_key=True)
    producto_id_prod = models.ForeignKey(Producto, models.DO_NOTHING, db_column='producto_id_prod')
    solicitud_venta_id_soli = models.ForeignKey('SolicitudVenta', models.DO_NOTHING, db_column='solicitud_venta_id_soli')
    cantidad = models.BigIntegerField(blank=True, null=True)
    tipo_distribucion = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'rel_soli_producto'


class Reportes(models.Model):
    id_reporte = models.BigIntegerField(primary_key=True)
    numero_reporte = models.BigIntegerField(blank=True, null=True)
    descripcion_reporte = models.CharField(max_length=500, blank=True, null=True)
    administrador_rut_admin = models.ForeignKey(Administrador, models.DO_NOTHING, db_column='administrador_rut_admin')
    consultor_rut_consultor = models.ForeignKey(Consultor, models.DO_NOTHING, db_column='consultor_rut_consultor')

    class Meta:
        managed = False
        db_table = 'reportes'


class Rol(models.Model):
    id_rol = models.BigIntegerField(primary_key=True)
    nom_rol = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'rol'

    def __str__(self):
        return '{}'.format(self.nom_rol)


class Saldo(models.Model):
    producto_id_prod = models.ForeignKey(Producto, models.DO_NOTHING, db_column='producto_id_prod')
    id_saldo = models.BigIntegerField(blank=True, null=True)
    cantidad = models.BigIntegerField(blank=True, null=True)
    tipo_distribucion = models.CharField(max_length=1, blank=True, null=True)
    saldo_id = models.FloatField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'saldo'


class SeccionEsta(models.Model):
    id_sesta = models.BigIntegerField(primary_key=True)
    descripcion = models.CharField(max_length=300, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'seccion_esta'


class SolicitudVenta(models.Model):
    id_soli = models.BigIntegerField(primary_key=True)
    numero_soli = models.BigIntegerField(blank=True, null=True)
    direccion_entrega = models.CharField(max_length=50, blank=True, null=True)
    cliente_externo_rut_cliente = models.ForeignKey(ClienteExterno, models.DO_NOTHING, db_column='cliente_externo_rut_cliente')

    class Meta:
        managed = False
        db_table = 'solicitud_venta'


class Subasta(models.Model):
    id_subasta = models.BigIntegerField(primary_key=True)
    requisito_subasta = models.CharField(max_length=100, blank=True, null=True)
    pedido_venta_cod_pedido = models.ForeignKey(PedidoVenta, models.DO_NOTHING, db_column='pedido_venta_cod_pedido')
    oferta_transp_cod_ot = models.ForeignKey(OfertaTransp, models.DO_NOTHING, db_column='oferta_transp_cod_ot')

    class Meta:
        managed = False
        db_table = 'subasta'


class Transportista(models.Model):
    rut_transp = models.CharField(primary_key=True, max_length=15)
    nombre_transp = models.CharField(max_length=20, blank=True, null=True)
    apellidop_transp = models.CharField(max_length=15, blank=True, null=True)
    apellidom_transp = models.CharField(max_length=15, blank=True, null=True)
    correo_trasp = models.CharField(max_length=30, blank=True, null=True)
    telefono_transo = models.BigIntegerField(blank=True, null=True)
    patente_vehiculo = models.CharField(max_length=30, blank=True, null=True)
    capacidad_carga = models.BigIntegerField(blank=True, null=True)
    refrigeracion = models.CharField(max_length=2, blank=True, null=True)
    pass_transp = models.CharField(max_length=30, blank=True, null=True)
    rol_id_rol = models.ForeignKey(Rol, models.DO_NOTHING, db_column='rol_id_rol')
    auth_user_username = models.CharField(max_length=150)

    class Meta:
        managed = False
        db_table = 'transportista'
    
    def __str__(self):
        return '{}'.format(self.rut_transp)
    
    