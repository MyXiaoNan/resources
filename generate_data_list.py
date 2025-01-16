import json
import hashlib
import zipfile
from pathlib import Path

data_path = Path(__file__).parent / "data"
font_path = Path(__file__).parent / "font"
img_path = Path(__file__).parent / "image"
template_path = Path(__file__).parent / "templates"

file_list = [{
    'path': f"{file.parent.name}/{file.name}",
    'hash': hashlib.md5(file.read_bytes()).hexdigest(),
    'lock': True
} for file in font_path.iterdir()]

this_path = str(Path().absolute())

for file in data_path.rglob("*"):
    if not file.is_file():
        continue

    file_list.append({
        'path': str(file.relative_to(this_path)).replace("\\", "/"),
        'hash': hashlib.md5(file.read_bytes()).hexdigest(),
        'lock': True
    })

for file in img_path.rglob("*"):
    if not file.is_file():
        continue

    file_list.append({
        'path': str(file.relative_to(this_path)).replace("\\", "/"),
        'hash': hashlib.md5(file.read_bytes()).hexdigest(),
        'lock': True
    })

for file in template_path.rglob("*"):
    if not file.is_file():
        continue

    file_list.append({
        'path': str(file.relative_to(this_path)).replace("\\", "/"),
        'hash': hashlib.md5(file.read_bytes()).hexdigest(),
        'lock': True
    })

with open('abscension_data_list.json', 'w', encoding='utf-8') as f:
    json.dump(file_list, f, ensure_ascii=False, indent=2)

resources_zip_path = Path() / 'resources.zip'
resources_zip = zipfile.ZipFile(resources_zip_path, 'w', zipfile.ZIP_DEFLATED)

for file in Path('font').iterdir():
    resources_zip.write(file)
for file in Path('data').rglob('*'):
    resources_zip.write(file)
for file in Path('image').rglob('*'):
    resources_zip.write(file)
for file in Path('templates').rglob('*'):
    resources_zip.write(file)

resources_zip.close()
