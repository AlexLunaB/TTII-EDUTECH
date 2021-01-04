


"""Carga Archivos estados-municipios"""
from ObservatorioTTApp.models import MexicoState, MexicoMunicipio
from recursos.models import Recurso

estadowithmunicipio=json.load(open("estados-municipios.json"))
estados=json.load(open("estados.json"))


for estado in estados:
  MexicoState.objects.create(id=estado["clave"],nombre=estado["nombre"])

estadowithmunicipio=json.load(open("estados-municipios.json"))
for estado in estadowithmunicipio:
  print(estado)
  m=MexicoState.objects.get(nombre=estado.upper())
  for municipio in estadowithmunicipio[estado]:
    MexicoMunicipio.objects.create(estado=m,nombre=municipio)




  MexicoMunicipio.objects.create(id=estado["clave"],nombre=estado["nombre"])





"""Graficar"""


"""Esta funcion obtiene los recursos con más tags"""
from collections import defaultdict, Counter
from taggit.models import Tag


tag_frequency = defaultdict(int)
for item in Recurso.objects.filter(estado="CMX"):
    for tag in item.tags.all():
        tag_frequency[tag.name] += 1

Counter(tag_frequency).most_common()



#Retorna la cantidad de recursos a los que pertece cada estado

MexicoState.objects.annotate(Count('recurso')).values()


MexicoState.objects.annotate(Count('recurso')).order_by("-recurso__count").values()
