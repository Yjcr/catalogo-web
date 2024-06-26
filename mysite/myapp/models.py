# This is an auto-generated   # def __str__(self):
    #     return self.nombredesarrolladora
    # Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Categorias(models.Model):
    idcategoria = models.AutoField(db_column='IDCategoria', primary_key=True)  # Field name made lowercase.
    nombrecategoria = models.CharField(db_column='NombreCategoria', max_length=15, blank=True, null=True)  # Field name made lowercase.
    descripcioncategoria = models.TextField(db_column='DescripcionCategoria', blank=True, null=True)  # Field name made lowercase.
    
    def __str__(self):
        return self.nombrecategoria if self.nombrecategoria else "Sin nombre"
    
    class Meta:
        managed = False
        db_table = 'Categorias'
        db_table_comment = 'Categorias de videojuegos'


class Clientes(models.Model):
    idcliente = models.AutoField(db_column='IDCliente', primary_key=True)  # Field name made lowercase.
    idusuario = models.ForeignKey('Usuarios', models.DO_NOTHING, db_column='IDUsuario')  # Field name made lowercase.
    idubicacion = models.ForeignKey('Ubicaciones', models.DO_NOTHING, db_column='IDUbicacion')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Clientes'
        db_table_comment = 'Tabla que almacenara los datos de clientes registrados'


class Desarrolladoras(models.Model):
    iddesarrolladora = models.AutoField(db_column='IDDesarrolladora', primary_key=True)  # Field name made lowercase.
    nombredesarrolladora = models.CharField(db_column='NombreDesarrolladora', blank=True, null=True)  # Field name made lowercase.
    descripciondes = models.TextField(db_column='DescripcionDes', blank=True, null=True)  # Field name made lowercase.
    sitioweb = models.TextField(db_column='SitioWeb', blank=True, null=True)  # Field name made lowercase.
    
  
    class Meta:
        managed = False
        db_table = 'Desarrolladoras'
        db_table_comment = 'Tabla que almacenara las desarrolladoras que crearon sus respectivos juegos'


