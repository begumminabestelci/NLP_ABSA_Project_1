import xmltodict
import json

# XML dosyasını okuyun
with open('dataset/test.xml', 'r', encoding='utf-8') as xml_file:
    xml_content = xml_file.read()

# XML'i Python dict'e dönüştür
data_dict = xmltodict.parse(xml_content)

# Python dict'i JSON formatına dönüştür
json_data = json.dumps(data_dict, indent=4, ensure_ascii=False)

# JSON dosyasını yaz
with open('dataset/test.json', 'w', encoding='utf-8') as json_file:
    json_file.write(json_data)

print("Dönüştürme işlemi tamamlandı. 'test.json' dosyası oluşturuldu.")
