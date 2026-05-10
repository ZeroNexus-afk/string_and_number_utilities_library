import unittest
import sys
import os

# Thêm đường dẫn thư mục 'src' vào sys.path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from string_utils import normalize_text, count_words, reverse_text, is_palindrome


class TestNormalizeText(unittest.TestCase):
    """Test cases cho hàm normalize_text"""

    def test_default_mode(self):
        """Mode default: xóa khoảng trắng thừa, trim 2 đầu"""
        self.assertEqual(normalize_text("  Xin   chào   thế  giới  "), "Xin chào thế giới")

    def test_lower_mode(self):
        """Mode lower: default + chuyển về chữ thường"""
        self.assertEqual(normalize_text("  HELLO   WORLD  ", mode="lower"), "hello world")

    def test_upper_mode(self):
        """Mode upper: default + chuyển về chữ hoa"""
        self.assertEqual(normalize_text("  hello   world  ", mode="upper"), "HELLO WORLD")

    def test_unicode_mode(self):
        """Mode unicode: default + chuẩn hóa Unicode NFC"""
        composed = "é"          # 1 code point (U+00E9)
        decomposed = "e\u0301"  # 2 code points (U+0065 + U+0301)
        result = normalize_text(decomposed, mode="unicode")
        self.assertEqual(result, composed)
        self.assertEqual(len(result), 1)

    def test_clean_mode(self):
        """Mode clean: xóa ký tự đặc biệt, chỉ giữ chữ cái, số và khoảng trắng"""
        self.assertEqual(normalize_text("H3ll0 W0rld! @#Test", mode="clean"), "H3ll0 W0rld Test")

    def test_clean_mode_with_unicode(self):
        """Mode clean: giữ nguyên ký tự Unicode (tiếng Việt)"""
        self.assertEqual(normalize_text("Xin chào! Bạn khỏe không?", mode="clean"), "Xin chào Bạn khỏe không")

    def test_clean_mode_only_special_chars(self):
        """Mode clean: chuỗi chỉ chứa ký tự đặc biệt → kết quả rỗng"""
        self.assertEqual(normalize_text("!@#$%^&*()", mode="clean"), "")

    def test_clean_mode_extra_spaces_after_removal(self):
        """Mode clean: sau khi xóa ký tự đặc biệt, khoảng trắng thừa cũng bị xóa"""
        self.assertEqual(normalize_text("a!@# b$%^ c", mode="clean"), "a b c")

    def test_empty_string(self):
        """Chuỗi rỗng trả về chuỗi rỗng"""
        self.assertEqual(normalize_text(""), "")

    def test_only_whitespace(self):
        """Chuỗi chỉ có khoảng trắng trả về chuỗi rỗng"""
        self.assertEqual(normalize_text("     "), "")

    def test_type_error(self):
        """Truyền kiểu không phải str → TypeError"""
        with self.assertRaises(TypeError):
            normalize_text(123)
        with self.assertRaises(TypeError):
            normalize_text(None)
        with self.assertRaises(TypeError):
            normalize_text(["list"])


class TestCountWords(unittest.TestCase):
    """Test cases cho hàm count_words"""

    def test_normal_sentence(self):
        """Đếm từ bình thường, có từ trùng lặp (cùng chữ thường)"""
        result = count_words("hello world hello")
        self.assertEqual(result['total'], 3)
        self.assertEqual(result['unique'], 2)
        self.assertEqual(result['frequency'], {'hello': 2, 'world': 1})

    def test_extra_spaces(self):
        """Chuỗi có khoảng trắng thừa"""
        result = count_words("  Một   hai   ba  ")
        self.assertEqual(result['total'], 3)
        self.assertEqual(result['unique'], 3)
        self.assertEqual(result['frequency'], {'Một': 1, 'hai': 1, 'ba': 1})

    def test_single_word(self):
        """Chuỗi chỉ có 1 từ"""
        result = count_words("Hello")
        self.assertEqual(result['total'], 1)
        self.assertEqual(result['unique'], 1)
        self.assertEqual(result['frequency'], {'Hello': 1})

    def test_all_same_words(self):
        """Tất cả từ đều giống nhau"""
        result = count_words("test test test")
        self.assertEqual(result['total'], 3)
        self.assertEqual(result['unique'], 1)
        self.assertEqual(result['frequency'], {'test': 3})

    def test_empty_string(self):
        """Chuỗi rỗng"""
        result = count_words("")
        self.assertEqual(result['total'], 0)
        self.assertEqual(result['unique'], 0)
        self.assertEqual(result['frequency'], {})

    def test_only_spaces(self):
        """Chuỗi chỉ có khoảng trắng"""
        result = count_words("   ")
        self.assertEqual(result['total'], 0)
        self.assertEqual(result['unique'], 0)
        self.assertEqual(result['frequency'], {})

    def test_case_sensitive_frequency(self):
        """Frequency phân biệt hoa/thường: 'Hello' và 'hello' là 2 từ khác nhau"""
        result = count_words("Hello hello HELLO")
        self.assertEqual(result['total'], 3)
        self.assertEqual(result['unique'], 3)
        self.assertEqual(result['frequency'], {'Hello': 1, 'hello': 1, 'HELLO': 1})

    def test_type_error(self):
        """Truyền kiểu không phải str → TypeError"""
        with self.assertRaises(TypeError):
            count_words(["list", "of", "words"])
        with self.assertRaises(TypeError):
            count_words(123)


