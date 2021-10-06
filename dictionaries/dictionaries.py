def run():
    # my_dictionary = {
    #         "key1": 1, 
    #         "key2": 2,
    #         "key3": 3
    # }
    # print(my_dictionary["key1"])
    # print(my_dictionary["key2"])
    # print(my_dictionary["key3"])
    
    country_population = {
        "Argentina": 44938712,
        "Brazil": 210147125,
        "Colombia": 50372424
    }

    # print(country_population["Argentina"])

#With dictionaries you can also go through.

    # for country in country_population.keys():
    #     print(country)
    # for country in country_population.values():
    #     print(country)
 
#Now I want to make a print that shows the keys and their values.
#For example, Argentina has a population of 44938712

    for country, population in country_population.items():
        print("The population in " + country + " is " + str(population))


if __name__ == "__main__":
    run()
