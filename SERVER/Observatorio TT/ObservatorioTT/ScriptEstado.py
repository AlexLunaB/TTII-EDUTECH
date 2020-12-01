


"""Carga Archivos estados-municipios"""
from ObservatorioTTApp.models import MexicoState, MexicoMunicipio

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
