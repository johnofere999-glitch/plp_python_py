# Grade Reporter

scores = [85, 72, 90, 64, 48]

total = 0

for score in scores:
    total += score

    if score >= 80:
        print(f"{score}: A")
    elif score >= 70:
        print(f"{score}: B")
    elif score >= 50:
        print(f"{score}: C")
    else:
        print(f"{score}: F")

print(f"Total score: {total}")