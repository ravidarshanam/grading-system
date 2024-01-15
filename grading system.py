from statistics import mean as m

admins = {'Ravi':'pass123@'}
studentDict = {'Jeff':[78,88,93],
               'Alex':[92,76,88],
               'Sam':[89,92,93]}

def enterGrades():
    nameToEnter = input('Student Name:')
    gradeToEnter = input('Grade: ')
    if nameToEnter in studentDict:
        print('Adding Grade...')
        studentDict[nameToEnter].append(float(gradeToEnter))
    else:
        print('student does not exits.')
    print(studentDict)
def removeStudent():
    nameToRemove = input('What student to remove?:')
    if nameToRemove in studentDict:
        print('removing student...')
        del studentDict[nameToRemove]
    print(studentDict)
def studentAVGs():
    for eachStudent in studentDict:
        gradeList = studentDict[eachStudent]
        avgGrade = m(gradeList)
        print(eachStudent,'has an average grade of:',avgGrade)
    
    
def main():
    print("""
    Welcome to Grade Central
    
    [1] - Enter Grades
    [2] - Remove Student
    [3] - Student Average Grades
    [4] - Exit
    """)
    action = input("What would you like to do today? (Enter a number)")
    if action == '1':
        enterGrades()
    elif action == '2':
        removeStudent()
    elif action == '3':
        studentAVGs()
    elif action == '4':
        exit()
    else:
        print('No valid choice was given, try again')
login = input('Username:')
passw = input('Password:')
if login in admins:
    if admins[login] == passw:
        print('Welcome',login)
        while True:
    
            main()
    else:
        print('Invalid password,will detonate in 5 seconds!')
else:
    print('Invalid username,calling the FBI to report this')