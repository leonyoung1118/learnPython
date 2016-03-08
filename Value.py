prices = {
    "banana" : 4,
    "apple"  : 2,
    "orange" : 1.5,
    "pear"   : 3,
}
stock = {
    "banana" : 6,
    "apple"  : 0,
    "orange" : 32,
    "pear"   : 15,
}

# Write your code below!
for key in prices:
    total = 0
    print key
    print "price: %s" % prices[key]
    print "stock: %s" % stock[key]
    number = prices[key] * stock[key]
    total = total + number

print total

"""This is a simple programe for getting familiar with the dict and for loop of Python"""
shopping_list = ["banana", "orange", "apple"]

stock = {
    "banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15
}

prices = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}

# Write your code below!

def compute_bill(food):
    total =0
    for item in food:
        if stock[item] > 0:
            total=total+prices[item]
            stock[item] -= 1
    return total

