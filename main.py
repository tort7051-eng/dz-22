a = float(input("Введи число "))
b = float(input("Введи число "))

print("1 — (+)")
print("2 —  (-)")
print("3 — (*)")
print("4 — (/)")

choice = input("Обери дію")

if choice == "1":
    print("Результат:", a + b)

elif choice == "2":
    print("Результат:", a - b)

elif choice == "3":
    print("Результат:", a * b)

elif choice == "4":
    if b != 0:
        print("Результат:", a / b)
