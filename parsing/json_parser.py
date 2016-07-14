__author__ = 'Perevalov'


import json
from pprint import pprint


def converting(fl):
    # converting weird ASTRA output format to float
    if fl is None or fl == "":
        return

    elif fl.isalnum() and not fl.isdigit():
        return

    elif len(fl) >= 2 and (fl[-2] == "-" or fl[-2] == "+") and len(fl) != 2:
        fl = fl[0:-2]+"E"+fl[-2:]
        return float(fl)

    else:
        return float(fl)

# Opening JSON file
with open('all_results.json') as json_data:
    data = json.load(json_data)


def char_to_float_in_data():
    # Fixing format in all database

    for exp_time in data:
        # print(exp_time)
        # print()
        # print()

        for data_set in data[exp_time]:

            if data_set.lower() == "scalar_data":
                for scalar_data in data[exp_time][data_set]:
                    data[exp_time][data_set][scalar_data] = converting(data[exp_time][data_set][scalar_data][0])
                    # print(scalar_data, ' = ', data[exp_time][data_set][scalar_data])
                # print()

            # elif data_set.lower() == "type":
                # print("Type = ", data[exp_time][data_set])
                # print()

            # elif data_set.lower() == "equation":
                # print("Equ = ", data[exp_time][data_set])
                # print()

            # elif data_set.lower() == "experiment":
                # print("Exp = ", data[exp_time][data_set])
                # print()

            elif data_set.lower() == "standard_data":
                for stand_data in data[exp_time][data_set]:
                    data[exp_time][data_set][stand_data] = converting(data[exp_time][data_set][stand_data])
                    # print(stand_data, " = ", data[exp_time][data_set][stand_data])
                # print()

            elif data_set.lower() == "vector_data":
                for vector in data[exp_time][data_set]:
                    try:
                        for i in range(len(data[exp_time][data_set][vector])):
                            data[exp_time][data_set][vector][i] = converting(data[exp_time][data_set][vector][i])
                            # print(vector, ' = ', data[exp_time][data_set][vector])
                    except ValueError:
                            data[exp_time][data_set][vector][i] = 0


def printing_all_data():

    for exp_time in data:
        print(exp_time)
        # print()
        # print()

        for data_set in data[exp_time]:

            if data_set.lower() == "scalar_data":
                for scalar_data in data[exp_time][data_set]:
                    # data[exp_time][data_set][scalar_data] = converting(data[exp_time][data_set][scalar_data][0])
                    print(scalar_data, ' = ', data[exp_time][data_set][scalar_data])
                print()

            elif data_set.lower() == "type":
                print("Type = ", data[exp_time][data_set])
                print()

            elif data_set.lower() == "equation":
                print("Equ = ", data[exp_time][data_set])
                print()

            elif data_set.lower() == "experiment":
                print("Exp = ", data[exp_time][data_set])
                print()

            elif data_set.lower() == "standard_data":
                for stand_data in data[exp_time][data_set]:
                    # data[exp_time][data_set][stand_data] = converting(data[exp_time][data_set][stand_data])
                    print(stand_data, " = ", data[exp_time][data_set][stand_data])
                print()

            elif data_set.lower() == "vector_data":
                for vector in data[exp_time][data_set]:
                    # for i in range(len(data[exp_time][data_set][vector])):
                    #     data[exp_time][data_set][vector][i] = converting(data[exp_time][data_set][vector][i])
                    print(vector, ' = ', data[exp_time][data_set][vector])
                print()


# ############################# IMPORTANT ################################
# Necessary to start this at the very beginning to switch weird strings in database to the float format
char_to_float_in_data()
#########################################################################

# EXAMPLES
# Printing q and zeff in Ohmic experiments where q(0) < 1 and ne(0) > 4
'''for experiment_time in data:
=======
for experiment_time in data:
>>>>>>> 7168faa824ec1a9b78b0f779f6e81be2f80d7000
    if data[experiment_time]["type"] == "OH":
        if data[experiment_time]["vector_data"]["q"][0] <= 1 and data[experiment_time]["vector_data"]["ne"][0] >= 4:

            print(experiment_time, "q  =", data[experiment_time]["vector_data"]["q"][0], sep="  ")
            try:
                print("Zeff  =", data[experiment_time]["vector_data"]["zef"][0], sep="  ")
            except KeyError:
                print(experiment_time, ' does not have zeff vector')

<<<<<<< HEAD
'''


# printing all vector data names in first dataset
'''for experiment_time in data:
    for vector in data[experiment_time]["vector_data"]:
        print(vector)
    break'''


'''for experiment_time in data:

    if data[experiment_time]["type"] == "OH":
        # print(data[experiment_time]["vector_data"])
        if data[experiment_time]["standard_data"]["i"] >= 0.020:
            print("Day =", data[experiment_time]["experiment"],
                  " Time =", 1000*data[experiment_time]["standard_data"]["time"],
                  " Current = ", data[experiment_time]["standard_data"]["i"]*1000
                  )
            # print(data[experiment_time]["vector_data"]["te"])
'''

# Printing electron energy confinement time, scaling times and mass of main ions
'''
print('Exp            Time     Taue      TNA      TGO       a')
for experiment_time in data:
    if data[experiment_time]["type"] == "OH":
        print(experiment_time[0:-6], ' ', experiment_time[-5:],
              data[experiment_time]["scalar_data"]["taue"],
              data[experiment_time]["scalar_data"]["tna"],
              data[experiment_time]["scalar_data"]["tgo"],
              data[experiment_time]["scalar_data"]["amj"],
              sep='    ')
'''


# Ways to print all data that is in the database

# Written above
'''
printing_all_data()
'''

# Standard Python JSON printing
'''
pprint(data)
'''
# or specific exp
'''
pprint(data["101209_0.027"])
'''

# Exporting database back to json
'''
with open('data.json', 'w') as outfile:
    json.dump(data, outfile)
    '''



