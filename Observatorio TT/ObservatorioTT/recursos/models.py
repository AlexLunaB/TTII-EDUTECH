from django.db import models

# Create your models here.

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


class Recurso(models.Model):
    nombreRecurso = models.CharField(max_length = 50)
    categoria = models.CharField(max_length = 20)
    entidadFederativa = models.CharField(max_length = 20, choices = ENTIDADES_FEDERATIVAS, default = 'AGS')
    autor = models.CharField(max_length = 100)
    nombreUsuario = models.CharField(max_length = 100)
    fechaCreacion = models.DateTimeField(auto_now_add=True)
    fechaModificacion = models.DateTimeField(auto_now_add=True)
    descripcion = models.CharField(max_length = 250)
    archivo = models.FileField(upload_to='uploads/%Y/%m/%d/')
    # created = models.DateTimeField(auto_now_add=True)
    # updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'recurso'
        verbose_name_plural = 'recursos'

    def __str__(self):
        return self.nombreRecurso