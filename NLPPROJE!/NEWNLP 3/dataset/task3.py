import json

# JSON dosyalarını yükle
def load_json(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return json.load(file)

# Karşılaştırma fonksiyonu
def compare_annotations(original, annotated):
    total_annotations = 0
    correct_matches = 0
    
    for orig_sentence, anno_sentence in zip(original["sentences"]["sentence"], annotated):
        original_aspects = {a["@category"]: a["@polarity"] for a in orig_sentence["aspectCategories"]["aspectCategory"]}
        annotated_aspects = {a["aspect"]: a["sentiment"] for a in anno_sentence["aspects"]}
        
        total_annotations += len(original_aspects)
        
        for aspect, sentiment in annotated_aspects.items():
            if aspect in original_aspects and original_aspects[aspect] == sentiment:
                correct_matches += 1
    
    success_rate = (correct_matches / total_annotations) * 100
    return success_rate, total_annotations, correct_matches

# Dosya yolları
original_file = "dataset/first_100_fromtest.json"
annotated_file = "dataset/full_annotated_data_cot.json"  # Burada yöntem seçilebilir

# JSON dosyalarını yükle
original_data = load_json(original_file)
annotated_data = load_json(annotated_file)

# Karşılaştırma
success_rate, total_annotations, correct_matches = compare_annotations(original_data, annotated_data)

# Sonuçları yazdır
print(f"Success Rate: {success_rate:.2f}%")
print(f"Total Annotations: {total_annotations}")
print(f"Correct Matches: {correct_matches}")
