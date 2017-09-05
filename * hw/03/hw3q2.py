
print("Please enter the prices of two items.")
#asks for item pricing
item1 = float(input("Enter the first price."))
item2 = float(input("Enter the second price.")) 
#asks about card, converts to uppercase letter 
cardYN = input(("Do you have a club card? Y or N.").upper())
#asks for tax rate
tax = float(input("What is the tax rate? E.g.: 5.5 if reat is 5.5%.")) 
#makes new variable for reduced price on items
items = item1 + item2
item1b = item1
item2b = item2
#calculates lower price, takes 50% off
if (item1 <= item2):
    item1b = item1 * .5
elif (item2 < item1):
    item2b = item2 * .5
itemsb = item1b + item2b
#if Y for card, takes 10% off 
if (cardYN == "Y"):
    itemsb = itemsb * .9
itemsc = itemsb
itemsc = itemsc + (itemsb * (tax/100)) 
print("Base price:", str(items),
      "Price after discount(s):", str(itemsb),
      "Total price:", str(itemsc))