class TestReverseText(unittest.TestCase):
    """Test cases cho hàm reverse_text"""

    def test_char_mode(self):
        """Đảo ngược theo ký tự"""
        self.assertEqual(reverse_text("Hello World", mode="char"), "dlroW olleH")

    def test_word_mode(self):
        """Đảo ngược theo từ"""
        self.assertEqual(reverse_text("Hello World", mode="word"), "World Hello")

    def test_char_mode_default(self):
        """Mode mặc định là 'char'"""
        self.assertEqual(reverse_text("Hello"), "olleH")
        self.assertEqual(reverse_text("Hello"), reverse_text("Hello", mode="char"))

    def test_unicode_char_mode(self):
        """Đảo ngược ký tự Unicode (tiếng Việt) - 'ộ' là 1 ký tự kết hợp"""
        self.assertEqual(reverse_text("Một hai ba", mode="char"), "ab iah tộM")

    def test_word_mode_multiple_spaces(self):
        """Mode word: khoảng trắng thừa bị normalize (do split/join)"""
        result = reverse_text("Hello   World", mode="word")
        self.assertEqual(result, "World Hello")

    def test_word_mode_single_word(self):
        """Mode word: chỉ có 1 từ → kết quả giống nguyên bản"""
        self.assertEqual(reverse_text("Hello", mode="word"), "Hello")

    def test_empty_string(self):
        """Chuỗi rỗng"""
        self.assertEqual(reverse_text("", mode="char"), "")
        self.assertEqual(reverse_text("", mode="word"), "")

    def test_word_keep_order_not_implemented(self):
        """Mode 'word_keep_order' được đề cập trong docstring nhưng chưa implement → ValueError"""
        with self.assertRaises(ValueError):
            reverse_text("Hello World", mode="word_keep_order")

    def test_invalid_mode(self):
        """Mode không hợp lệ → ValueError"""
        with self.assertRaises(ValueError):
            reverse_text("Hello", mode="invalid_mode")
        with self.assertRaises(ValueError):
            reverse_text("Hello", mode="CHAR")

    def test_type_error(self):
        """Truyền kiểu không phải str → TypeError"""
        with self.assertRaises(TypeError):
            reverse_text(12345)
        with self.assertRaises(TypeError):
            reverse_text(None)


class TestIsPalindrome(unittest.TestCase):
    """Test cases cho hàm is_palindrome"""

    def test_true_palindrome(self):
        """Palindrome đơn giản với khoảng trắng"""
        result = is_palindrome("Race car")
        self.assertTrue(result['is_palindrome'])

    def test_false_palindrome(self):
        """Không phải palindrome"""
        result = is_palindrome("Hello")
        self.assertFalse(result['is_palindrome'])

    def test_complex_palindrome(self):
        """Palindrome phức tạp: có dấu câu, khoảng trắng"""
        result = is_palindrome("A man, a plan, a canal: Panama")
        self.assertTrue(result['is_palindrome'])

    def test_number_palindrome(self):
        """Palindrome là chuỗi số"""
        result = is_palindrome("12321")
        self.assertTrue(result['is_palindrome'])

    def test_single_character(self):
        """1 ký tự luôn là palindrome"""
        result = is_palindrome("a")
        self.assertTrue(result['is_palindrome'])

    def test_empty_string(self):
        """Chuỗi rỗng là palindrome"""
        result = is_palindrome("")
        self.assertTrue(result['is_palindrome'])

    def test_case_sensitive(self):
        """ignore_case=False: phân biệt hoa/thường"""
        result = is_palindrome("Racecar", ignore_case=False)
        self.assertFalse(result['is_palindrome'])

    def test_case_sensitive_true_palindrome(self):
        """ignore_case=False nhưng chuỗi đồng nhất case → vẫn True"""
        result = is_palindrome("racecar", ignore_case=False)
        self.assertTrue(result['is_palindrome'])

    def test_space_sensitive(self):
        """ignore_spaces=False: khoảng trắng được tính"""
        result = is_palindrome("race car", ignore_spaces=False)
        self.assertFalse(result['is_palindrome'])

    def test_space_sensitive_no_spaces(self):
        """ignore_spaces=False nhưng không có khoảng trắng → vẫn True"""
        result = is_palindrome("racecar", ignore_spaces=False)
        self.assertTrue(result['is_palindrome'])

    def test_special_chars_not_ignored(self):
        """ignore_special=False: ký tự đặc biệt được tính"""
        result = is_palindrome("A man, a plan, a canal: Panama", ignore_special=False)
        self.assertFalse(result['is_palindrome'])

    def test_ignore_special_false_simple(self):
        """ignore_special=False với chuỗi không có ký tự đặc biệt → True"""
        result = is_palindrome("racecar", ignore_special=False)
        self.assertTrue(result['is_palindrome'])

    def test_return_structure(self):
        """Kiểm tra cấu trúc dict trả về đầy đủ các key"""
        result = is_palindrome("Race car")
        self.assertIn('is_palindrome', result)
        self.assertIn('original', result)
        self.assertIn('processed', result)
        self.assertIn('reversed', result)
        self.assertEqual(result['original'], "Race car")
        self.assertEqual(result['processed'], "racecar")
        self.assertEqual(result['reversed'], "racecar")

    def test_unicode_palindrome(self):
        """Palindrome với ký tự Unicode"""
        result = is_palindrome("Ábá")
        self.assertTrue(result['is_palindrome'])

    def test_type_error(self):
        """Truyền kiểu không phải str → TypeError"""
        with self.assertRaises(TypeError):
            is_palindrome(12321)
        with self.assertRaises(TypeError):
            is_palindrome(None)


if __name__ == '__main__':
    unittest.main()