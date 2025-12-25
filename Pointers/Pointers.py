num1 = 11

num2 = num1
## Displaying the values and memory addresses before and after updating num2
print("Before num2 value is updated:")
print("num1 =", num1)
print("num2 =", num2)

## Displaying memory addresses
print("\nnum1 points to:", id(num1))
print("num2 points to:", id(num2)) 

## Updating num2 to a new value
num2 = 22 
 ## Displaying the values and memory addresses after updating num2. Now num1 remains unchanged while num2 points to a new memory address.
print("\nAfter num2 value is updated:")
print("num1 =", num1)
print("num2 =", num2) 

print("\nnum1 points to:", id(num1))
print("num2 points to:", id(num2))


#####################################

## Demonstrating pointer behavior with dictionaries
dict1 = {
         'value': 11
        }

## Assigning dict1 to dict2
dict2 = dict1 

print("\n\nBefore value is updated:")
print("dict1 =", dict1)
print("dict2 =", dict2)

print("\ndict1 points to:", id(dict1))
print("dict2 points to:", id(dict2)) 

## Updating the 'value' key in dict2
dict2['value'] = 22

## Displaying the values and memory addresses after updating dict2. Both dict1 and dict2 reflect the change since they point to the same dictionary.
print("\nAfter value is updated:")
print("dict1 =", dict1)
print("dict2 =", dict2) 
## Since dictionary are mutable and is a key value pair, updating the key in dict2 also updates dict1.
## Displaying memory addresses, now both point to the same dictionary
print("\ndict1 points to:", id(dict1))
print("dict2 points to:", id(dict2))


