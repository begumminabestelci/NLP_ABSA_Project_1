import json

# Kaynak JSON dosyasının adı
input_file = "dataset/texts_separate.json"

# Çıktı JSON dosyasının adı
output_file = "dataset/first_100_texts.json"

# JSON dosyasını okuma ve ilk 100 metni yazma işlemi
try:
    # JSON dosyasını okuma
    with open(input_file, "r", encoding="utf-8") as file:
        data = json.load(file)  # JSON içeriğini yükle
    
    # İlk 100 texti alma
    first_100_texts = data[:100]

    # Yeni JSON dosyasına yazma
    with open(output_file, "w", encoding="utf-8") as file:
        json.dump(first_100_texts, file, indent=4, ensure_ascii=False)

    print(f"İlk 100 text {output_file} dosyasına başarıyla kaydedildi.")
except Exception as e:
    print(f"Bir hata oluştu: {e}")
