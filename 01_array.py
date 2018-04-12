# 03 String. 04 Array. 05 Array. 19 Sets. 20 Dictionary.
mylist0 = ['AAA', 'BBB', 'CCC','DDD','EEE']
mylist = ['aaa', 'bbb', 'ccc','ddd','eee']
print(mylist[0])
mylist[0] = 'zzz'
print(mylist[0])
print(mylist[1:3])
myMatrix = [mylist0,mylist]
print(myMatrix)
print(myMatrix[1][1])

print(len(mylist))
print(max(mylist))#zzz最大, aaa最小
print(min(mylist))
print(mylist[:3])
print(mylist[-2:])

players = [29, 58, 66, 71, 87]
players[2]
players[2] = 6666
players + [100] #本身不改变
print(players)
players += [100] #等效于 players.append(100)
print(players)

players[:2] = [1,2] #设值
print(players)
players[:] = [] #设值
print(players)

# 19 Sets
groceries = {"cereal", "milk", "starcrunch", "beer", "duct tape", "lotion", "beer"}
print(groceries)

if "milk" in groceries:
    print("yes")
else:
    print("no")

# 20 Dictionary.
classmates = {1: "Jiang", 2:"Wang", 3:"Haha"}
print(classmates)
print(classmates[1])

for k,v in classmates.items():
    print(k, v)
    if k == 1:
        print(classmates[k])