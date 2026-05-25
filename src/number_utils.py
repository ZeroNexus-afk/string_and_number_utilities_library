def is_prime(n):
    """Kiểm tra xem một số có phải là số nguyên tố hay không."""
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def factorial(n):
    """Tính giai thừa của một số nguyên không âm."""
    if n < 0:
        raise ValueError("Giai thừa không xác định cho số âm")
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

def is_even(n):
    """Kiểm tra số chẵn."""
    return n % 2 == 0

def is_odd(n):
    """Kiểm tra số lẻ."""
    return n % 2 != 0

def gcd(a, b):
    """Tính Ước chung lớn nhất (UCLN) của hai số."""
    while b:
        a, b = b, a % b
    return abs(a)

def lcm(a, b):
    """Tính Bội chung nhỏ nhất (BCNN) của hai số."""
    if a == 0 or b == 0:
        return 0
    return abs(a * b) // gcd(a, b)

def fibonacci(n):
    """Tính số Fibonacci thứ n (bắt đầu từ 0)."""
    if n < 0:
        raise ValueError("N không được là số âm")
    if n == 0:
        return 0
    elif n == 1:
        return 1
    
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b

def sum_of_digits(n):
    """Tính tổng các chữ số của một số nguyên (ví dụ 123 -> 6)."""
    return sum(int(digit) for digit in str(abs(n)))
