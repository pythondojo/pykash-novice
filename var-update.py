#! usr/local/env python

# This is an example and tips here if for some reason, you want to update the variables but don't want to disturb the existing one, then use this example:

# IMP FYI here:  a+=10 is equal to a=a+10

# Ok, if we are keeping on adding the variables it will be a big mess. so, what we can do right here is:
# 
total_fishes = 50
fishes_removed = 20

total_fishes_after_removed = 30

# Now, if we want to remove 5 more fishes, but don't want to disturb above 3 lines.

remove_5more = 5
total_fishes_after_removed -=  remove_5more

print total_fishes_after_removed
