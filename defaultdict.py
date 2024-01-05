from collections import defaultdict

def default_message():
    return " key is not there"

my_default = defaultdict(default_message)
my_default["key 1"] = "value 1"
my_default["key 2"] = "value 2"
print(my_default["key 1"])
print(my_default["key 2"])
print(my_default["key 3"])
