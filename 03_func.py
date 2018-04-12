# 12 def. 13 return. 14 default arg.
# 15 Variable Scope. 16 Keyword arg. 17 Flexible number of arg. 18 Unpacking arg.
def add(a,b):
    sum = a+b
    return sum

print(add(1,2))

def beef():
    print("good food")

beef()

def bitcoin_to_usd(btc):
    amount = btc * 527
    print(amount)

bitcoin_to_usd(100)

# 13 return.
def allowed_dating_age(my_age):
    girls_age = my_age/2 + 7
    return  girls_age

print(allowed_dating_age(20))
print(allowed_dating_age(30))

# 14 default arg.
def get_gender(sex = "Unknown"):
    if sex is 'm':
        sex = "Male"
    elif sex is 'f':
        sex = "Female"
    print(sex)

get_gender('m')
get_gender('f')
get_gender('Other')
get_gender()

# 16 Keyword arg.
def dumb_sentence(name = "Bucky", action = "ate", item = "tuna"):
    print(name, action, item)
dumb_sentence()
dumb_sentence("Sally", "farts", "gently")
dumb_sentence(item="awesome")
dumb_sentence(item="awesome", action="si")

# 17 Flexible number of arg.
def add_number(*args):
    total = 0
    for a in args:
        total += a
    print(total)

add_number(3)
add_number(3, 32)
add_number(3, 10, 100)

# 18 Unpacking arg.
def health_calculator(age, apples_ate, cigs_smoked):
    answer = (100-age) + (apples_ate * 3.5 ) - (cigs_smoked * 2)
    print(answer)

health_calculator(10, 1, 1)

data = [27, 20, 1]
health_calculator(data[0], data[1], data[2])
health_calculator(*data) # unpacking data