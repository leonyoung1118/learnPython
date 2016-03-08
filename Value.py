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
total = 0
for key in prices:
    
    print key
    print "price: %s" % prices[key]
    print "stock: %s" % stock[key]
    number = prices[key] * stock[key]
    total = total + number

print total

"""This is a simple programe for getting familiar with the dict and for loop of Python"""