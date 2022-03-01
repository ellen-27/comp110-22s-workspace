"""demonstrations of dictionary capabilities."""

# declaring the type of a dictionary
schools: dict[str,int]

# initialize to an empty dictionary
schools = dict()

# set a key-value pairing in the dictionary
schools["UNC"] = 19400
schools["Duke"] = 6717
schools["NCSO"] = 26150

# print a dictionary literal representation
print(schools)

# access a value by its key -- "lookup"
print(f"UNC has {schools['UNC']} students")

# remove a key-value pair from a dictionary
# by its key. 
schools.pop("Duke")

# test for the existence of a key
is_duke_present: bool = "Duke" in schools
print(f"Duke is present: {is_duke_present}")


print(schools)

# demonstration of dictionary literals

# empty dictionary literal
schools = {} # same as dict()
print(schools)

# alternatively, initialize key-value pairs
schools = {"UNC": 19400, 
    "Dukie": 6717, 
    "NCSU": 26150}
print(schools) 

# example looping over the keys of a dict
for school in schools:
    print(f"Key: {school} -> Value: {schools[school]}")