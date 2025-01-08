#Creating empty dictionary
medical_costs = {}

# Adding key, value pair
medical_costs['Marina'] = 6607.0
medical_costs['Vinay'] = 3225.0

# Updating dictionary using update method
medical_costs.update({"Connie":8886.0,"Isaac":16444.0,"Valentina":6420.0})

# Print the dictionary
print(medical_costs)

# Change Vinay's Insurance costs
medical_costs["Vinay"] = 3325.0
print(medical_costs)


# Calculating total costs
total_cost = 0
for values in medical_costs.values():
  total_cost += values

print(total_cost)
average_cost = total_cost / len(medical_costs.keys())
print(average_cost)

# Getting and deleting values from the dictionary
medical_costs.get("Vinay", 0) # if value of Vinay exists, otherwise return 0
medical_costs.pop("Vinay", 0) # delete Vinay if exists, otherwise return 0

# Creating Dictionary from lists
names = ['Marina', 'Vinay','Connie', 'Isaac','Valentina']
ages = [27,24,43,35,52]

# Dictionary Comprehension
zipped_ages = zip(names,ages)
names_to_ages = {key:value for key,value in zipped_ages}
print(names_to_ages)

marina_age = names_to_ages.get("Marina")
print(f"Marina's age is {marina_age}")

# Empty Dictionary
medical_records = {}
medical_records["Marina"] = {"Age": 27, "Sex": "Female", "BMI": 31.1, "Children": 2, "Smoker": "Non-smoker", "Insurance Cost": 6607.0}

print(medical_records)

# Updating Dictionary with different medical records
medical_records.update({
   "Vinay": {
        "Age": 24,
        "Sex": "Male",
        "BMI": 26.9,
        "Children": 0,
        "Smoker": "Non-smoker",
        "Insurance Cost": 3225.0
    },
    "Connie": {
        "Age": 43,
        "Sex": "Female",
        "BMI": 25.3,
        "Children": 3,
        "Smoker": "Non-smoker",
        "Insurance Cost": 8886.0
    },
    "Isaac": {
        "Age": 35,
        "Sex": "Male",
        "BMI": 20.6,
        "Children": 4,
        "Smoker": "Smoker",
        "Insurance Cost": 16444.0
    },
    "Valentina": {
        "Age": 52,
        "Sex": "Female",
        "BMI": 18.7,
        "Children": 1,
        "Smoker": "Non-smoker",
        "Insurance Cost": 6420.0
    }
})

print(medical_records)

# Accessing elements from the data
print(f"Connie's insurance cost is {medical_records['Connie']['Insurance Cost']} dollars.")

medical_records.pop("Vinay")
print(medical_records)

# Showing all the data i the database
for name,value in medical_records.items():
  print(f"{name} is a {value['Age']} year old {value['Sex']} {value['Smoker']} with a BMI of {value['BMI']} and insurance cost of {value['Insurance Cost']}")








