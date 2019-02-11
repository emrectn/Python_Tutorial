import json

"""
    Json bir verinin dosyaya kaydedilmesi
    encoding: dosyaya encode edilme türü
    ensure_ascii: türkçe karakter problemini önlemek için
    indent: dosyaya kaydedilirken tab' boşluk sayısı
"""

data = {'data': 'Hello'}
with open("deneme" + '.json', 'w', encoding='utf8') as f:
    json.dump(data, f, indent=4, ensure_ascii=False)


"""
    Json bir verinin dosyadan yüklenilmesi.
"""

with open("deneme" + '.json', 'r') as f:
    d = json.loads(f.read())
print("Yüklenen: ", d)
