# in line 2-8 I'm setting/naming the variables to have a good overview later
cars = 100 # there are 100 cars
space_in_a_car = 4.0 # each car has four spaces for a person
drivers = 30 # there are 30 available drivers
passengers = 90 # there are 90 available passengers
cars_not_driven = cars - drivers #the amount of cars that aren't driven isequal to the amountof cars that are available minus the amount of drivers
cars_driven = drivers # the amount of cars driven is equal to the amount of drivers
carpool_capacity = cars_driven * space_in_a_car # the amount of people that can be driven in total is equal to the amount of driven cars times the amount of spaces in one car
average_passengers_per_car = passengers / cars_driven # the average amount of passengers that has to share a car is equally to the amount of passengers divided by the amount of driven cars

# in line 12-17 the text inside thequotes will be printed as it is written there, the variables will changeaccrding to the settings from line 2-9
print "There are", cars, "cars available."
print "There are only", drivers, "drivers available."
print "There will be", cars_not_driven, "empty cars today."
print "We can transport", carpool_capacity, "people today."
print "We have", passengers, "to carpool today."
print "We need to put about", average_passengers_per_car, "in each car."


# Study Drill
# Python shows precisely where an error occured, by stating the file name, the line
# and telling what the exact problem is. Here,"NameError".
# You cannot use a variable, that wasn't set in the first place.
# You either forgot to define the name at all or had a writing error using an underscore in the word carpool itself.

# 1. I don't think that it was especially necessary in this task to use a floating point.
# Nothing changes in this calculation apart from the fact, that 4 is not a floating point anymore.
