import json

# Dosyayı aç ve oku
with open("dataset/test.json", "r", encoding="utf-8") as file:
    data = json.load(file)  # JSON dosyasını yükle

# İlk 100 elemanı al
sentences = data.get("sentences", {}).get("sentence", [])  # sentence listesini al
first_100_sentences = sentences[:100]  # İlk 100 elemanı al

# Yeni bir JSON yapısı oluştur
new_data = {"sentences": {"sentence": first_100_sentences}}

# Yeni dosyaya kaydet
with open("dataset/first_100_fromtest.json", "w", encoding="utf-8") as file:
    json.dump(new_data, file, ensure_ascii=False, indent=4)

print("İlk 100 eleman 'first_100_fromtest.json' dosyasına kaydedildi.")
