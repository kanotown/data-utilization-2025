import re
from pymdownx import slugs

def keep_dots_slugify(text, separator):
    """pymdownxベースでドットを保持"""
    # 一時的にドットを特殊文字に置換
    text = text.replace('.', '__DOT__')
    
    # 標準のslugifyを適用
    result = slugs.uslugify(text, separator)
    
    # ドットを復元
    result = result.replace('__dot__', '.')
    
    return result