def hanoi(n, source="1", auxiliary="2", target="3"):
    if n == 1:
        print(f"Перемістити диск 1 з стрижня {source} на стрижень {target}")
        return
    # Перемістити n-1 дисків з source на auxiliary, використовуючи target як допоміжний
    hanoi(n - 1, source, target, auxiliary)
    # Перемістити найбільший диск з source на target
    print(f"Перемістити диск {n} з стрижня {source} на стрижень {target}")
    # Перемістити n-1 дисків з auxiliary на target, використовуючи source як допоміжний
    hanoi(n - 1, auxiliary, source, target)

# Ввід кількості дисків
n = int(input("Введіть кількість дисків (n < 6): "))

if n < 1 or n >= 6:
    print("Будь ласка, введіть число від 1 до 5")
else:
    print(f"Послідовність переміщень для {n} дисків:")
    hanoi(n)
    print(f"Готово! Всі {n} дисків переміщено з стрижня 1 на стрижень 3")