import json

# JSON dosyasını oku
with open('dataset/test.json', 'r', encoding='utf-8') as json_file:
    data = json.load(json_file)

# Sadece 'text' alanını al
def extract_texts(data):
    if isinstance(data, dict):  # Eğer veri bir sözlükse
        results = []
        for key, value in data.items():
            if key == "text":  # 'text' anahtarını kontrol et
                results.append({"text": value})
            elif isinstance(value, (dict, list)):  # Sözlük ya da listeyse rekürsif kontrol
                results.extend(extract_texts(value))
        return results
    elif isinstance(data, list):  # Eğer veri bir listeyse
        results = []
        for item in data:
            results.extend(extract_texts(item))
        return results
    return []  # Eğer başka bir şeyse boş liste döndür

texts = extract_texts(data)

# Yeni JSON dosyasına her text'i ayrı bir obje olarak yaz
with open('dataset/texts_separate.json', 'w', encoding='utf-8') as output_file:
    json.dump(texts, output_file, indent=4, ensure_ascii=False)

print(f"Her 'text' alanı ayrı ayrı 'texts_separate.json' dosyasına yazıldı.")
