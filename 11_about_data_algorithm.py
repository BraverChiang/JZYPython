# 38 unpack. 39 zip.
#  40 lambda. 41 Min Max Sort Dictionary.

# 38 unpack. 类似数据的拆分
date, name, price = ["December 23, 2015", "Brave", "23.12"]
print(name)

def drop_first_last(grades):
    first, *middle, last = grades # *middle 是指 除去头尾所有中间的数字
    avg = sum(middle) / len(middle)
    print(avg)

drop_first_last([65, 76, 60, 21, 99])

# 39 zip. 类似数据的组合
first = ["a", "b", "c"]
middle = [1, 2, 3]
last = ["xx", "yy", "zz"]

names = zip(first, middle, last)
# [("a", "xx"), ("b","yy")]
for a, b, c in names:
    print(a, b, c)

# 40 lambda.
answer = lambda x: x*7
print(answer(5))

# Button(text="Click Me", command=lambda:custom)

# 41 Min Max Sort Dictionary.
stocks = {
    "GOOG": 520.54,
    "FB": 76.45,
    "YHOO": 39.28,
    "AMZN": 306.21,
    "AAPL": 99.76
}

print(zip(stocks.values(), stocks.keys()))
print(min(zip(stocks.values(), stocks.keys())))
print(max(zip(stocks.values(), stocks.keys())))
print(sorted(zip(stocks.values(), stocks.keys())))
print(sorted(zip(stocks.keys(), stocks.values())))


