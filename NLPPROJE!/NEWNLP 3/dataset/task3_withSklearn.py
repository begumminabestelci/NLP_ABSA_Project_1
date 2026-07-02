from sklearn.metrics import classification_report
import json

# JSON dosyalarını yükle
def load_json(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return json.load(file)

# Karşılaştırma fonksiyonu
def prepare_data(original, annotated):
    y_true = []  # Gerçek değerler (referans)
    y_pred = []  # Tahmin edilen değerler (annotated)
    
    for orig_sentence, anno_sentence in zip(original["sentences"]["sentence"], annotated):
        original_aspects = {a["@category"]: a["@polarity"] for a in orig_sentence["aspectCategories"]["aspectCategory"]}
        annotated_aspects = {a["aspect"]: a["sentiment"] for a in anno_sentence["aspects"]}
        
        # Gerçek değerleri ekle
        for aspect, sentiment in original_aspects.items():
            y_true.append((aspect, sentiment))
            # Annotated setinde varsa tahmini ekle, yoksa 'None' olarak ekle
            y_pred.append((aspect, annotated_aspects.get(aspect, "None")))
    
    return y_true, y_pred

# Dosya yolları
original_file = "dataset/first_100_fromtest.json"
annotated_file = "dataset/full_annotated_data_cot_claude.json"

# JSON dosyalarını yükle
original_data = load_json(original_file)
annotated_data = load_json(annotated_file)

# Veriyi Hazırla
y_true, y_pred = prepare_data(original_data, annotated_data)

# classification_report için sadece sentiment değerlerini ayır
true_labels = [sentiment for _, sentiment in y_true]
pred_labels = [sentiment for _, sentiment in y_pred]

# Classification report
report = classification_report(true_labels, pred_labels, labels=["positive", "negative", "neutral", "None"], zero_division=0)
print(report)
