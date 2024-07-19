my_dict={
    "name":"Hana",
    "age":16,
    "fav_subjects":["math","science"]
}
print(my_dict)
print(my_dict.get("name"))
my_dict.update({"birthday":"21/1"})
print(my_dict)
del my_dict["fav_subjects"]
print(my_dict)