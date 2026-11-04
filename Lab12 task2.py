import random
letters = ["A", "E", "U", "F", "Q", "R", "Z", "W"]
voltages = [3, 6, 12]
N = int(input("Введіть кількість компонентів для генерації: "))
def generate_random_component():
    digits = ""
    for i in range(8):
        digits += str(random.randint(0, 9))
    letter = random.choice(letters)
    voltage = random.choice(voltages)
    return f"{letter}{digits}-{voltage}"
component = []
for _ in range(N):
    component.append(generate_random_component())
component.sort()
with open(r"C:\Users\Nazar\OneDrive\Desktop\Lab.txt", "w", encoding="utf-8") as file:
    for comp in component:
        file.write(comp + "\n")

