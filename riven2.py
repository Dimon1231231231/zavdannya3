def swap_case(s):
    result = ''
    for i in range(len(s)):
        char = s[i]
        # Перевіряємо, чи символ — латинська літера
        if 'a' <= char <= 'z':
            # Мала → велика: віднімання 32 в ASCII
            result += chr(ord(char) - 32)
        elif 'A' <= char <= 'Z':
            # Велика → мала: додавання 32 в ASCII
            result += chr(ord(char) + 32)
        else:
            # Не літера — залишаємо без змін
            result += char
    return result

# Тест
text = input("Введіть рядок: ")
print("Результат:", swap_case(text))