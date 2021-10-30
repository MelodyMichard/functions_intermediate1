x = [ [5,2,3], [10,8,9] ] 
students = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'}
]
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]

# update value of 10 to 15
x[1][0] = 15
print(x)

# change jordan to bryant
students[0]['last_name'] = 'Bryant'
print(students[0])

# change messi to andres
sports_directory['soccer'][0] = 'Andres'
print(sports_directory['soccer'])

# change value 20 to 30
z[0]['y'] = 30
print(z[0])

students = [
        {'first_name' : 'Michael', 'last_name' : 'Jordan'},
        {'first_name' : 'John', 'last_name' : 'Rosales'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]

def iterate_dictionary(students):
    for student in students:
        arrTemp = []
        for key in student:
            arrTemp.append(key + " - " + student[key])
        print("{}, {}".format(arrTemp[0], arrTemp[1]))
iterate_dictionary(students)

def iterate_dictionary2(key, list):
    for item in list:
        print(item[key])
iterate_dictionary2('first_name', students)

dojo = {
    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

def print_info(dict_list):
    for key in dict_list:
        print(str(len(dict_list[key])) + " " + key.upper())
        for value in dict_list[key]:
            print(value)
        print()
print_info(dojo)