class Detallesfactura(models.Model):
    iddetallefactura = models.IntegerField(db_column='IDDetalleFactura', primary_key=True)  # Field name made lowercase.
    idfactura = models.ForeignKey('Facturas', models.DO_NOTHING, db_column='IDFactura', blank=True, null=True)  # Field name made lowercase.
    idvideojuego = models.ForeignKey('Videojuegos', models.DO_NOTHING, db_column='IDVideojuego', blank=True, null=True)  # Field name made lowercase.
    cantidad = models.SmallIntegerField(db_column='Cantidad', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DetallesFactura'
        db_table_comment = 'Detalles de la factura'


class Empleados(models.Model):
    idempleado = models.AutoField(db_column='IDEmpleado', primary_key=True)  # Field name made lowercase.
    idusuario = models.ForeignKey('Usuarios', models.DO_NOTHING, db_column='IDUsuario')  # Field name made lowercase.
    foto = models.TextField(db_column='Foto')  # Field name made lowercase.
    notas = models.TextField(db_column='Notas', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Empleados'
        db_table_comment = 'Tabla que almacenara los empleados de la tienda'


class Facturas(models.Model):
    idfactura = models.AutoField(db_column='IDFactura', primary_key=True)  # Field name made lowercase.
    idpago = models.ForeignKey('Pagos', models.DO_NOTHING, db_column='IDPago')  # Field name made lowercase.
    idempleado = models.ForeignKey(Empleados, models.DO_NOTHING, db_column='IDEmpleado')  # Field name made lowercase.
    idcliente = models.ForeignKey(Clientes, models.DO_NOTHING, db_column='IDCliente')  # Field name made lowercase.
    fechafactura = models.DateField(db_column='FechaFactura', blank=True, null=True)  # Field name made lowercase.
    total = models.DecimalField(db_column='Total', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Facturas'
        db_table_comment = 'Tabla que almacenara los datos principales de las facturas'


class Favoritos(models.Model):
    idfavorito = models.IntegerField(db_column='IDFavorito', primary_key=True)  # Field name made lowercase.
    idusuario = models.ForeignKey('Usuarios', models.DO_NOTHING, db_column='IDUsuario')  # Field name made lowercase.
    idvideojuego = models.ForeignKey('Videojuegos', models.DO_NOTHING, db_column='IDVideojuego')  # Field name made lowercase.
    fechaagregado = models.DateField(db_column='FechaAgregado', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Favoritos'
        db_table_comment = 'Tabla que almacenara los juegos favoritos seleccionados por el usuario'


class Pagos(models.Model):
    idpago = models.AutoField(db_column='IDPago', primary_key=True)  # Field name made lowercase.
    idcliente = models.ForeignKey(Clientes, models.DO_NOTHING, db_column='IDCliente')  # Field name made lowercase.
    referencia = models.CharField(db_column='Referencia', blank=True, null=True)  # Field name made lowercase.
    capturapago = models.TextField(db_column='CapturaPago', blank=True, null=True)  # Field name made lowercase.
    metodopago = models.CharField(db_column='MetodoPago', max_length=20, blank=True, null=True)  # Field name made lowercase.
    fechapago = models.DateField(db_column='FechaPago', blank=True, null=True)  # Field name made lowercase.
    monto = models.DecimalField(db_column='Monto', max_digits=10, decimal_places=5, blank=True, null=True)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float

    class Meta:
        managed = False
        db_table = 'Pagos'
        db_table_comment = 'Tabla que almacenara los pagos realizados por los clientes para generar factura y comprobar dicho pago'


class Promociones(models.Model):
    idpromocion = models.IntegerField(db_column='IDPromocion', primary_key=True)  # Field name made lowercase.
    idvideojuego = models.ForeignKey('Videojuegos', models.DO_NOTHING, db_column='IDVideojuego', blank=True, null=True)  # Field name made lowercase.
    descuento = models.DecimalField(db_column='Descuento', max_digits=5, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    fechainicio = models.DateField(db_column='FechaInicio', blank=True, null=True)  # Field name made lowercase.
    fechafin = models.DateField(db_column='FechaFin', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Promociones'
        db_table_comment = 'Tabla que administrara las promociones disponibles para los respectivos videojuegos'


class Reseñas(models.Model):
    idreseña = models.AutoField(db_column='IDReseña', primary_key=True)  # Field name made lowercase.
    idvideojuego = models.IntegerField(db_column='IDVideojuego')  # Field name made lowercase.
    idusuario = models.ForeignKey('Usuarios', models.DO_NOTHING, db_column='IDUsuario')  # Field name made lowercase.
    comentario = models.TextField(db_column='Comentario', blank=True, null=True)  # Field name made lowercase.
    calificacion = models.SmallIntegerField(db_column='Calificacion', blank=True, null=True)  # Field name made lowercase.
    fechareseña = models.DateField(db_column='FechaReseña', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Reseñas'
        db_table_comment = 'Tabla que administrara las reseñas creadas por los usuarios (ya sea empleado o cliente)'


class Ubicaciones(models.Model):
    idubicacion = models.AutoField(db_column='IDUbicacion', primary_key=True)  # Field name made lowercase.
    direccion = models.CharField(db_column='Direccion', max_length=50, blank=True, null=True)  # Field name made lowercase.
    estado = models.CharField(db_column='Estado', max_length=20, blank=True, null=True)  # Field name made lowercase.
    ciudad = models.CharField(db_column='Ciudad', max_length=25, blank=True, null=True)  # Field name made lowercase.
    codpostal = models.CharField(db_column='CodPostal', max_length=15, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Ubicaciones'
        db_table_comment = 'Tabla de ubicaciones que conecta con la direcciñn del cliente'


class Usuarios(models.Model):
    idusuario = models.AutoField(db_column='IDUsuario', primary_key=True)  # Field name made lowercase.
    nombre = models.CharField(db_column='Nombre', max_length=10, blank=True, null=True)  # Field name made lowercase.
    apellido = models.CharField(db_column='Apellido', max_length=10, blank=True, null=True)  # Field name made lowercase.
    cedula = models.CharField(db_column='Cedula', max_length=20, blank=True, null=True)  # Field name made lowercase.
    nacimiento = models.DateField(db_column='Nacimiento', blank=True, null=True)  # Field name made lowercase.
    email = models.CharField(db_column='Email', max_length=254, blank=True, null=True)  # Field name made lowercase.
    telefono = models.CharField(db_column='Telefono', max_length=20, blank=True, null=True)  # Field name made lowercase.
    nombreusuario = models.CharField(db_column='NombreUsuario', max_length=15, blank=True, null=True)  # Field name made lowercase.
    contraseña = models.CharField(db_column='Contraseña', max_length=15, blank=True, null=True)  # Field name made lowercase.
    rol = models.TextField(db_column='Rol', blank=True, null=True)  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'Usuarios'
        db_table_comment = 'Tabla que almacenara los usuarios de la pagina web'


class Videojuegos(models.Model):
    idvideojuego = models.AutoField(db_column='IDVideojuego', primary_key=True)  # Field name made lowercase.
    nombre = models.CharField(db_column='Nombre', max_length=30, blank=True, null=True)  # Field name made lowercase.
    lanzamiento = models.DateField(db_column='Lanzamiento', blank=True, null=True)  # Field name made lowercase.
    descripcion = models.TextField(db_column='Descripcion', blank=True, null=True)  # Field name made lowercase.
    precio = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True, db_column='Precio')
    plataforma = models.CharField(db_column='Plataforma', max_length=30, blank=True, null=True)  # Field name made lowercase.
    imagenjuego = models.ImageField(upload_to='videojuegos', blank=True, null=True, db_column='ImagenJuego')
    iddesarrolladora = models.ForeignKey(Desarrolladoras, models.DO_NOTHING, db_column='IDDesarrolladora', blank=True, null=True)  # Field name made lowercase.
    idcategoria = models.ForeignKey(Categorias, models.DO_NOTHING, db_column='IDCategoria', blank=True, null=True)  # Field name made lowercase.
    
    def __str__(self):
        return self.nombre if self.nombre else "Sin nombre"
    class Meta:
        managed = False
        db_table = 'Videojuegos'
        db_table_comment = 'Tabla que almacenara todos los datos relacionados con los videojuegos disponibles e ingresados'