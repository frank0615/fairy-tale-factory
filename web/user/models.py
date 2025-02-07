from django.db import models

class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'

class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)

class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)

class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'

class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)

class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)

class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'

class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)

class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'

class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'

class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    user_type = models.IntegerField(blank=True, null=True)
    user_name = models.CharField(max_length=50)
    user_nick_name = models.CharField(max_length=50, blank=True, null=True)
    user_password = models.CharField(max_length=16)
    user_email = models.CharField(max_length=255, blank=True, null=True)
    creation_time = models.DateTimeField(blank=True, null=True)
    modification_time = models.DateTimeField(blank=True, null=True)
    disable_time = models.DateTimeField(blank=True, null=True)

    def check_password(self, password):
        return self.user_password == password
    
    class Meta:
        managed = False
        db_table = 'user'

class Prompt(models.Model):
    prompt_id = models.PositiveIntegerField(primary_key=True)
    prompt_name = models.CharField(max_length=50)
    version_code = models.PositiveIntegerField(blank=True, null=True)
    version_desc = models.CharField(max_length=255, blank=True, null=True)
    prompt_content = models.CharField(max_length=2000)
    developer = models.ForeignKey('User', models.DO_NOTHING, blank=True, null=True)
    creation_time = models.DateTimeField(blank=True, null=True)
    modification_time = models.DateTimeField(blank=True, null=True)
    disable_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'prompt'

class ApiKey(models.Model):
    key_id = models.PositiveIntegerField(primary_key=True)
    key_name = models.CharField(max_length=50)
    key_password = models.CharField(max_length=255)
    developer = models.ForeignKey('User', models.DO_NOTHING, blank=True, null=True)
    creation_time = models.DateTimeField(blank=True, null=True)
    disable_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'api_key'

class ApiKeyCost(models.Model):
    key = models.OneToOneField(ApiKey, models.DO_NOTHING, primary_key=True)  # The composite primary key (key_id, user_id) found, that is not supported. The first column is selected.
    user = models.ForeignKey('User', models.DO_NOTHING)
    usd_key_cost = models.DecimalField(max_digits=5, decimal_places=2)
    twd_key_cost = models.PositiveSmallIntegerField(blank=True, null=True)
    unit = models.CharField(max_length=6)
    quantity = models.PositiveSmallIntegerField()
    start_time = models.DateTimeField(blank=True, null=True)
    end_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'api_key_cost'
        unique_together = (('key', 'user'),)
