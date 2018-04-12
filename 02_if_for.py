# 07 if. 08 for. 09 range while. 10 break 11 continue.

# 07 if.
age = 18
if age >= 21:
    print('You are 21')
elif age >= 16:
    print('You are old enough to drive')
else:
    print("you are not old enough")

if ((age>=1)and(age<=18 )):
    print('1...18')
elif (age==21)or(age>=65):
    print('21 and 65')
elif not(age == 30):
    print('not 30')
else:
    print('else eee')

number = 15
name = "Jiang"
if name is "Jiang":
    print("Hello, Jiang")
if number is 15: # 等效于 number == 15®
    print("Hello, 15")

# 08 for.
foods = ['bacon', 'tuna', 'ham', 'snausages', 'beef']
for f in foods:
    f += '00'
    print(f)
print(len(foods))

# 09 range while.
for x in range(10):
    print(x)

for x in range(100,200,10):
    print(x)

for x in range(5,10):
    print(x)

buky = 5
while buky < 10:
    print(buky)
    buky += 1

# 10 break.
magicNumber = 26
for n in range(101):
    if n is magicNumber:
        print(n, "is magic number")
        break # 停止整个for循环
    else:
        print(n)

# 11 continue.
numbersTaken = [2, 5, 12, 13, 17, 19]
for n in range(1, 20):
    if n in numbersTaken:
        continue # 立刻停止当前循环,不执行后面的语句. 并进入下一个循环
    print(n)