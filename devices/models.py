from django.db import models

# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.


class OldAlert(models.Model):
    id_device = models.ForeignKey('Devices', models.DO_NOTHING, db_column='id_device', blank=True, null=True)
    temperatura = models.IntegerField(blank=True, null=True)
    mensaje = models.TextField(blank=True, null=True)
    sw_visto = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'OLD_alert'


class OldCamaras(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    estado = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'OLD_camaras'


class OldChips(models.Model):
    icc = models.CharField(db_column='ICC', max_length=100, blank=True, null=True)  # Field name made lowercase.
    msisdn = models.CharField(db_column='MSISDN', max_length=100, blank=True, null=True)  # Field name made lowercase.
    numero = models.CharField(db_column='NUMERO', max_length=100, blank=True, null=True)  # Field name made lowercase.
    m2m_imei = models.CharField(db_column='M2M - IMEI', max_length=100, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    camara = models.CharField(db_column='CAMARA', max_length=100, blank=True, null=True)  # Field name made lowercase.
    sensor = models.CharField(db_column='SENSOR', max_length=100, blank=True, null=True)  # Field name made lowercase.
    puk = models.CharField(db_column='PUK', max_length=100, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'OLD_chips'


class OldDataReadingsTest(models.Model):
    valor = models.DecimalField(max_digits=7, decimal_places=1, blank=True, null=True)
    id_device = models.IntegerField(blank=True, null=True)
    id_identificador = models.IntegerField(blank=True, null=True)
    id_type_alert_data = models.IntegerField(blank=True, null=True)
    estado = models.IntegerField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    created_user = models.IntegerField(blank=True, null=True)
    updated_user = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'OLD_data_readings_test'
        unique_together = (('id_device', 'id_identificador', 'id_type_alert_data', 'created_at'),)


class OldDatos(models.Model):
    imei = models.TextField()
    mensaje = models.TextField()
    hora = models.DateTimeField()
    pass_field = models.TextField(db_column='pass')  # Field renamed because it was a Python reserved word.
    tlf = models.CharField(max_length=30)
    id_m = models.CharField(max_length=3)
    com = models.CharField(max_length=2)

    class Meta:
        managed = False
        db_table = 'OLD_datos'


class OldDigitalAlertsBak(models.Model):
    id_type_alert_data = models.IntegerField(blank=True, null=True)
    id_device = models.IntegerField(blank=True, null=True)
    descripcion = models.CharField(max_length=255, blank=True, null=True)
    valor = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    limite_umbral = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    estado = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    fecha = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'OLD_digital_alerts_bak'


class OldDigitalAlertsCopy(models.Model):
    id_type_alert_data = models.IntegerField(blank=True, null=True)
    id_device = models.IntegerField(blank=True, null=True)
    descripcion = models.CharField(max_length=255, blank=True, null=True)
    valor = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    estado = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'OLD_digital_alerts_copy'


class OldFormato8(models.Model):
    imei = models.CharField(max_length=100, blank=True, null=True)
    ts = models.DateTimeField(blank=True, null=True)
    pass_field = models.CharField(db_column='pass', max_length=100, blank=True, null=True)  # Field renamed because it was a Python reserved word.
    type = models.CharField(max_length=100, blank=True, null=True)
    mova = models.CharField(max_length=100, blank=True, null=True)
    tem = models.CharField(max_length=100, blank=True, null=True)
    temh = models.CharField(max_length=100, blank=True, null=True)
    teml = models.CharField(max_length=100, blank=True, null=True)
    teme = models.CharField(max_length=100, blank=True, null=True)
    i1 = models.CharField(max_length=100, blank=True, null=True)
    i2 = models.CharField(max_length=100, blank=True, null=True)
    i3 = models.CharField(max_length=100, blank=True, null=True)
    i4 = models.CharField(max_length=100, blank=True, null=True)
    i5 = models.CharField(max_length=100, blank=True, null=True)
    i6 = models.CharField(max_length=100, blank=True, null=True)
    i7 = models.CharField(max_length=100, blank=True, null=True)
    i8 = models.CharField(max_length=100, blank=True, null=True)
    i9 = models.CharField(max_length=100, blank=True, null=True)
    i10 = models.CharField(max_length=100, blank=True, null=True)
    ad1 = models.CharField(max_length=100, blank=True, null=True)
    ad2 = models.CharField(max_length=100, blank=True, null=True)
    apow = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'OLD_formato8'


class OldM2MPiloto(models.Model):
    imei = models.CharField(max_length=30, blank=True, null=True)
    valor = models.DecimalField(max_digits=7, decimal_places=1, blank=True, null=True)
    id_device = models.ForeignKey('Devices', models.DO_NOTHING, db_column='id_device', blank=True, null=True)
    id_type_alert_data = models.ForeignKey('TypeAlertData', models.DO_NOTHING, db_column='id_type_alert_data', blank=True, null=True)
    estado = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'OLD_m2m_piloto'


class OldM2MPilotoNotificar(models.Model):
    nombres = models.CharField(max_length=50, blank=True, null=True)
    movil = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'OLD_m2m_piloto_notificar'


class OldM2MPilotoUmbral(models.Model):
    minimo = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    maximo = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'OLD_m2m_piloto_umbral'


class OldM2MRouter(models.Model):
    imei = models.TextField(blank=True, null=True)
    ts = models.DateTimeField(blank=True, null=True)
    p = models.CharField(max_length=100, blank=True, null=True)
    st = models.CharField(max_length=100, blank=True, null=True)
    v1 = models.CharField(max_length=100, blank=True, null=True)
    id_sonda = models.CharField(max_length=100, blank=True, null=True)
    v3 = models.CharField(max_length=100, blank=True, null=True)
    v4 = models.CharField(max_length=100, blank=True, null=True)
    v5 = models.CharField(max_length=100, blank=True, null=True)
    v6 = models.CharField(max_length=100, blank=True, null=True)
    type = models.CharField(max_length=100, blank=True, null=True)
    mova = models.CharField(max_length=100, blank=True, null=True)
    apow = models.CharField(max_length=100, blank=True, null=True)
    null = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'OLD_m2m_router'


class OldMigrations(models.Model):
    migration = models.CharField(max_length=255)
    batch = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'OLD_migrations'


class OldModbus(models.Model):
    id_root = models.ForeignKey('OldRoot', models.DO_NOTHING, db_column='id_root', blank=True, null=True)
    p = models.CharField(max_length=50, blank=True, null=True)
    st = models.CharField(max_length=50, blank=True, null=True)
    id_name_valor = models.ForeignKey('OldModbusNameValor', models.DO_NOTHING, db_column='id_name_valor', blank=True, null=True)
    valor = models.CharField(max_length=50, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'OLD_modbus'


class OldModbusNameValor(models.Model):
    name = models.CharField(max_length=20, blank=True, null=True)
    descripcion = models.CharField(max_length=100, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'OLD_modbus_name_valor'


class OldModbusP2Copy(models.Model):
    id = models.IntegerField(primary_key=True)
    imei = models.TextField(blank=True, null=True)
    ts = models.DateTimeField(blank=True, null=True)
    st = models.CharField(max_length=100, blank=True, null=True)
    pass_field = models.CharField(db_column='pass', max_length=100, blank=True, null=True)  # Field renamed because it was a Python reserved word.
    st2 = models.CharField(max_length=100, blank=True, null=True)
    add = models.CharField(max_length=100, blank=True, null=True)
    i1 = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'OLD_modbus_p2_copy'


class OldParameterAlertaCopy(models.Model):
    id_device = models.IntegerField(blank=True, null=True)
    id_type_alert_data = models.IntegerField(blank=True, null=True)
    valor = models.DecimalField(max_digits=7, decimal_places=2, blank=True, null=True)
    mensaje_maximo = models.CharField(max_length=100, blank=True, null=True)
    valor_minimo = models.DecimalField(max_digits=7, decimal_places=2, blank=True, null=True)
    mensaje_minimo = models.CharField(max_length=100, blank=True, null=True)
    valor_sms_n1 = models.IntegerField(blank=True, null=True)
    valor_sms_n2 = models.IntegerField(blank=True, null=True)
    valor_sms_n3 = models.IntegerField(blank=True, null=True)
    valor_sms_n4 = models.IntegerField(blank=True, null=True)
    estado = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'OLD_parameter_alerta_copy'


class OldParameterConfig(models.Model):
    id_device = models.ForeignKey('Devices', models.DO_NOTHING, db_column='id_device', blank=True, null=True)
    name = models.CharField(max_length=200, blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    created_user = models.IntegerField(blank=True, null=True)
    updated_user = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'OLD_parameter_config'


class OldPasswordResets(models.Model):
    email = models.CharField(max_length=200, blank=True, null=True)
    name = models.CharField(max_length=200, blank=True, null=True)
    token = models.CharField(max_length=200, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'OLD_password_resets'


class OldPermitsModules(models.Model):
    id_module = models.ForeignKey('Modules', models.DO_NOTHING, db_column='id_module', blank=True, null=True)
    id_perfil = models.ForeignKey('Perfiles', models.DO_NOTHING, db_column='id_perfil', blank=True, null=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    created_user = models.IntegerField(blank=True, null=True)
    updated_user = models.IntegerField(blank=True, null=True)
    state = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'OLD_permits_modules'


class OldPermitsOptions(models.Model):
    id_module = models.ForeignKey('Modules', models.DO_NOTHING, db_column='id_module', blank=True, null=True)
    id_option = models.ForeignKey('Options', models.DO_NOTHING, db_column='id_option', blank=True, null=True)
    id_perfil = models.ForeignKey('Perfiles', models.DO_NOTHING, db_column='id_perfil', blank=True, null=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    created_user = models.IntegerField(blank=True, null=True)
    updated_user = models.IntegerField(blank=True, null=True)
    state = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'OLD_permits_options'


class OldPrivilegios(models.Model):
    id_priv = models.IntegerField(blank=True, null=True)
    name = models.CharField(max_length=250, blank=True, null=True)
    state = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'OLD_privilegios'


class OldProjects(models.Model):
    id_company = models.ForeignKey('Company', models.DO_NOTHING, db_column='id_company', blank=True, null=True)
    id_type_project = models.ForeignKey('OldTypeProjects', models.DO_NOTHING, db_column='id_type_project', blank=True, null=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    responsible = models.CharField(max_length=100, blank=True, null=True)
    state = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    created_user = models.IntegerField(blank=True, null=True)
    updated_user = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'OLD_projects'


class OldRoot(models.Model):
    imei = models.TextField()
    ts = models.DateTimeField()
    p = models.CharField(max_length=50)
    type = models.CharField(max_length=50, blank=True, null=True)
    tem = models.CharField(max_length=100, blank=True, null=True)
    temh = models.IntegerField(blank=True, null=True)
    teml = models.IntegerField(blank=True, null=True)
    teme = models.IntegerField(blank=True, null=True)
    mova = models.IntegerField(blank=True, null=True)
    io1 = models.IntegerField(blank=True, null=True)
    io2 = models.IntegerField(blank=True, null=True)
    io3 = models.IntegerField(blank=True, null=True)
    io4 = models.IntegerField(blank=True, null=True)
    io5 = models.IntegerField(blank=True, null=True)
    io6 = models.IntegerField(blank=True, null=True)
    io7 = models.IntegerField(blank=True, null=True)
    io8 = models.IntegerField(blank=True, null=True)
    io9 = models.IntegerField(blank=True, null=True)
    io10 = models.IntegerField(blank=True, null=True)
    ad1 = models.CharField(max_length=50, blank=True, null=True)
    ad2 = models.CharField(max_length=50, blank=True, null=True)
    ser = models.TextField(blank=True, null=True)
    apow = models.IntegerField(blank=True, null=True)
    modbus = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'OLD_root'


class OldTempActu(models.Model):
    limite_umbral = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    valor = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    id_device = models.IntegerField(blank=True, null=True)
    id = models.IntegerField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'OLD_temp_actu'


class OldTypeProjects(models.Model):
    name = models.CharField(max_length=50, blank=True, null=True)
    description = models.CharField(max_length=100, blank=True, null=True)
    state = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    created_user = models.IntegerField(blank=True, null=True)
    updated_user = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'OLD_type_projects'


class OldWav1(models.Model):
    imei = models.TextField(blank=True, null=True)
    ts = models.DateTimeField(blank=True, null=True)
    pass_field = models.CharField(db_column='pass', max_length=100, blank=True, null=True)  # Field renamed because it was a Python reserved word.
    type = models.CharField(max_length=100, blank=True, null=True)
    apow = models.CharField(max_length=100, blank=True, null=True)
    mac = models.CharField(max_length=100, blank=True, null=True)
    bat = models.CharField(max_length=100, blank=True, null=True)
    ac1 = models.CharField(max_length=100, blank=True, null=True)
    ac2 = models.CharField(max_length=100, blank=True, null=True)
    ac3 = models.CharField(max_length=100, blank=True, null=True)
    ac4 = models.CharField(max_length=100, blank=True, null=True)
    ct1 = models.CharField(max_length=100, blank=True, null=True)
    ct2 = models.CharField(max_length=100, blank=True, null=True)
    ct3 = models.CharField(max_length=100, blank=True, null=True)
    ct4 = models.CharField(max_length=100, blank=True, null=True)
    i1 = models.CharField(max_length=100, blank=True, null=True)
    i2 = models.CharField(max_length=100, blank=True, null=True)
    i3 = models.CharField(max_length=100, blank=True, null=True)
    i4 = models.CharField(max_length=100, blank=True, null=True)
    i5 = models.CharField(max_length=100, blank=True, null=True)
    i6 = models.CharField(max_length=100, blank=True, null=True)
    i7 = models.CharField(max_length=100, blank=True, null=True)
    i8 = models.CharField(max_length=100, blank=True, null=True)
    i9 = models.CharField(max_length=100, blank=True, null=True)
    i10 = models.CharField(max_length=100, blank=True, null=True)
    ad1 = models.CharField(max_length=100, blank=True, null=True)
    ad2 = models.CharField(max_length=100, blank=True, null=True)
    st = models.CharField(max_length=100, blank=True, null=True)
    add = models.CharField(max_length=100, blank=True, null=True)
    v1 = models.CharField(max_length=100, blank=True, null=True)
    v2 = models.CharField(max_length=100, blank=True, null=True)
    v3 = models.CharField(max_length=100, blank=True, null=True)
    v4 = models.CharField(max_length=100, blank=True, null=True)
    v5 = models.CharField(max_length=100, blank=True, null=True)
    v6 = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'OLD_wav1'


class Accesos(models.Model):
    id_accesos = models.AutoField(primary_key=True)
    id_perfil = models.IntegerField()
    id_menu = models.IntegerField()
    agregar = models.IntegerField(blank=True, null=True)
    editar = models.IntegerField(blank=True, null=True)
    eliminar = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'accesos'


class Audit(models.Model):
    id_user = models.IntegerField(blank=True, null=True)
    id_objeto = models.IntegerField(blank=True, null=True)
    id_tabla = models.CharField(max_length=50, blank=True, null=True)
    tabla = models.CharField(max_length=50, blank=True, null=True)
    campo = models.CharField(max_length=45, blank=True, null=True)
    old_value = models.CharField(max_length=128, blank=True, null=True)
    new_value = models.CharField(max_length=128, blank=True, null=True)
    fecha = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'audit'


class AuditParameterAlerta(models.Model):
    id_device = models.ForeignKey('Devices', models.DO_NOTHING, db_column='id_device', blank=True, null=True)
    id_type_alert_data = models.ForeignKey('TypeAlertData', models.DO_NOTHING, db_column='id_type_alert_data', blank=True, null=True)
    valor = models.DecimalField(max_digits=7, decimal_places=2, blank=True, null=True)
    mensaje_maximo = models.CharField(max_length=100, blank=True, null=True)
    valor_minimo = models.DecimalField(max_digits=7, decimal_places=2, blank=True, null=True)
    mensaje_minimo = models.CharField(max_length=100, blank=True, null=True)
    valor_sms_n1 = models.DecimalField(max_digits=3, decimal_places=1, blank=True, null=True)
    valor_sms_n2 = models.DecimalField(max_digits=3, decimal_places=1, blank=True, null=True)
    valor_sms_n3 = models.DecimalField(max_digits=3, decimal_places=1, blank=True, null=True)
    valor_sms_n4 = models.DecimalField(max_digits=3, decimal_places=1, blank=True, null=True)
    valor_sms_n5 = models.DecimalField(max_digits=3, decimal_places=1, blank=True, null=True)
    estado = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    user_id = models.IntegerField(blank=True, null=True)
    valor_aes = models.CharField(max_length=128, blank=True, null=True)
    mensaje_maximo_aes = models.CharField(max_length=128, blank=True, null=True)
    valor_minimo_aes = models.CharField(max_length=128, blank=True, null=True)
    mensaje_minimo_aes = models.CharField(max_length=128, blank=True, null=True)
    valor_sms_n1_aes = models.CharField(max_length=128, blank=True, null=True)
    valor_sms_n2_aes = models.CharField(max_length=128, blank=True, null=True)
    valor_sms_n3_aes = models.CharField(max_length=128, blank=True, null=True)
    valor_sms_n4_aes = models.CharField(max_length=128, blank=True, null=True)
    valor_sms_n5_aes = models.CharField(max_length=128, blank=True, null=True)
    estado_aes = models.CharField(max_length=128, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'audit_parameter_alerta'


class AuditUsers(models.Model):
    id_company = models.ForeignKey('Company', models.DO_NOTHING, db_column='id_company', blank=True, null=True)
    id_perfil = models.ForeignKey('Perfiles', models.DO_NOTHING, db_column='id_perfil', blank=True, null=True)
    id_type_state_user = models.ForeignKey('TypeStateUser', models.DO_NOTHING, db_column='id_type_state_user', blank=True, null=True)
    name = models.CharField(max_length=255)
    lastname = models.CharField(unique=True, max_length=255)
    address = models.CharField(max_length=200, blank=True, null=True)
    cargo = models.CharField(max_length=50, blank=True, null=True)
    email = models.CharField(unique=True, max_length=255)
    pass_field = models.CharField(db_column='pass', max_length=255)  # Field renamed because it was a Python reserved word.
    password = models.CharField(max_length=255, blank=True, null=True)
    remember_token = models.CharField(max_length=100, blank=True, null=True)
    sw_alert = models.IntegerField()
    level = models.IntegerField(blank=True, null=True)
    active = models.IntegerField(blank=True, null=True)
    key_verificar_pass = models.CharField(max_length=200, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    created_user = models.IntegerField(blank=True, null=True)
    updated_user = models.IntegerField(blank=True, null=True)
    user_id = models.IntegerField(blank=True, null=True)
    name_aes = models.CharField(max_length=128, blank=True, null=True)
    lastname_aes = models.CharField(max_length=128, blank=True, null=True)
    address_aes = models.CharField(max_length=128, blank=True, null=True)
    cargo_aes = models.CharField(max_length=128, blank=True, null=True)
    email_aes = models.CharField(max_length=128, blank=True, null=True)
    pass_aes = models.CharField(max_length=128, blank=True, null=True)
    password_aes = models.CharField(max_length=128, blank=True, null=True)
    remenber_token_aes = models.CharField(max_length=128, blank=True, null=True)
    sw_alert_aes = models.CharField(max_length=128, blank=True, null=True)
    level_aes = models.CharField(max_length=128, blank=True, null=True)
    active_aes = models.CharField(max_length=128, blank=True, null=True)
    key_verificar_pass_aes = models.CharField(max_length=128, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'audit_users'
        unique_together = (('id', 'email'),)


class Company(models.Model):
    ruc = models.PositiveIntegerField()
    name_social = models.CharField(max_length=100, blank=True, null=True)
    name_comerce = models.CharField(max_length=100, blank=True, null=True)
    direction = models.CharField(max_length=200, blank=True, null=True)
    responsible = models.CharField(max_length=100, blank=True, null=True)
    state = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    created_user = models.IntegerField(blank=True, null=True)
    updated_user = models.IntegerField(blank=True, null=True)
    ruc_aes = models.CharField(max_length=128, blank=True, null=True)
    name_social_aes = models.CharField(max_length=128, blank=True, null=True)
    direction_aes = models.CharField(max_length=128, blank=True, null=True)
    responsable_aes = models.CharField(max_length=128, blank=True, null=True)
    state_aes = models.CharField(max_length=128, blank=True, null=True)
    name_comerce_aes = models.CharField(max_length=128, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'company'


class DataReadings(models.Model):
    valor = models.DecimalField(max_digits=7, decimal_places=1, blank=True, null=True)
    id_device = models.ForeignKey('Devices', models.DO_NOTHING, db_column='id_device', blank=True, null=True)
    id_identificador = models.IntegerField(blank=True, null=True)
    id_type_alert_data = models.ForeignKey('TypeAlertData', models.DO_NOTHING, db_column='id_type_alert_data', blank=True, null=True)
    estado = models.IntegerField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    created_user = models.IntegerField(blank=True, null=True)
    updated_user = models.IntegerField(blank=True, null=True)
    valor_aes = models.CharField(max_length=128, blank=True, null=True)
    estado_aes = models.CharField(max_length=128, blank=True, null=True)
    description_aes = models.CharField(max_length=128, blank=True, null=True)
    created_at_aes = models.CharField(max_length=128, blank=True, null=True)
    updated_at_aes = models.CharField(max_length=128, blank=True, null=True)
    created_user_aes = models.CharField(max_length=128, blank=True, null=True)
    updated_user_aes = models.CharField(max_length=128, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'data_readings'
        unique_together = (('id_device', 'id_identificador', 'id_type_alert_data', 'created_at'),)


class DataReadings21032020(models.Model):
    id = models.IntegerField(primary_key=True)
    valor = models.DecimalField(max_digits=7, decimal_places=1, blank=True, null=True)
    id_device = models.IntegerField(blank=True, null=True)
    id_identificador = models.IntegerField(blank=True, null=True)
    id_type_alert_data = models.IntegerField(blank=True, null=True)
    estado = models.IntegerField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    created_user = models.IntegerField(blank=True, null=True)
    updated_user = models.IntegerField(blank=True, null=True)
    valor_aes = models.CharField(max_length=128, blank=True, null=True)
    estado_aes = models.CharField(max_length=128, blank=True, null=True)
    description_aes = models.CharField(max_length=128, blank=True, null=True)
    created_at_aes = models.CharField(max_length=128, blank=True, null=True)
    updated_at_aes = models.CharField(max_length=128, blank=True, null=True)
    created_user_aes = models.CharField(max_length=128, blank=True, null=True)
    updated_user_aes = models.CharField(max_length=128, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'data_readings_21032020'


class DataReadingsCopy(models.Model):
    id = models.IntegerField(primary_key=True)
    valor = models.DecimalField(max_digits=7, decimal_places=1, blank=True, null=True)
    id_device = models.IntegerField(blank=True, null=True)
    id_identificador = models.IntegerField(blank=True, null=True)
    id_type_alert_data = models.IntegerField(blank=True, null=True)
    estado = models.IntegerField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    created_user = models.IntegerField(blank=True, null=True)
    updated_user = models.IntegerField(blank=True, null=True)
    valor_aes = models.CharField(max_length=128, blank=True, null=True)
    estado_aes = models.CharField(max_length=128, blank=True, null=True)
    description_aes = models.CharField(max_length=128, blank=True, null=True)
    created_at_aes = models.CharField(max_length=128, blank=True, null=True)
    updated_at_aes = models.CharField(max_length=128, blank=True, null=True)
    created_user_aes = models.CharField(max_length=128, blank=True, null=True)
    updated_user_aes = models.CharField(max_length=128, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'data_readings_copy'


class DataReadingsDiario(models.Model):
    hora = models.TimeField(blank=True, null=True)
    c1_a = models.DecimalField(max_digits=6, decimal_places=1, blank=True, null=True)
    c1_b = models.DecimalField(max_digits=6, decimal_places=1, blank=True, null=True)
    c1_p = models.DecimalField(max_digits=6, decimal_places=1, blank=True, null=True)
    c2_a = models.DecimalField(max_digits=6, decimal_places=1, blank=True, null=True)
    c2_b = models.DecimalField(max_digits=6, decimal_places=1, blank=True, null=True)
    c2_p = models.DecimalField(max_digits=6, decimal_places=1, blank=True, null=True)
    c3_a = models.DecimalField(max_digits=6, decimal_places=1, blank=True, null=True)
    c3_b = models.DecimalField(max_digits=6, decimal_places=1, blank=True, null=True)
    c3_p = models.DecimalField(max_digits=6, decimal_places=1, blank=True, null=True)
    c5_a = models.DecimalField(max_digits=6, decimal_places=1, blank=True, null=True)
    c5_b = models.DecimalField(max_digits=6, decimal_places=1, blank=True, null=True)
    c5_p = models.DecimalField(max_digits=6, decimal_places=1, blank=True, null=True)
    c4_a = models.DecimalField(max_digits=6, decimal_places=1, blank=True, null=True)
    c4_b = models.DecimalField(max_digits=6, decimal_places=1, blank=True, null=True)
    c4_p = models.DecimalField(max_digits=6, decimal_places=1, blank=True, null=True)
    c12_a = models.DecimalField(max_digits=6, decimal_places=1, blank=True, null=True)
    c12_b = models.DecimalField(max_digits=6, decimal_places=1, blank=True, null=True)
    c12_p = models.DecimalField(max_digits=6, decimal_places=1, blank=True, null=True)
    c11_a = models.DecimalField(max_digits=6, decimal_places=1, blank=True, null=True)
    c11_b = models.DecimalField(max_digits=6, decimal_places=1, blank=True, null=True)
    c11_p = models.DecimalField(max_digits=6, decimal_places=1, blank=True, null=True)
    c10_a = models.DecimalField(max_digits=6, decimal_places=1, blank=True, null=True)
    c10_b = models.DecimalField(max_digits=6, decimal_places=1, blank=True, null=True)
    c10_p = models.DecimalField(max_digits=6, decimal_places=1, blank=True, null=True)
    c9_a = models.DecimalField(max_digits=6, decimal_places=1, blank=True, null=True)
    c9_b = models.DecimalField(max_digits=6, decimal_places=1, blank=True, null=True)
    c9_p = models.DecimalField(max_digits=6, decimal_places=1, blank=True, null=True)
    c8_a = models.DecimalField(max_digits=6, decimal_places=1, blank=True, null=True)
    c8_b = models.DecimalField(max_digits=6, decimal_places=1, blank=True, null=True)
    c8_p = models.DecimalField(max_digits=6, decimal_places=1, blank=True, null=True)
    c6_a = models.DecimalField(max_digits=6, decimal_places=1, blank=True, null=True)
    c6_b = models.DecimalField(max_digits=6, decimal_places=1, blank=True, null=True)
    c6_p = models.DecimalField(max_digits=6, decimal_places=1, blank=True, null=True)
    c7_a = models.DecimalField(max_digits=6, decimal_places=1, blank=True, null=True)
    c7_b = models.DecimalField(max_digits=6, decimal_places=1, blank=True, null=True)
    c7_p = models.DecimalField(max_digits=6, decimal_places=1, blank=True, null=True)
    fecha = models.DateField(blank=True, null=True)
    fecha_hora = models.DateTimeField(blank=True, null=True)
    hora_aes = models.CharField(max_length=128, blank=True, null=True)
    c1_a_aes = models.CharField(max_length=128, blank=True, null=True)
    c1_b_aes = models.CharField(max_length=128, blank=True, null=True)
    c1_p_aes = models.CharField(max_length=128, blank=True, null=True)
    c2_a_aes = models.CharField(max_length=128, blank=True, null=True)
    c2_b_aes = models.CharField(max_length=128, blank=True, null=True)
    c2_p_aes = models.CharField(max_length=128, blank=True, null=True)
    c3_a_aes = models.CharField(max_length=128, blank=True, null=True)
    c3_b_aes = models.CharField(max_length=128, blank=True, null=True)
    c3_p_aes = models.CharField(max_length=128, blank=True, null=True)
    c5_a_aes = models.CharField(max_length=128, blank=True, null=True)
    c5_b_aes = models.CharField(max_length=128, blank=True, null=True)
    c5_p_aes = models.CharField(max_length=128, blank=True, null=True)
    c4_a_aes = models.CharField(max_length=128, blank=True, null=True)
    c4_b_aes = models.CharField(max_length=128, blank=True, null=True)
    c4_p_aes = models.CharField(max_length=128, blank=True, null=True)
    c12_a_aes = models.CharField(max_length=128, blank=True, null=True)
    c12_b_aes = models.CharField(max_length=128, blank=True, null=True)
    c12_p_aes = models.CharField(max_length=128, blank=True, null=True)
    c11_a_aes = models.CharField(max_length=128, blank=True, null=True)
    c11_b_aes = models.CharField(max_length=128, blank=True, null=True)
    c11_p_aes = models.CharField(max_length=128, blank=True, null=True)
    c10_a_aes = models.CharField(max_length=128, blank=True, null=True)
    c10_b_aes = models.CharField(max_length=128, blank=True, null=True)
    c10_p_aes = models.CharField(max_length=128, blank=True, null=True)
    c9_a_aes = models.CharField(max_length=128, blank=True, null=True)
    c9_b_aes = models.CharField(max_length=128, blank=True, null=True)
    c9_p_aes = models.CharField(max_length=128, blank=True, null=True)
    c8_a_aes = models.CharField(max_length=128, blank=True, null=True)
    c8_b_aes = models.CharField(max_length=128, blank=True, null=True)
    c8_p_aes = models.CharField(max_length=128, blank=True, null=True)
    c7_a_aes = models.CharField(max_length=128, blank=True, null=True)
    c7_b_aes = models.CharField(max_length=128, blank=True, null=True)
    c7_p_aes = models.CharField(max_length=128, blank=True, null=True)
    fecha_aes = models.CharField(max_length=128, blank=True, null=True)
    fecha_hora_aes = models.CharField(max_length=128, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'data_readings_diario'
        unique_together = (('hora', 'fecha'),)


class Devices(models.Model):
    id = models.IntegerField(primary_key=True)
    id_identificacion = models.IntegerField(blank=True, null=True)
    id_type_device = models.ForeignKey('TypeDevices', models.DO_NOTHING, db_column='id_type_device', blank=True, null=True)
    id_tipo_componente = models.CharField(max_length=255, blank=True, null=True)
    orden = models.IntegerField(blank=True, null=True)
    agrupado = models.CharField(max_length=100, blank=True, null=True)
    ubicacion = models.CharField(max_length=200, blank=True, null=True)
    description = models.CharField(max_length=225, blank=True, null=True)
    state = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    valor_maximo = models.DecimalField(max_digits=7, decimal_places=1, blank=True, null=True)
    valor_minimo = models.DecimalField(max_digits=7, decimal_places=1, blank=True, null=True)
    valor_promedio = models.DecimalField(max_digits=7, decimal_places=1, blank=True, null=True)
    ultimo_fecha = models.DateTimeField(blank=True, null=True)
    ultimo_valor = models.DecimalField(max_digits=7, decimal_places=1, blank=True, null=True)
    created_user = models.IntegerField(blank=True, null=True)
    updated_user = models.IntegerField(blank=True, null=True)
    valor_calibracion = models.DecimalField(max_digits=4, decimal_places=1, blank=True, null=True)
    sms_agrupado = models.CharField(max_length=100, blank=True, null=True)
    data_readings_diario = models.CharField(max_length=10, blank=True, null=True)
    data_readings_diario_p = models.CharField(max_length=10, blank=True, null=True)
    id_sucursal = models.IntegerField(blank=True, null=True)
    total_devices = models.IntegerField(blank=True, null=True)
    id_plano = models.IntegerField(blank=True, null=True)
    total_componentes = models.IntegerField(blank=True, null=True)
    orden_aes = models.CharField(max_length=128, blank=True, null=True)
    agrupado_aes = models.CharField(max_length=128, blank=True, null=True)
    ubicacion_aes = models.CharField(max_length=128, blank=True, null=True)
    description_aes = models.CharField(max_length=128, blank=True, null=True)
    state_aes = models.CharField(max_length=128, blank=True, null=True)
    valor_maximo_aes = models.CharField(max_length=128, blank=True, null=True)
    valor_minimo_aes = models.CharField(max_length=128, blank=True, null=True)
    valor_promedio_aes = models.CharField(max_length=128, blank=True, null=True)
    ultimo_fecha_aes = models.CharField(max_length=128, blank=True, null=True)
    ultimo_valor_aes = models.CharField(max_length=128, blank=True, null=True)
    valor_calibracion_aes = models.CharField(max_length=128, blank=True, null=True)
    sms_agrupado_aes = models.CharField(max_length=128, blank=True, null=True)
    data_readings_diario_aes = models.CharField(max_length=128, blank=True, null=True)
    data_readings_diario_p_aes = models.CharField(max_length=128, blank=True, null=True)
    total_alertas_xdia = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'devices'
        verbose_name = 'device'
        verbose_name_plural = 'devices'
        ordering = ['agrupado']
    
    def __str__(self):
        return self.ubicacion


class DevicesApago(models.Model):
    id_devices_apagado = models.AutoField(primary_key=True)
    id_devices = models.IntegerField(unique=True, blank=True, null=True)
    hora_apagado = models.DateTimeField(blank=True, null=True)
    hora_prendido = models.DateTimeField(blank=True, null=True)
    hora_apagado_aes = models.CharField(max_length=128, blank=True, null=True)
    hora_prendido_aes = models.CharField(max_length=128, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'devices_apago'


class DevicesApagoHist(models.Model):
    id_devices_apagado_hist = models.AutoField(primary_key=True)
    hora_registro = models.DateTimeField(blank=True, null=True)
    id_devices = models.IntegerField(blank=True, null=True)
    hora_apagado = models.DateTimeField(blank=True, null=True)
    hora_prendido = models.DateTimeField(blank=True, null=True)
    hora_registro_aes = models.CharField(max_length=128, blank=True, null=True)
    hora_apagado_aes = models.CharField(max_length=128, blank=True, null=True)
    hora_prendido_aes = models.CharField(max_length=128, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'devices_apago_hist'


class DigitalAlerts(models.Model):
    id_type_alert_data = models.ForeignKey('TypeAlertData', models.DO_NOTHING, db_column='id_type_alert_data', blank=True, null=True)
    id_device = models.ForeignKey(Devices, models.DO_NOTHING, db_column='id_device', blank=True, null=True)
    descripcion = models.CharField(max_length=255, blank=True, null=True)
    valor = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    limite_umbral = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    estado = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    fecha = models.DateField(blank=True, null=True)
    min_max = models.CharField(max_length=20, blank=True, null=True)
    descripcion_aes = models.CharField(max_length=128, blank=True, null=True)
    valor_aes = models.CharField(max_length=128, blank=True, null=True)
    limite_umbral_aes = models.CharField(max_length=128, blank=True, null=True)
    estado_aes = models.CharField(max_length=128, blank=True, null=True)
    fecha_aes = models.CharField(max_length=128, blank=True, null=True)
    min_max_aes = models.CharField(max_length=128, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'digital_alerts'


class DigitalAlertsCopy(models.Model):
    id_type_alert_data = models.IntegerField(blank=True, null=True)
    id_device = models.IntegerField(blank=True, null=True)
    descripcion = models.CharField(max_length=255, blank=True, null=True)
    valor = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    limite_umbral = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    estado = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    fecha = models.DateField(blank=True, null=True)
    min_max = models.CharField(max_length=20, blank=True, null=True)
    descripcion_aes = models.CharField(max_length=128, blank=True, null=True)
    valor_aes = models.CharField(max_length=128, blank=True, null=True)
    limite_umbral_aes = models.CharField(max_length=128, blank=True, null=True)
    estado_aes = models.CharField(max_length=128, blank=True, null=True)
    fecha_aes = models.CharField(max_length=128, blank=True, null=True)
    min_max_aes = models.CharField(max_length=128, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'digital_alerts_copy'


class LevelAlertSms(models.Model):
    name = models.CharField(max_length=50, blank=True, null=True)
    name_aes = models.CharField(max_length=128, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'level_alert_sms'


class M2MNotificar(models.Model):
    id_notificar = models.AutoField(primary_key=True)
    celular = models.CharField(max_length=50, blank=True, null=True)
    email = models.CharField(max_length=30, blank=True, null=True)
    mensaje = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'm2m_notificar'


class M2MNotificarLog(models.Model):
    id_notificar = models.IntegerField(blank=True, null=True)
    celular = models.CharField(max_length=50, blank=True, null=True)
    email = models.CharField(max_length=30, blank=True, null=True)
    mensaje = models.TextField(blank=True, null=True)
    fecha_envio = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'm2m_notificar_log'


class Menu(models.Model):
    id_menu = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    submenu = models.IntegerField()
    cierre = models.IntegerField()
    icono = models.CharField(max_length=50)
    pagina = models.CharField(max_length=50)
    orden = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'menu'


class ModbusP2(models.Model):
    id = models.AutoField(primary_key=True)
    imei = models.TextField(blank=True, null=True)
    ts = models.DateTimeField(blank=True, null=True)
    st = models.CharField(max_length=100, blank=True, null=True)
    pass_field = models.CharField(db_column='pass', max_length=100, blank=True, null=True)  # Field renamed because it was a Python reserved word.
    st2 = models.CharField(max_length=100, blank=True, null=True)
    add = models.CharField(max_length=100, blank=True, null=True)
    i1 = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'modbus_p2'


class ModbusP2Copy(models.Model):
    id = models.IntegerField(primary_key=True)
    imei = models.TextField(blank=True, null=True)
    ts = models.DateTimeField(blank=True, null=True)
    st = models.CharField(max_length=100, blank=True, null=True)
    pass_field = models.CharField(db_column='pass', max_length=100, blank=True, null=True)  # Field renamed because it was a Python reserved word.
    st2 = models.CharField(max_length=100, blank=True, null=True)
    add = models.CharField(max_length=100, blank=True, null=True)
    i1 = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'modbus_p2_copy'


class Modules(models.Model):
    name = models.CharField(max_length=99, blank=True, null=True)
    url = models.CharField(max_length=250, blank=True, null=True)
    icono = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    created_user = models.IntegerField(blank=True, null=True)
    updated_user = models.IntegerField(blank=True, null=True)
    state = models.IntegerField(blank=True, null=True)
    ico = models.CharField(max_length=100, blank=True, null=True)
    name_aes = models.CharField(max_length=128, blank=True, null=True)
    url_aes = models.CharField(max_length=128, blank=True, null=True)
    icono_aes = models.CharField(max_length=128, blank=True, null=True)
    created_at_aes = models.CharField(max_length=128, blank=True, null=True)
    updated_at_aes = models.CharField(max_length=128, blank=True, null=True)
    created_user_aes = models.CharField(max_length=128, blank=True, null=True)
    updated_user_aes = models.CharField(max_length=128, blank=True, null=True)
    state_aes = models.CharField(max_length=128, blank=True, null=True)
    ico_aes = models.CharField(max_length=128, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'modules'


class Notifications(models.Model):
    id_device = models.ForeignKey(Devices, models.DO_NOTHING, db_column='id_device', blank=True, null=True)
    valor_max = models.IntegerField(blank=True, null=True)
    valor_min = models.IntegerField(blank=True, null=True)
    nivel_not = models.IntegerField(blank=True, null=True)
    valor_max_aes = models.CharField(max_length=128, blank=True, null=True)
    valor_min_aes = models.CharField(max_length=128, blank=True, null=True)
    nivel_not_aes = models.CharField(max_length=128, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'notifications'


class Options(models.Model):
    id_modules = models.ForeignKey(Modules, models.DO_NOTHING, db_column='id_modules', blank=True, null=True)
    name = models.CharField(max_length=150, blank=True, null=True)
    ruta = models.CharField(max_length=250, blank=True, null=True)
    icono = models.CharField(max_length=250, blank=True, null=True)
    id_permits = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    created_user = models.IntegerField(blank=True, null=True)
    updated_user = models.IntegerField(blank=True, null=True)
    state = models.IntegerField(blank=True, null=True)
    ico = models.CharField(max_length=100, blank=True, null=True)
    name_aes = models.CharField(max_length=128, blank=True, null=True)
    ruta_aes = models.CharField(max_length=128, blank=True, null=True)
    icono_aes = models.CharField(max_length=128, blank=True, null=True)
    created_at_aes = models.CharField(max_length=128, blank=True, null=True)
    updated_at_aes = models.CharField(max_length=128, blank=True, null=True)
    created_user_aes = models.CharField(max_length=128, blank=True, null=True)
    updated_user_aes = models.CharField(max_length=128, blank=True, null=True)
    state_aes = models.CharField(max_length=128, blank=True, null=True)
    ico_aes = models.CharField(max_length=128, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'options'


class ParameterAlerta(models.Model):
    id_device = models.ForeignKey(Devices, models.DO_NOTHING, db_column='id_device', blank=True, null=True)
    id_type_alert_data = models.ForeignKey('TypeAlertData', models.DO_NOTHING, db_column='id_type_alert_data', blank=True, null=True)
    valor = models.DecimalField(max_digits=7, decimal_places=2, blank=True, null=True)
    mensaje_maximo = models.CharField(max_length=100, blank=True, null=True)
    valor_minimo = models.DecimalField(max_digits=7, decimal_places=2, blank=True, null=True)
    mensaje_minimo = models.CharField(max_length=100, blank=True, null=True)
    valor_sms_n1 = models.DecimalField(max_digits=3, decimal_places=1, blank=True, null=True)
    valor_sms_n2 = models.DecimalField(max_digits=3, decimal_places=1, blank=True, null=True)
    valor_sms_n3 = models.DecimalField(max_digits=3, decimal_places=1, blank=True, null=True)
    valor_sms_n4 = models.DecimalField(max_digits=3, decimal_places=1, blank=True, null=True)
    valor_sms_n5 = models.DecimalField(max_digits=3, decimal_places=1, blank=True, null=True)
    estado = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    valor_aes = models.CharField(max_length=128, blank=True, null=True)
    mensaje_maximo_aes = models.CharField(max_length=128, blank=True, null=True)
    valor_minimo_aes = models.CharField(max_length=128, blank=True, null=True)
    mensaje_minimo_aes = models.CharField(max_length=128, blank=True, null=True)
    valor_sms_n1_aes = models.CharField(max_length=128, blank=True, null=True)
    valor_sms_n2_aes = models.CharField(max_length=128, blank=True, null=True)
    valor_sms_n3_aes = models.CharField(max_length=128, blank=True, null=True)
    valor_sms_n4_aes = models.CharField(max_length=128, blank=True, null=True)
    valor_sms_n5_aes = models.CharField(max_length=128, blank=True, null=True)
    estado_aes = models.CharField(max_length=128, blank=True, null=True)
    uinsert_id = models.IntegerField(blank=True, null=True)
    uupdate_id = models.IntegerField(blank=True, null=True)
    ucancel_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'parameter_alerta'


class PerNotification(models.Model):
    id_personal = models.IntegerField(blank=True, null=True)
    id_device = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'per_notification'


class Perfiles(models.Model):
    name = models.CharField(max_length=250, blank=True, null=True)
    estado = models.IntegerField(blank=True, null=True)
    opcion_excel = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    created_user = models.IntegerField(blank=True, null=True)
    updated_user = models.IntegerField(blank=True, null=True)
    name_aes = models.CharField(max_length=128, blank=True, null=True)
    estado_aes = models.CharField(max_length=128, blank=True, null=True)
    created_user_aes = models.CharField(max_length=128, blank=True, null=True)
    updated_user_aes = models.CharField(max_length=128, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'perfiles'


class Permisos(models.Model):
    id_module = models.IntegerField(blank=True, null=True)
    id_option = models.IntegerField(blank=True, null=True)
    id_perfil = models.IntegerField(blank=True, null=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    created_user = models.IntegerField(blank=True, null=True)
    updated_user = models.IntegerField(blank=True, null=True)
    state = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'permisos'


class PermisosCamara(models.Model):
    id_device = models.IntegerField(blank=True, null=True)
    id_usuario = models.IntegerField(blank=True, null=True)
    id_device_aes = models.CharField(max_length=128, blank=True, null=True)
    id_usuario_aes = models.CharField(max_length=128, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'permisos_camara'


class Personal(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    id_level_alert_sms = models.ForeignKey(LevelAlertSms, models.DO_NOTHING, db_column='id_level_alert_sms', blank=True, null=True)
    estado = models.CharField(max_length=20, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    name_aes = models.CharField(max_length=128, blank=True, null=True)
    phone_aes = models.CharField(max_length=128, blank=True, null=True)
    id_level_alert_sms_aes = models.CharField(max_length=128, blank=True, null=True)
    estado_aes = models.CharField(max_length=128, blank=True, null=True)
    created_at_aes = models.CharField(max_length=128, blank=True, null=True)
    updated_at_aes = models.CharField(max_length=128, blank=True, null=True)
    created_user = models.IntegerField(blank=True, null=True)
    updated_user = models.IntegerField(blank=True, null=True)
    email_aes = models.CharField(max_length=128, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'personal'


class PersonalNotification(models.Model):
    id_personal = models.ForeignKey(Personal, models.DO_NOTHING, db_column='id_personal', blank=True, null=True)
    id_device = models.ForeignKey(Devices, models.DO_NOTHING, db_column='id_device', blank=True, null=True)
    id_personal_aes = models.CharField(max_length=128, blank=True, null=True)
    id_device_aes = models.CharField(max_length=128, blank=True, null=True)
    created_user = models.IntegerField(blank=True, null=True)
    updated_user = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'personal_notification'


class Sucursal(models.Model):
    id_sucursal = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=150, blank=True, null=True)
    nombre_aes = models.CharField(max_length=128, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sucursal'
        verbose_name = 'sucursal'
        verbose_name_plural = 'sucursales'


class TempCalculos(models.Model):
    id = models.IntegerField(primary_key=True)
    valor = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    valor_aes = models.CharField(max_length=128, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'temp_calculos'


class TypeAlertData(models.Model):
    descripcion = models.CharField(max_length=255, blank=True, null=True)
    sw_type = models.CharField(max_length=100, blank=True, null=True)
    estado = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'type_alert_data'


class TypeDevices(models.Model):
    id_company = models.ForeignKey(Company, models.DO_NOTHING, db_column='id_company', blank=True, null=True)
    orden = models.IntegerField(db_column='Orden', blank=True, null=True)  # Field name made lowercase.
    name = models.CharField(max_length=50, blank=True, null=True)
    description = models.CharField(max_length=200, blank=True, null=True)
    imei = models.CharField(max_length=40, blank=True, null=True)
    tiempo_lectura = models.CharField(max_length=20, blank=True, null=True)
    fecha_instalacion = models.DateField(blank=True, null=True)
    ubicacion = models.CharField(max_length=50, blank=True, null=True)
    observaciones = models.CharField(max_length=50, blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    created_user = models.IntegerField(blank=True, null=True)
    updated_user = models.IntegerField(blank=True, null=True)
    id_company_aes = models.CharField(max_length=128, blank=True, null=True)
    orden_aes = models.CharField(db_column='Orden_aes', max_length=128, blank=True, null=True)  # Field name made lowercase.
    name_aes = models.CharField(max_length=128, blank=True, null=True)
    description_aes = models.CharField(max_length=128, blank=True, null=True)
    imei_aes = models.CharField(max_length=128, blank=True, null=True)
    tiempo_lectura_aes = models.CharField(max_length=128, blank=True, null=True)
    fecha_instalacion_aes = models.CharField(max_length=128, blank=True, null=True)
    ubicacion_aes = models.CharField(max_length=128, blank=True, null=True)
    observaciones_aes = models.CharField(max_length=128, blank=True, null=True)
    created_user_aes = models.CharField(max_length=128, blank=True, null=True)
    updated_user_aes = models.CharField(max_length=128, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'type_devices'
    
    def __str__(self):
        return self.name


class TypeStateUser(models.Model):
    name = models.CharField(max_length=250, blank=True, null=True)
    state = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    name_aes = models.CharField(max_length=128, blank=True, null=True)
    state_aes = models.CharField(max_length=128, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'type_state_user'


class Users(models.Model):
    id_company = models.ForeignKey(Company, models.DO_NOTHING, db_column='id_company', blank=True, null=True)
    id_perfil = models.ForeignKey(Perfiles, models.DO_NOTHING, db_column='id_perfil', blank=True, null=True)
    id_type_state_user = models.ForeignKey(TypeStateUser, models.DO_NOTHING, db_column='id_type_state_user', blank=True, null=True)
    name = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    address = models.CharField(max_length=200, blank=True, null=True)
    cargo = models.CharField(max_length=50, blank=True, null=True)
    email = models.CharField(max_length=255)
    pass_field = models.CharField(db_column='pass', max_length=255)  # Field renamed because it was a Python reserved word.
    password = models.CharField(max_length=255, blank=True, null=True)
    remember_token = models.CharField(max_length=100, blank=True, null=True)
    sw_alert = models.IntegerField()
    level = models.IntegerField(blank=True, null=True)
    active = models.IntegerField(blank=True, null=True)
    key_verificar_pass = models.CharField(max_length=200, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    created_user = models.IntegerField(blank=True, null=True)
    updated_user = models.IntegerField(blank=True, null=True)
    id_company_aes = models.CharField(max_length=128, blank=True, null=True)
    id_perfil_aes = models.CharField(max_length=128, blank=True, null=True)
    id_type_state_user_aes = models.CharField(max_length=128, blank=True, null=True)
    name_aes = models.CharField(max_length=128, blank=True, null=True)
    lastname_aes = models.CharField(max_length=128, blank=True, null=True)
    address_aes = models.CharField(max_length=128, blank=True, null=True)
    cargo_aes = models.CharField(max_length=128, blank=True, null=True)
    email_aes = models.CharField(unique=True, max_length=128, blank=True, null=True)
    pass_aes = models.CharField(max_length=128, blank=True, null=True)
    password_aes = models.CharField(max_length=128, blank=True, null=True)
    remember_token_aes = models.CharField(max_length=128, blank=True, null=True)
    sw_alert_aes = models.CharField(max_length=128, blank=True, null=True)
    level_aes = models.CharField(max_length=128, blank=True, null=True)
    active_aes = models.CharField(max_length=128, blank=True, null=True)
    key_verificar_pass_aes = models.CharField(max_length=128, blank=True, null=True)
    created_at_aes = models.CharField(max_length=128, blank=True, null=True)
    updated_at_aes = models.CharField(max_length=128, blank=True, null=True)
    created_user_aes = models.CharField(max_length=128, blank=True, null=True)
    updated_user_aes = models.CharField(max_length=128, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'users'
        unique_together = (('id', 'email'),)


class UsersLogin(models.Model):
    user_id = models.IntegerField()
    fecha_hora = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'users_login'
        unique_together = (('id', 'user_id'),)
