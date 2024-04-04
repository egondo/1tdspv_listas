import time

fahr = 50

while fahr <= 150:
    celsius = 5 / 9 * (fahr - 32)
    print(f"{fahr} \t {celsius:.1f}")
    fahr = fahr + 1
    time.sleep(0.5)


