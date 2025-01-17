import json
import hashlib
import zipfile
from pathlib import Path

file_list = []

data_path = Path(__file__).parent / "data"
this_path = str(Path().absolute())

for file in data_path.rglob("*"):
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

for file in Path('data').rglob('*'):
    resources_zip.write(file, file.relative_to('data'))

resources_zip.close()
