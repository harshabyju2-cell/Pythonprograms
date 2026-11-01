try:
    units = float(input("Enter electricity units: "))
    if units < 0:
        raise ValueError("Units cannot be negative")
except ValueError as e:
    print("Invalid input:", e)
else:
    if units <= 100:
        bill = units * 3
    elif units <= 200:
        bill = 100 * 3 + (units - 100) * 5
    else:
        bill = 100 * 3 + 100 * 5 + (units - 200) * 8
    print("Electricity Bill: Rs.", bill)
finally:
    print("Bill calculation completed")