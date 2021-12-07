import Database
from Model import Model
from datetime import datetime

class View:
    def __init__(self, table, datas):
        self.table = table
        self.datas = datas


    @staticmethod
    def listof():
        print('''
        1                 => Subjects
        2                 => Teachers
        3                 => Pupils
        4                 => Marks 
        5                 => PupilsSubjects
        6                 => TeachersSubjects
        ''')

    @staticmethod
    def listofdata(choice):
        if choice == 1:
            print('''
            1 => id
            2 => name
            3 => marksID
            ''')
        elif choice == 2:
            print('''
            1 => id
            2 => Name
            3 => Surname
            ''')
        elif choice == 3:
            print('''
            1 => id
            2 => Name
            3 => Surname
            4 => Patronymic
            ''')
        elif choice == 4:
            print('''
            1 => id
            2 => time
            3 => pupilsID
            4 => teachersID
            ''')
        elif choice == 5:
            print('''
            1 => id
            2 => pupilsID
            3 => subjectsID
            ''')
        elif choice == 6:
            print('''
            1 => id
            2 => teachersID
            3 => subjectsID
            ''')

    def output_spec(self):
        if self.table == 1:
            print("***************************\n")
            print('teacher name      teacher surname       pupil name          pupil surname')
            for column in self.datas:
                print(
                    "{:18s}{:22s}{:20s}{}".format(column[0], column[1], column[2], column[3]))
            print("***************************\n")
        elif self.table == 2:
            print("***************************\n")
            print('teacher name       teacher surname          subjects name        marks time')
            for column in self.datas:
                print(
                    "{:19s}{:25s}{:21s}{}".format(column[0], column[1], column[2], column[3]))
            print("***************************\n")
        elif self.table == 3:
            print("***************************\n")
            print('Name')
            for column in self.datas:
                print(
                    "{}".format(column[0]))
            print("***************************\n")
        else:
            print('Something gone wrong')

    def output(self):
        print("***************************\n")
        if self.table == 1:
            print('id       name           marksID')
            for column in self.datas:
               print("{:<9}{:<15}{}".format(column[0], column[1], column[2]))
            print("***************************\n")
        elif self.table == 2:
            print('id       Name      Surname')
            for column in self.datas:
                print("{:<9}{:<10}{}".format(column[0], column[1], column[2]))
            print("***************************\n")
        elif self.table == 3:
            print('id       Name     Patronymic      Surname')
            for column in self.datas:
                print("{:<9}{:<9}{:16}{}".format(column[0], column[1], column[2],column[3]))
            print("***************************\n")
        elif self.table == 4:
            print('id       time                      pupilsID      teachersID')
            for column in self.datas:
              print("{:<9}{:<26}{:<14}{}".format(column[0], str(column[1]), column[2], column[3]))
            print("***************************\n")

        elif self.table == 5:
            print('id       pupilsID     subjectID')
            for column in self.datas:
                print("{:<9}{:<13}{}".format(column[0], column[1], column[2]))
            print("***************************\n")
        elif self.table == 6:
            print('id       teachersID     subjectsID')
            for column in self.datas:
              print("{:<9}{:<15}{}".format(column[0], column[1], column[2]))
            print("***************************\n")




