import os
import xml.etree.ElementTree as ET

path = ".//XML_files"
dir_list = os.listdir(path)

print("Files and directories in '", path, "' :")
for xml in dir_list :
  print("xml", xml)
  tree = ET.parse(path+"//"+xml)
  root = tree.getroot()
  #print(root.tag)
  for factura in root.findall("./liquidaciones/liquidacion/facturas/factura"):
    print("factura",factura.attrib["fuf"])
    suma = 0.0
    for montto_total in factura.findall("./conceptos/concepto/monto_total"):
      suma += float(montto_total.text)
  
    print("suma $%.2f" % suma)