# Display a welcome message
print("Hello, Welcome to the Fiber Optic Installation Cost Calculator")

# Get the company name from the user
company_name = input("Please enter the name of your company: ")

# Get the number of feet of fiber optic to be installed from the user
feet_of_fiber = float(input("Please enter the number of feet of fiber optic cable to be stalled: "))

# Multiply the total cost as the number of feet times $0.87
Total_cost = feet_of_fiber * 0.87

# Display the calculated information and company name
print("The total cost of installing", feet_of_fiber, "feet of the fiber optic cable of", company_name, "is $", format(Total_cost, ".2f"), ".", sep="")
