s = input().strip()

filtered = [ch for ch in s if ch.isalpha()]

if len(set(filtered)) % 2 == 0:
    print("CHAT WITH HER!")
else:
    print("IGNORE HIM!")