# indexing[start:stop:step]
name="Opiyo Oscar"
first_name=name[0:5]
print(first_name)
last_name=name[6:]
print(last_name)
funcky_name=name[0:7:2]
print(funcky_name)
# Reversing a string 
reversed_name=name[::-1]
print(reversed_name)
# using the slice function
# slice(start,stop,step)
website="http://www.google.com"
slice=slice(11,-4)
print(website[slice])
website2="http://www.facebook.com"
print(website2[slice])
