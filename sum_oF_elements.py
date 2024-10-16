
def sum_of_elements(numbers, exclude_negative=False):
 if exclude_negative:
  total=sum(num for num in numbers if num>=0)  
  return total
 else:
  total=sum(numbers)
  return total

numbers_input=input("Enter a list of numbers: ")
#string->integer
numbers = [int(n) for n in numbers_input.split()]

exclude_negative_input = input("Do you want to exclude negative numbers? (yes or no): ")

exclude_negative = exclude_negative_input == "yes"

result = sum_of_elements(numbers, exclude_negative)

print(f"The sum of the elements: {result}")