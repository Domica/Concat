import json
import glob
import os

# Pronađi engleski fajl (osnovni)
base_files = glob.glob('**/locales/en.json', recursive=True) + glob.glob('**/locales/en-US.json', recursive=True)
if not base_files:
    print("Ne mogu pronaći engleski locale fajl!")
    exit(1)

base_path = base_files[0]
print(f"Koristim osnovni fajl: {base_path}")

with open(base_path, 'r', encoding='utf-8') as f:
    base_data = json.load(f)

base_keys = set(base_data.keys())

# Pronađi sve ostale locale fajlove
locale_dir = os.path.dirname(base_path)
all_locales = glob.glob(f'{locale_dir}/*.json')

updated = []
for locale_path in all_locales:
    if locale_path == base_path:
        continue
    
    with open(locale_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    original_keys = set(data.keys())
    added = 0
    removed = 0
    
    # Dodaj ključeve koji fale (koristi engleski tekst kao placeholder)
    for key in base_keys:
        if key not in data:
            data[key] = base_data[key]
            added += 1
    
    # Ukloni stale ključeve (kojih više nema u engleskom)
    for key in list(data.keys()):
        if key not in base_keys:
            del data[key]
            removed += 1
    
    if added > 0 or removed > 0:
        with open(locale_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        print(f"✓ {os.path.basename(locale_path)}: dodano {added}, obrisano {removed}")
        updated.append(locale_path)

if not updated:
    print("Svi fajlovi su već sinhronizovani.")
