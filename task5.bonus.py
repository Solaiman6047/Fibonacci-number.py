population={
    "Egypt":114558093,
    "US":341889990,
    "China":1425158378,
    "Russia":143936883,
}
population_list=list(population.items())
for i in range(len(population_list)):
    for j in range(0, len(population_list) - i - 1):
        if population_list[j][1]<population_list[j+1][1]:
            temp = population_list[j]
            population_list[j] = population_list[j+1]
            population_list[j+1] = temp
print(population_list)