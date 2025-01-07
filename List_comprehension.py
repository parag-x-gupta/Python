# Learning List comprehension
# Using direct for loop to create a new list
x = [1,2,3,4,5,6,7,8,9,10]
y = [i ** 2 for i in x]
print("Squaring everything : ", list(zip(x,y)))


# Using only one if condition 
heights = [161, 164, 156, 144, 158, 170, 163, 163, 157]

can_ride_coaster = [h for h in heights if h > 161]
print(can_ride_coaster)

# Using logical statement
y_ls = [ number ** 2 if number % 2 == 0 else number ** 3 for number in x]
print("Squaring even numbers, Cubing odd Numbers : ", list(zip(x,y_ls)))


# List Comprehension Exercise
names = ["Judith", "Abel", "Tyson", "Martha", "Beverley", "David", "Anabel"]
estimated_insurance_costs = [1000.0, 2000.0, 3000.0, 4000.0, 5000.0, 6000.0, 7000.0]
actual_insurance_costs = [1100.0, 2200.0, 3300.0, 4400.0, 5500.0, 6600.0, 7700.0]

# Calculating Average Costs and comparing them with the average
total_cost = 0

for ic in actual_insurance_costs:
  total_cost += ic

average_cost = total_cost/len(actual_insurance_costs)
print(f"Average Insurance Cost: {average_cost} dollars.")

for i in range(len(names)):
  name = names[i]
  insurance_cost = actual_insurance_costs[i]
  print(f'The insurance cost for {name} is {insurance_cost} dollars.')
  if insurance_cost > average_cost:
    print(f'The insurance cost for {name} is above average.')
  elif insurance_cost < average_cost:
    print(f'The insurance cost for {name} is below average.')
  else:
    print(f"The insurance cost for {name} is equal to the average.")

  
updated_estimated_costs = [element * 11/ 10 for element in estimated_insurance_costs]
print(updated_estimated_costs)
