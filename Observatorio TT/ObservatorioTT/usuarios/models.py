from django.db import models

# Create your models here.

# Declarando Preferencias

PERMISO_USUARIO = ( 
    ("AD", "Administrador"), 
    ("GE", "General"), 
    ("IN", "Investigador"), 
) 

# Declarando Estados
ENTIDADES_FEDERATIVAS = (
    ( "AGS", "AGUASCALIENTES" ),
    ( "BC",  "BAJA CALIFORNIA" ),
    ( "BCS", "BAJA CALIFORNIA SUR" ),
    ( "CHI", "CHIHUAHUA" ),
    ( "CHS", "CHIAPAS" ),
    ( "CMP", "CAMPECHE" ),
    ( "CMX", "CIUDAD DE MEXICO" ),
    ( "COA", "COAHUILA" ),
    ( "COL", "COLIMA" ),
    ( "DGO", "DURANGO" ),
    ( "GRO", "GUERRERO" ),
    ( "GTO", "GUANAJUATO" ),
    ( "HGO", "HIDALGO" ),
    ( "JAL", "JALISCO" ),
    ( "MCH", "MICHOACAN" ),
    ( "MEX", "ESTADO DE MEXICO" ),
    ( "MOR", "MORELOS" ),
    ( "NAY", "NAYARIT" ),
    ( "NL",  "NUEVO LEON" ),
    ( "OAX", "OAXACA" ),
    ( "PUE", "PUEBLA" ),
    ( "QR",  "QUINTANA ROO" ),
    ( "QRO", "QUERETARO" ),
    ( "SIN", "SINALOA" ),
    ( "SLP", "SAN LUIS POTOSI" ),
    ( "SON", "SONORA" ),
    ( "TAB", "TABASCO" ),
    ( "TLX", "TLAXCALA" ),
    ( "TMS", "TAMAULIPAS" ),
    ( "VER", "VERACRUZ" ),
    ( "YUC", "YUCATAN" ),
    ( "ZAC", "ZACATECAS" ) 
)

class Usuario(models.Model):
    nombre = models.CharField(max_length = 30)
    apellidoPaterno = models.CharField(max_length = 20)
    apellidoMaterno = models.CharField(max_length = 20)
    edad = models.IntegerField()
    correoElectronico = models.EmailField(max_length = 30)
    contraseña = models.CharField(max_length = 20)
    preferencias = models.CharField(max_length = 100)
    permiso = models.CharField(max_length = 20, choices = PERMISO_USUARIO, default = 'GE')
    entidadFederativa = models.CharField(max_length = 20, choices = ENTIDADES_FEDERATIVAS, default = 'AGS')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'usuario'
        verbose_name_plural = 'usuarios'

    def __str__(self):
        return self.nombre
