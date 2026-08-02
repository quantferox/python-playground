# users = ["Murad", "Emma", "John", "Drake", "Anderson"]
# users.append("Dave")
# users.clear()

# news_users = users.copy()
# news_users = users[:-1]
# print(id(users), id(news_users))
# users.count("Murad") -> 1
# len(users)

# id_users = ["1","2","3","4","5"]
# users.extend(id_users)

# users.index("Murad") - 0

# users.insert(1, "Danilla")
# users.pop(0)
# users.remove("John")
# users.reverse()
# users.sort(key=lambda k:(k[0] != "E",k),reverse=False)

# print(users)


# ==============================================================================
# name = "Murad"
# surname = "Gazymagomedov"
# year = "1997"

# print(name.expandtabs(1))
# print(name.ljust(9, "#"))
# print(name.rjust(9, "#"))
# print(name.center(9, "#"))
# print(name.splitlines())
# print(name.swapcase())
# print(name.zfill(10))
# print(name.partition(" "))
# print(name.rpartition(" "))


# x = {"a": "0", "u": "z"}

# table = name.maketrans(x)

# print(name.translate(table))
# ==============================================================================
# my_set = {"apple", "banana", "cherry"}
# my_set.add("kiwi")
# my_set.clear()
# my_set.pop()
# my_set.remove("apple")
# print(my_set)


# Пример 1:
# set1 = {"a", "b", "c", "d", "e"}
# set2 = {"d", "e", "f", "g", "h"}
# set3 = {"e", "f", "g", "h", "i"}

# # Пример 2:
# set4 = {"a", "b", "c"}
# set5 = {"c", "d", "e"}

# # Пример 3:
# set6 = {"j", "k", "l"}
# set7 = {"l", "m", "n"}

# # Пример 4:
# set8 = {"a", "b"}
# set9 = {"b", "c"}
# set10 = {"a", "b", "c"}
# isdisjoint()	 	Returns whether two sets have a intersection or not
# print(set1.isdisjoint(set3))


# issubset()	<=	Returns whether another set contains this set or not
#  	<	Returns whether all items in this set is present in other, specified set(s)
# issuperset()	>=	Returns whether this set contains another set or not
#  	>	Returns whether all items in other, specified set(s) is present in this set
# print(set8 >= set9)
# print(set8 <= set10)
# print(set8.issubset(set9))
# print(set10.issuperset(set8))


# symmetric_difference()	^	Returns a set with the symmetric differences of two sets
# symmetric_difference_update()	^=	Inserts the symmetric differences from this set and another
# print(set8 ^ set9)
# print(set8.symmetric_difference(set9))

# union()	|	Return a set containing the union of sets
# update()	|=	Update the set with the union of this set and others
# print(set8 | set9)
# print(set8.union(set9))

# intersection()	&	Returns a set, that is the intersection of two other sets
# intersection_update()	&=	Removes the items in this set that are not present in other, specified set(s)
# print(set8 & set9)
# print(set8.intersection(set9))

# discard()	 	Remove the specified item
# set8.discard("a")
# print(set8)

# difference_update()	-=	Removes the items in this set that are also included in another, specified set
# set1.difference_update(set4)
# set1 -= set4
# print(set1)

# difference()	-	Returns a set containing the difference between two or more sets
# print(set1.difference(set4))
# print(set1 - set4)
# ==============================================================================
# dict1 = {"a": 1, "b": 2, "c": 3}
# dict2 = {"d": 4, "e": 5}
# dict3 = {"a": 10, "f": 6}

# dict1.clear()
# dict1.pop("a")
# dict1.popitem()
# val = dict1.setdefault("a", 10)
# val = dict1.setdefault("e", 10)
# dict1.update(dict2)
# print(dict1.fromkeys(['x', 'y', 'z'], 0))
