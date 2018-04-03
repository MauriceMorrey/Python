students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
]
def print_stu(list_a):
    #for i, student in enumerate(students):#why does this print everything?
        #print (i,student)
    for i in students:
        print i["first_name"], i["last_name"]

print_stu(students)
print "...end of students..."

users = {
 'Students': [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
  ],
 'Instructors': [
     {'first_name' : 'Michael', 'last_name' : 'Choi'},
     {'first_name' : 'Martin', 'last_name' : 'Puryear'}
  ]
 }
def users_instructors(list_a):
    for keys in list_a:
        print keys
        number = 0
        for i in list_a[keys]:
            number += 1
            first_name_len = len(i["first_name"])
            last_name_len = len(i["last_name"])
            print number, "-", i["first_name"], i["last_name"], "-", first_name_len + last_name_len

users_instructors( users )
