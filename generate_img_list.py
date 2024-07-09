import json
from pathlib import Path

img_path = Path(__file__).parent / "image"

img_list = {chara.name: [img.name for img in chara.iterdir()] for chara in img_path.iterdir()}

with open('abscension_img_list.json', 'w', encoding='utf-8') as f:
    json.dump(img_list, f, ensure_ascii=False, indent=2)


