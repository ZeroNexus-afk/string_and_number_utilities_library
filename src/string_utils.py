import re
import unicodedata


def normalize_text(text: str, mode: str = "default") -> str:
    """
    Chuẩn hóa chuỗi văn bản.
    
    Modes:
      - "default" : Xóa khoảng trắng thừa, trim 2 đầu
      - "lower"   : default + chuyển về chữ thường
      - "upper"   : default + chuyển về chữ hoa
      - "unicode" : default + chuẩn hóa Unicode (NFC)
      - "clean"   : Xóa tất cả ký tự đặc biệt, chỉ giữ chữ cái và số
    """
    if not isinstance(text, str):
        raise TypeError(f"Expected str, got {type(text).__name__}")

    if mode == "unicode":
        text = unicodedata.normalize("NFC", text)

    if mode == "clean":
        text = re.sub(r'[^a-zA-Z0-9À-ỹ\s]', '', text)

    # Xóa khoảng trắng thừa (nhiều space -> 1 space)
    result = re.sub(r'\s+', ' ', text).strip()

    if mode == "lower":
        result = result.lower()
    elif mode == "upper":
        result = result.upper()

    return result


def count_words(text: str) -> dict:
    """
    Đếm số từ trong chuỗi. Trả về dict chi tiết.
    """
    if not isinstance(text, str):
        raise TypeError(f"Expected str, got {type(text).__name__}")

    words = text.split()
    total = len(words)

    frequency = {}
    for word in words:
        frequency[word] = frequency.get(word, 0) + 1

    return {
        "total": total,
        "unique": len(frequency),
        "frequency": frequency,
    }


def reverse_text(text: str, mode: str = "char") -> str:
    """
    Đảo ngược chuỗi.
    
    Modes:
      - "char"  : Đảo theo ký tự
      - "word"  : Đảo theo từ
      - "word_keep_order" : Đảo thứ tự từ nhưng giữ nguyên từ
    """
    if not isinstance(text, str):
        raise TypeError(f"Expected str, got {type(text).__name__}")

    if mode == "char":
        return text[::-1]
    elif mode == "word":
        words = text.split()
        return " ".join(reversed(words))
    else:
        raise ValueError(f"Unknown mode: '{mode}'. Use 'char' or 'word'.")


def is_palindrome(text: str, ignore_case: bool = True, 
                  ignore_spaces: bool = True, 
                  ignore_special: bool = True) -> dict:
    """
    Kiểm tra chuỗi có phải palindrome (xuôi ngược giống nhau) không.
    
    Args:
        text             : Chuỗi cần kiểm tra
        ignore_case      : Bỏ qua phân biệt hoa/thường
        ignore_spaces    : Bỏ qua khoảng trắng
        ignore_special   : Bỏ qua ký tự đặc biệt (chỉ giữ chữ + số)
    """
    if not isinstance(text, str):
        raise TypeError(f"Expected str, got {type(text).__name__}")

    processed = text

    if ignore_special:
        processed = re.sub(r'[^a-zA-Z0-9À-ỹ]', '', processed)

    if ignore_spaces:
        processed = processed.replace(" ", "")

    if ignore_case:
        processed = processed.lower()

    reversed_text = processed[::-1]
    result = (processed == reversed_text)

    return {
        "is_palindrome": result,
        "original": text,
        "processed": processed,
        "reversed": reversed_text,
    }
