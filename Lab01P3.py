# Nakarin Philangam
# 01/06/2022

copiesNum = int(input("How many copies are you buying? "))
if copiesNum >= 1 and copiesNum <= 10:
    unit_price = 99
    print("Unit price: $99")
    total = copiesNum * unit_price
    print("Total price: $%-6s" % total)
elif copiesNum >= 11 and copiesNum <= 50:
    unit_price = 89
    print("Unit price: $89")
    total = copiesNum * unit_price
    print("Total price: $%-6s" % total)
elif copiesNum >= 51 and copiesNum <= 100:
    unit_price = 79
    print("Unit price: $79")
    total = copiesNum * unit_price
    print("Total price: $%-6s" % total)
elif copiesNum >= 101:
    unit_price = 69
    print("Unit price: $69")
    total = copiesNum * unit_price
    print("Total price: $%-6s" % total)


