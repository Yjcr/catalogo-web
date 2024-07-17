# Generated by Django 5.0.7 on 2024-07-13 04:53

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categorias',
            fields=[
                ('idcategoria', models.AutoField(db_column='IDCategoria', primary_key=True, serialize=False)),
                ('nombrecategoria', models.CharField(blank=True, db_column='NombreCategoria', max_length=15, null=True)),
                ('descripcioncategoria', models.TextField(blank=True, db_column='DescripcionCategoria', null=True)),
            ],
            options={
                'db_table': 'Categorias',
                'db_table_comment': 'Categorias de videojuegos',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Clientes',
            fields=[
                ('idcliente', models.AutoField(db_column='IDCliente', primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'Clientes',
                'db_table_comment': 'Tabla que almacenara los datos de clientes registrados',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Desarrolladoras',
            fields=[
                ('iddesarrolladora', models.AutoField(db_column='IDDesarrolladora', primary_key=True, serialize=False)),
                ('nombredesarrolladora', models.CharField(blank=True, db_column='NombreDesarrolladora', null=True)),
                ('descripciondes', models.TextField(blank=True, db_column='DescripcionDes', null=True)),
                ('sitioweb', models.TextField(blank=True, db_column='SitioWeb', null=True)),
            ],
            options={
                'db_table': 'Desarrolladoras',
                'db_table_comment': 'Tabla que almacenara las desarrolladoras que crearon sus respectivos juegos',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Empleados',
            fields=[
                ('idempleado', models.AutoField(db_column='IDEmpleado', primary_key=True, serialize=False)),
                ('foto', models.TextField(db_column='Foto')),
                ('notas', models.TextField(blank=True, db_column='Notas', null=True)),
            ],
            options={
                'db_table': 'Empleados',
                'db_table_comment': 'Tabla que almacenara los empleados de la tienda',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Ubicaciones',
            fields=[
                ('idubicacion', models.AutoField(db_column='IDUbicacion', primary_key=True, serialize=False)),
                ('direccion', models.CharField(blank=True, db_column='Direccion', max_length=50, null=True)),
                ('estado', models.CharField(blank=True, db_column='Estado', max_length=20, null=True)),
                ('ciudad', models.CharField(blank=True, db_column='Ciudad', max_length=25, null=True)),
                ('codpostal', models.CharField(blank=True, db_column='CodPostal', max_length=15, null=True)),
            ],
            options={
                'db_table': 'Ubicaciones',
                'db_table_comment': 'Tabla de ubicaciones que conecta con la direcciñn del cliente',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Usuarios',
            fields=[
                ('idusuario', models.AutoField(db_column='IDUsuario', primary_key=True, serialize=False)),
                ('nombre', models.CharField(blank=True, db_column='Nombre', max_length=10, null=True)),
                ('apellido', models.CharField(blank=True, db_column='Apellido', max_length=10, null=True)),
                ('cedula', models.CharField(blank=True, db_column='Cedula', max_length=20, null=True)),
                ('nacimiento', models.DateField(blank=True, db_column='Nacimiento', null=True)),
                ('email', models.CharField(blank=True, db_column='Email', max_length=254, null=True)),
                ('telefono', models.CharField(blank=True, db_column='Telefono', max_length=20, null=True)),
                ('nombreusuario', models.CharField(blank=True, db_column='NombreUsuario', max_length=15, null=True)),
                ('contraseña', models.CharField(blank=True, db_column='Contraseña', max_length=15, null=True)),
                ('rol', models.TextField(blank=True, db_column='Rol', null=True)),
            ],
            options={
                'db_table': 'Usuarios',
                'db_table_comment': 'Tabla que almacenara los usuarios de la pagina web',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Pagos',
            fields=[
                ('idpago', models.AutoField(db_column='IDPago', primary_key=True, serialize=False)),
                ('referencia', models.CharField(blank=True, db_column='Referencia', null=True)),
                ('capturapago', models.TextField(blank=True, db_column='CapturaPago', null=True)),
                ('metodopago', models.CharField(blank=True, db_column='MetodoPago', max_length=20, null=True)),
                ('fechapago', models.DateField(blank=True, db_column='FechaPago', null=True)),
                ('monto', models.DecimalField(blank=True, db_column='Monto', decimal_places=5, max_digits=10, null=True)),
                ('idcliente', models.ForeignKey(db_column='IDCliente', on_delete=django.db.models.deletion.DO_NOTHING, to='myapp.clientes')),
            ],
            options={
                'db_table': 'Pagos',
                'db_table_comment': 'Tabla que almacenara los pagos realizados por los clientes para generar factura y comprobar dicho pago',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Facturas',
            fields=[
                ('idfactura', models.AutoField(db_column='IDFactura', primary_key=True, serialize=False)),
                ('fechafactura', models.DateField(blank=True, db_column='FechaFactura', null=True)),
                ('total', models.DecimalField(blank=True, db_column='Total', decimal_places=2, max_digits=10, null=True)),
                ('idcliente', models.ForeignKey(db_column='IDCliente', on_delete=django.db.models.deletion.DO_NOTHING, to='myapp.clientes')),
                ('idempleado', models.ForeignKey(db_column='IDEmpleado', on_delete=django.db.models.deletion.DO_NOTHING, to='myapp.empleados')),
                ('idpago', models.ForeignKey(db_column='IDPago', on_delete=django.db.models.deletion.DO_NOTHING, to='myapp.pagos')),
            ],
            options={
                'db_table': 'Facturas',
                'db_table_comment': 'Tabla que almacenara los datos principales de las facturas',
                'managed': True,
            },
        ),
        migrations.AddField(
            model_name='clientes',
            name='idubicacion',
            field=models.ForeignKey(db_column='IDUbicacion', on_delete=django.db.models.deletion.DO_NOTHING, to='myapp.ubicaciones'),
        ),
        migrations.CreateModel(
            name='Reseñas',
            fields=[
                ('idreseña', models.AutoField(db_column='IDReseña', primary_key=True, serialize=False)),
                ('idvideojuego', models.IntegerField(db_column='IDVideojuego')),
                ('comentario', models.TextField(blank=True, db_column='Comentario', null=True)),
                ('calificacion', models.SmallIntegerField(blank=True, db_column='Calificacion', null=True)),
                ('fechareseña', models.DateField(blank=True, db_column='FechaReseña', null=True)),
                ('idusuario', models.ForeignKey(db_column='IDUsuario', on_delete=django.db.models.deletion.DO_NOTHING, to='myapp.usuarios')),
            ],
            options={
                'db_table': 'Reseñas',
                'db_table_comment': 'Tabla que administrara las reseñas creadas por los usuarios (ya sea empleado o cliente)',
                'managed': True,
            },
        ),
        migrations.AddField(
            model_name='empleados',
            name='idusuario',
            field=models.ForeignKey(db_column='IDUsuario', on_delete=django.db.models.deletion.DO_NOTHING, to='myapp.usuarios'),
        ),
        migrations.AddField(
            model_name='clientes',
            name='idusuario',
            field=models.ForeignKey(db_column='IDUsuario', on_delete=django.db.models.deletion.DO_NOTHING, to='myapp.usuarios'),
        ),
        migrations.CreateModel(
            name='Videojuegos',
            fields=[
                ('idvideojuego', models.AutoField(db_column='IDVideojuego', primary_key=True, serialize=False)),
                ('nombre', models.CharField(blank=True, db_column='Nombre', max_length=30, null=True)),
                ('lanzamiento', models.DateField(blank=True, db_column='Lanzamiento', null=True)),
                ('descripcion', models.TextField(blank=True, db_column='Descripcion', null=True)),
                ('precio', models.DecimalField(blank=True, db_column='Precio', decimal_places=2, max_digits=10, null=True)),
                ('plataforma', models.CharField(blank=True, db_column='Plataforma', max_length=30, null=True)),
                ('imagenjuego', models.ImageField(blank=True, db_column='ImagenJuego', null=True, upload_to='galeria')),
                ('idcategoria', models.ForeignKey(blank=True, db_column='IDCategoria', null=True, on_delete=django.db.models.deletion.SET_NULL, to='myapp.categorias')),
                ('iddesarrolladora', models.ForeignKey(blank=True, db_column='IDDesarrolladora', null=True, on_delete=django.db.models.deletion.SET_NULL, to='myapp.desarrolladoras')),
            ],
            options={
                'db_table': 'Videojuegos',
                'db_table_comment': 'Tabla que almacenara todos los datos relacionados con los videojuegos disponibles e ingresados',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Promociones',
            fields=[
                ('idpromocion', models.IntegerField(db_column='IDPromocion', primary_key=True, serialize=False)),
                ('descuento', models.DecimalField(blank=True, db_column='Descuento', decimal_places=2, max_digits=5, null=True)),
                ('fechainicio', models.DateField(blank=True, db_column='FechaInicio', null=True)),
                ('fechafin', models.DateField(blank=True, db_column='FechaFin', null=True)),
                ('idvideojuego', models.ForeignKey(blank=True, db_column='IDVideojuego', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='myapp.videojuegos')),
            ],
            options={
                'db_table': 'Promociones',
                'db_table_comment': 'Tabla que administrara las promociones disponibles para los respectivos videojuegos',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Favoritos',
            fields=[
                ('idfavorito', models.IntegerField(db_column='IDFavorito', primary_key=True, serialize=False)),
                ('fechaagregado', models.DateField(blank=True, db_column='FechaAgregado', null=True)),
                ('idusuario', models.ForeignKey(db_column='IDUsuario', on_delete=django.db.models.deletion.DO_NOTHING, to='myapp.usuarios')),
                ('idvideojuego', models.ForeignKey(db_column='IDVideojuego', on_delete=django.db.models.deletion.DO_NOTHING, to='myapp.videojuegos')),
            ],
            options={
                'db_table': 'Favoritos',
                'db_table_comment': 'Tabla que almacenara los juegos favoritos seleccionados por el usuario',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Detallesfactura',
            fields=[
                ('iddetallefactura', models.IntegerField(db_column='IDDetalleFactura', primary_key=True, serialize=False)),
                ('cantidad', models.SmallIntegerField(blank=True, db_column='Cantidad', null=True)),
                ('idfactura', models.ForeignKey(blank=True, db_column='IDFactura', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='myapp.facturas')),
                ('idvideojuego', models.ForeignKey(blank=True, db_column='IDVideojuego', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='myapp.videojuegos')),
            ],
            options={
                'db_table': 'DetallesFactura',
                'db_table_comment': 'Detalles de la factura',
                'managed': True,
            },
        ),
    ]
