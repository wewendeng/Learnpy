

li = []
li.append(1)
li.append(2)
li.append(3)
li.append(4)

print(li)

li.pop()

print(li)

li.append(4)

print(li)

print(li[0])

li[0] = 42
print(li[0])

li[0] = 1
print(li)
print(li[-1])
print(li[0])
#print(li[4])
print(li[1:3])
print(li[:3])
print(li[2:])
print(li[::2])
print(li[::-1])

del li[2]
print(li)

other_list = [5, 6]
print(li + other_list)
print(li.extend(other_list))

print(li.remove(2))

print(1 in li)
print(len(li))

tuple = (1, 2, 3)
print(tuple)
print(tuple[1])
# tuple[0] = 3

print(len(tuple))
print(tuple + (4, 5, 6))
print(tuple[:2])
print(2 in tuple)

a, b, c = (1, 2, 4)
print(a)
print(b)
print(c)

empty_dict = {}
filter_dict = {"one":"1", "two":"2", "three":"3"}
print(filter_dict["one"])
print(filter_dict.keys())
print(filter_dict.values())
print(filter_dict.items())

print("one" in filter_dict)
print("1" in filter_dict)
print(1 in filter_dict)
#print(filter_dict["four"])

print(filter_dict.get("one"))
print(filter_dict.get("four"))

print(filter_dict.get("one", 4))
print(filter_dict.get("four", 4))
print(filter_dict)

filter_dict["four"] = "4"
print(filter_dict)

filter_dict.setdefault("five", "5")
print(filter_dict)
filter_dict.setdefault("five", "6")
print(filter_dict)