class Menu:

    @staticmethod
    def mainmenu():
        check = True
        while check:
            print('''
             1 => One table
             2 => All tables
             3 => Insertion
             4 => Delete some inf
             5 => Updating
             6 => Selection
             7 => Random inf
             ...
             0 = > Exit
            ''')

            choice = input('Your choice is: ')
            if choice == '1':
                View.listof()
                table = input('Choose your table:')
                table = Model.existingtable(table)
                if table == 0:
                    continue
                datas = Model.outputonetable(table)
                obj = View(table, datas)
                obj.output()
            elif choice == '2':
                for table in range(1, 7):
                    datas = Model.outputonetable(table)
                    obj = View(table, datas)
                    obj.output()
            elif choice == '3':
                ins = True
                while ins:
                    View.listof()
                    table = input('Choose your table: ')
                    table = int(table)
                    table = Model.existingtable(table)
                    if table == 0:
                        continue
                    elif table == 1:
                        f = input('name = ')
                        s = input('marksID = ')
                        added = "'Record added'"
                        notice = "'Mark with ID={} is not exists'".format(s)
                        if str(f).isalnum() and s.isdigit():
                            s = "'" + s + "'"
                            f = "'" + f + "'"
                            Model.insertSubject(f, s, added, notice)
                        else:
                            print('The value types are wrong')
                    elif table == 2:
                        f = input('Name = ')
                        s = input('Surname = ')
                        notice = 'something went wrong'
                        notice = "'" + notice + "'"
                        added = 'added'
                        added = "'" + added + "'"
                        if str(f).isalnum() and str(s).isalnum():
                            Model.insertTeacher(f, s, added, notice)
                        else:
                            print('The values are wrong')

                    elif table == 3:
                        f = input('Name = ')
                        s = input('Patronymic = ')
                        t = input('Surname = ')

                        notice = "'Something went wrong'"
                        added = 'added'
                        added = "'" + added + "'"

                        if str(f).isalnum() and s.isalnum() and t.isalnum():
                            f = "'" + f + "'"
                            s = "'" + s + "'"
                            t = "'" + t + "'"
                            Model.insertPupil(f,s,t,added,notice)
                        else:
                            print('The values are wrong')
                    elif table == 4:
                        f = input('time (%d/%m/%y %H:%M:%S) = ')
                        s = input('pupilsID = ')
                        t = input('teachersID = ')
                        notice = 'pupil with ID = {} or teacher with id = {} is not exists'.format(s, t)
                        notice = "'" + notice + "'"
                        added = 'added'
                        added = "'" + added + "'"
                        timestamp = datetime.strptime(f, '%d/%m/%y %H:%M:%S')
                        if str(s).isdigit() and str(t).isdigit() and timestamp:
                            Model.insertMark(s,t, timestamp, added,notice)
                        else:
                            print('The values are wrong')
                    else:
                        print('Insert for such table is forbidden')
                    cont = True
                    while cont:
                        ch = input('1 => Continue insertion, 2 => Stop insertion => ')
                        if ch == '2':
                            ins = False
                            cont = False
                        elif ch == '1':
                            cont = False
                            pass
                        else:
                            print('Try again')
            elif choice == '4':
                delete = 'deleted'
                delete = "'" + delete + "'"
                notice = 'Entered ID is wrong'
                notice = "'" + notice + "'"
                dele = True
                while dele:
                    View.listof()
                    table = input('Choose your table:')

                    table = Model.existingtable(table)
                    if table == 1:
                            idk = input('Attribute to delete ID = ')
                            if str(idk).isdigit():
                                Model.deleteSubject(idk,delete,notice)
                            else:
                                print('The value are wrong')
                    elif table == 2:
                            idk = input('Attribute to delete ID = ')
                            if str(idk).isdigit():
                                Model.deleteTeachers(idk,delete,notice)
                            else:
                                print('The value are wrong')
                    elif table == 3:
                            idk = input('Attribute to delete ID = ')
                            if str(idk).isdigit():
                                Model.deletePupils(idk,delete,notice)
                            else:
                                print('The value are wrong')
                    elif table == 4:
                            idk = input('Attribute to delete ID = ')
                            if str(idk).isdigit():
                                Model.deleteMarks(idk,delete,notice)
                            else:
                                print('The value are wrong')

                    cont = True
                    while cont:
                        ch = input('1 => Continue delete, 2 => Stop delete => ')
                        if ch == '2':
                            dele = False
                            cont = False
                        elif ch == '1':
                            cont = False
                            pass
                        else:
                            print('Try again')
            elif choice == '5':
                updated = 'updated'
                updated = "'" + updated + "'"
                upd = True
                while upd:
                    View.listof()
                    table = input('Choose your table:')
                    table = Model.existingtable(table)
                    table = int(table)
                    #View.listofdatatoupdate(table)

                    if table == 1:
                        idk = input('Row to update where id = ')
                        notice = 'id = {} is not present in table.'.format(idk)
                        notice = "'" + notice + "'"
                        name = input('New name = ')
                        if name.isalnum():
                            name = "'" + name + "'"
                            Model.UpdateSubject(idk, name, updated, notice)
                        else:
                            print('The values are wrong')
                    elif table == 2:
                        idk = input('Row to update where id = ')
                        notice = 'id = {} is not present in table.'.format(idk)
                        notice = "'" + notice + "'"
                        set1 = input('Name = ')
                        set2 = input('Surname = ')

                        if str(idk).isdigit() and str(set1).isalnum() and str(set2).isalnum():
                            set1 = "'" + set1 + "'"
                            set2 = "'" + set2 + "'"
                            Model.UpdateTeachers(idk, set1, set2, updated, notice)
                        else:
                            print('The values are wrong')
                    elif table == 3:
                        idk = input('Row to update where id = ')
                        notice = 'id = {} is not present in table.'.format(idk)
                        notice = "'" + notice + "'"
                        name = input('Name = ')
                        patronymic = input('Patronymic = ')
                        surname = input('Surname = ')
                        if str(idk).isdigit() and name.isalnum() and patronymic.isalnum() and surname.isalnum():
                            name = "'" + name + "'"
                            patronymic = "'" + patronymic + "'"
                            surname = "'" + surname + "'"
                            Model.UpdatePupils(idk, name, patronymic, surname, updated, notice)
                        else:
                            print('The values are wrong')
                    elif table == 4:
                        idk = input('Row to update where id = ')
                        notice = 'id = {} is not present in table.'.format(idk, idk)
                        notice = "'" + notice + "'"
                        dateTimeInput = input('time (%d/%m/%y %H:%M:%S) = ')
                        date = datetime.strptime(dateTimeInput, '%d/%m/%y %H:%M:%S')
                        if date:
                            Model.UpdateMarks(idk, date, updated, notice)
                        else:
                            print('The values are wrong')
                    else:
                        print('Something went wrong')
                    cont = True
                    while cont:
                        ch = input('1 => Continue update, 2 => Stop update => ')
                        if ch == '2':
                            upd = False
                            cont = False
                        elif ch == '1':
                            cont = False
                            pass
                        else:
                            print('Try again')
            elif choice == '6':
                sel = True
                while sel:
                    print('----------------------------------------')
                    print('1 => Show Teachers and related to them Pupils where mark datetime is greater then X'
                          ' and Teachers surname like Y')
                    print('----------------------------------------')
                    print(
                        '2 => Show teachers that teach subjects with name like X and post a marks starting from date Y')
                    print('----------------------------------------')
                    print('3 => Show name of ongoing subjects (have teachers, students and marks)')
                    print('----------------------------------------')
                    choice = input('Your choice is ')
                    choice = int(choice)
                    if choice == 1:
                        time = input('Enter time criteria (Y-m-d H:M:S) = ')
                        sur = input('Enter teachers surname criteria = ')
                        datas = Model.selectionone(time, sur)
                        obj = View(choice, datas)
                        obj.output_spec()
                    elif choice == 2:
                        subj = input('Enter subject name criteria = ')
                        time = input('Enter time criteria (Y-m-d H:M:S) = ')
                        datas = Model.selectiontwo(subj, time)
                        obj = View(choice, datas)
                        obj.output_spec()
                    elif choice == 3:
                        teachersS = input('Enter teachers surname criteria = ')
                        pupilsS = input('Enter pupils surname criteria = ')
                        datas = Model.selectionthree(teachersS, pupilsS)
                        obj = View(choice, datas)
                        obj.output_spec()
                    else:
                        print('Try again')
                    cont = True
                    while cont:
                        ch = input('1 => Continue selection, 2 => Stop selection => ')
                        if ch == '2':
                            sel = False
                            cont = False
                        elif ch == '1':
                            cont = False
                            pass
                        else:
                            print('Try again')
            elif choice == '7':
                ra = True
                while ra:
                    View.listof()
                    table = input("Choose your table: ")
                    table = Model.existingtable(table)
                    if table == 0:
                        print('Something went wrong')
                        continue
                    kolvo = input('How much datas do you want to add => ')
                    if not str(kolvo).isdigit():
                        print('Something wrong')
                        continue
                    Model.randomik(table, kolvo)
                    cont = True
                    while cont:
                        ch = input('1 => Continue random, 2 => Stop random => ')
                        if ch == '2':
                            ra = False
                            cont = False
                        elif ch == '1':
                            cont = False
                            pass
                        else:
                            print('Try again')
            elif choice == '0':
                check = False
            else:
                print('Try again')

            cont = True
            while cont:
                con = input('Continue to work with db => 1, stop => 2. Your choice =>')
                if con == '2':
                    check = False
                    cont = False
                elif con == '1':
                    cont = False
                    check = True
                else:
                    print('Try again')