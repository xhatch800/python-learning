score = 30

if score >= 90:
    grade = "A"
elif score >= 80 and score < 90:
    grade = "B"
elif score >= 70 and score < 80:
    grade = "C"
elif score >= 60 and score < 70:
    grade = "D"
elif score >= 50 and score < 60:
    grade = "E"
else:
    grade = "F"

print(f"Grade is {grade}")

items = ["apple", "banana", "cherry"]

for item in items:
    print(item)

for i, item in enumerate(items):
    print(i, item)

for i in range(5):
    print(i)

for i in range(0, 10, 2):
    print(i)

for i in range(0, 10):
    print(i)

flag = True

while flag:
    flag = False
    print(f"Flag is {flag}")

while not flag:
    flag = True
    print(f"Flag is {flag}")

match score:
    case val if val >= 90:
        grade = "A"
    case val if val >= 80 and val < 90:
        grade = "B"
    case val if val >= 70 and val < 80:
        grade = "C"
    case val if val >= 60 and val < 70:
        grade = "D"
    case val if val >= 50 and val < 60:
        grade = "E"
    case val if val < 50:
        grade = "F"

print(f"Grade is {grade}")

count = 10
while count > 0:
    print(f"Count is {count}")
    count -= 1






