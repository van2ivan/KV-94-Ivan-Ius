import random
import Database
import time

Tables = {
    1: 'Subjects',
    2: 'Teachers',
    3: 'Pupils',
    4: 'Marks',
    5: 'PupilsSubjects',
    6: 'TeachersSubjects'
}

class Model:
    @staticmethod
    def existingtable(table):
        if str(table).isdigit():
             table = int(table)
             cons = True
             while cons:
                if table == 1 or table == 2 or table == 3 or table == 4 or table == 5 or table == 6:
                   return table
                else:
                   print('///Try again.')
                   return 0
        else:
             print('Try again')
             return 0


    @staticmethod
    def outputonetable(table):
        connect = Database.connect()
        cursor = connect.cursor()
        show = 'select * from public."{}"'.format(Tables[table])
        print("SQL query => ", show)
        print('')
        cursor.execute(show)
        datas = cursor.fetchall()
        cursor.close()
        Database.close(connect)
        return datas

    @staticmethod
    def insertSubject(f,s,added,notice):
        connect = Database.connect()
        cursor = connect.cursor()
        insert = 'DO $$ BEGIN if (1=1) and exists (select id from public."Marks" where id = {}) ' \
                 'then INSERT INTO public."Subjects"(name, marksID) VALUES ({},{}); ' \
                 'raise notice {}; else raise notice {}; ' \
                 'end if; end $$;'.format(s, f, s, added, notice)
        cursor.execute(insert)
        connect.commit()
        print(connect.notices)
        cursor.close()
        Database.close(connect)

    @staticmethod
    def insertTeacher(f, s, added, notice):
        connect = Database.connect()
        cursor = connect.cursor()
        insert = 'DO $$	BEGIN IF (1=1) THEN ' \
                 'INSERT INTO public."Teachers"(name, surname) values (\'{}\', \'{}\'); ' \
                 'RAISE NOTICE {};' \
                 ' ELSE RAISE NOTICE {};' \
                 'END IF; ' \
                 'END $$;'.format(f, s, added, notice)
        cursor.execute(insert)
        connect.commit()
        print(connect.notices)
        cursor.close()
        Database.close(connect)

    @staticmethod
    def insertPupil(f,s,t,added,notice):
        connect = Database.connect()
        cursor = connect.cursor()
        insert = 'DO $$ BEGIN IF (1=1) THEN ' \
                 'INSERT INTO public."Pupils"("Name", "Patronymic", "Surname") values ({}, {}, {}); ' \
                 'RAISE NOTICE {};' \
                 ' ELSE RAISE NOTICE {};' \
                 'END IF; ' \
                 'END $$;'.format(f,s,t, added, notice)
        cursor.execute(insert)
        connect.commit()
        print(connect.notices)
        cursor.close()
        Database.close(connect)

    @staticmethod
    def insertMark(f,s,t,added,notice):
        connect = Database.connect()
        cursor = connect.cursor()
        insert = 'DO $$	BEGIN IF EXISTS (select "Id" from public."Pupils" where "Id" = {}) and exists (select id from public."Teachers" where id = {}) THEN ' \
                 'INSERT INTO public."Marks"(time, pupilsID, teachersID) values (\'{}\', {}, {}); ' \
                 'RAISE NOTICE {};' \
                 ' ELSE RAISE NOTICE {};' \
                 'END IF; ' \
                 'END $$;'.format(f, s, t, f, s, added, notice)
        cursor.execute(insert)
        connect.commit()
        print(connect.notices)
        cursor.close()
        Database.close(connect)

    @staticmethod
    def deleteSubject(idk, delete, notice):
        connect = Database.connect()
        cursor = connect.cursor()
        delete = 'DO $$ BEGIN IF EXISTS (select id from public."Subjects" where id = {}) then ' \
                 'delete from public."Marks" where id in (select marksID from public."Subjects" where id = {});' \
                 'delete from public."Subjects" where id = {};' \
                 'raise notice {};' \
                 'else raise notice {};' \
                 'end if;' \
                 'end $$;'.format(idk, idk, idk, delete, notice)
        cursor.execute(delete)
        connect.commit()
        print(connect.notices)
        cursor.close()
        Database.close(connect)

    @staticmethod
    def deleteTeachers(idk, delete, notice):
        connect = Database.connect()
        cursor = connect.cursor()
        delete = 'DO $$ BEGIN if ' \
                 'exists (select id from public."Teachers" where id = {}) then ' \
                 'delete from public."TeachersSubjects" where teachersID = {};' \
                 'delete from public."Marks" where teachersID = {};' \
                 'delete from public."Teachers" where id = {};' \
                 'raise notice {};' \
                 'else raise notice {};' \
                 'end if;' \
                 'end $$;'.format(idk, idk, idk, idk, delete, notice)
        cursor.execute(delete)
        connect.commit()
        print(connect.notices)
        cursor.close()
        Database.close(connect)

    @staticmethod
    def deletePupils(idk, delete, notice):
        connect = Database.connect()
        cursor = connect.cursor()
        delete = 'DO $$ BEGIN if ' \
                 'exists (select "Id" from public."Pupils" where "Id" = {}) then ' \
                 'delete from public."PupilsSubjects" where pupilsID = {};' \
                 'delete from public."Marks" where pupilsID = {};' \
                 'delete from public."Pupils" where "Id" = {};' \
                 'raise notice {};' \
                 'else raise notice {};' \
                 'end if;' \
                 'end $$;'.format(idk, idk, idk, idk, delete, notice)
        cursor.execute(delete)
        connect.commit()
        print(connect.notices)
        cursor.close()
        Database.close(connect)

    @staticmethod
    def deleteMarks(idk, delete, notice):
        connect = Database.connect()
        cursor = connect.cursor()
        delete = 'DO $$ BEGIN if exists (select id from public."Marks" where id = {}) then ' \
                 'delete from public."Marks" where id = {};' \
                 'raise notice {};' \
                 'else raise notice {};' \
                 'end if;' \
                 'end $$;'.format(idk, idk, delete, notice)
        cursor.execute(delete)
        connect.commit()
        print(connect.notices)
        cursor.close()
        Database.close(connect)

    @staticmethod
    def UpdateSubject(idk, name, updated, notice):
        connect = Database.connect()
        cursor = connect.cursor()
        update = 'DO $$ BEGIN IF EXISTS (select id from public."Subjects" where id = {}) THEN ' \
                 'update public."Subjects" set name = {} where id = {}; ' \
                 'RAISE NOTICE {};' \
                 ' ELSE RAISE NOTICE {};' \
                 'END IF; ' \
                 'END $$;'.format(idk, name, idk, updated, notice)
        cursor.execute(update)
        connect.commit()
        print(connect.notices)
        cursor.close()
        Database.close(connect)


    @staticmethod
    def UpdateTeachers(idk, set1, set2, updated, notice):
        connect = Database.connect()
        cursor = connect.cursor()
        update = 'DO $$ BEGIN IF EXISTS (select id from public."Teachers" where id = {})' \
                 ' THEN ' \
                 'update public."Teachers" set Name = {}, Surname = {} where id = {}; ' \
                 'RAISE NOTICE {};' \
                 ' ELSE RAISE NOTICE {};' \
                 'END IF; ' \
                 'END $$;'.format(idk, set1, set2, idk, updated, notice)
        cursor.execute(update)
        connect.commit()
        print(connect.notices)
        cursor.close()
        Database.close(connect)

    @staticmethod
    def UpdatePupils(idk, name, patronymic, surname, updated, notice):
        connect = Database.connect()
        cursor = connect.cursor()
        update = 'DO $$ BEGIN IF EXISTS (select "Id" from public."Pupils" where "Id" = {}) ' \
                 ' THEN ' \
                 'update public."Pupils" set "Name" = {}, "Patronymic" = {}, "Surname" = {} where "Id" = {}; ' \
                 'RAISE NOTICE {};' \
                 ' ELSE RAISE NOTICE {};' \
                 'END IF; ' \
                 'END $$;'.format(idk, name, patronymic, surname, idk, updated, notice)
        cursor.execute(update)
        connect.commit()
        print(connect.notices)
        cursor.close()
        Database.close(connect)

    @staticmethod
    def UpdateMarks(idk, date, updated, notice):
        connect = Database.connect()
        cursor = connect.cursor()
        update = 'DO $$ BEGIN IF EXISTS (select id from public."Marks" where id = {}) ' \
                 ' THEN ' \
                 'update public."Marks" set time = \'{}\' where id = {}; ' \
                 'RAISE NOTICE {};' \
                 ' ELSE RAISE NOTICE {};' \
                 'END IF; ' \
                 'END $$;'.format(idk, date, idk, updated, notice)
        cursor.execute(update)
        connect.commit()
        print(connect.notices)
        cursor.close()
        Database.close(connect)


    @staticmethod
    def selectionone(timestamp, teacherSurname):
        connect = Database.connect()
        cursor = connect.cursor()
        select = """
        select 
            public."Teachers".name, public."Teachers".surname, 
            public."Pupils"."Name", public."Pupils"."Surname"
            
            from public."Teachers"
            right join public."Marks" on public."Marks".teachersid = public."Teachers".id
            left join public."Pupils" on public."Marks".pupilsid = public."Pupils"."Id"
            
            where public."Marks".time > '{}'
                and public."Teachers".surname like '{}'
        """.format(timestamp, teacherSurname)
        print("SQL query => ", select)
        beg = int(time.time() * 1000)
        cursor.execute(select)
        end = int(time.time() * 1000) - beg
        datas = cursor.fetchall()
        print('Time of request {} ms'.format(end))
        print('Selected')
        cursor.close()
        Database.close(connect)
        return datas

    @staticmethod
    def selectiontwo(subj, markTime):
        connect = Database.connect()
        cursor = connect.cursor()
        select = """
        select 
            public."Teachers".name, public."Teachers".surname, 
            public."Subjects".name,
            public."Marks".time
            
            from public."Subjects"
            join public."Marks"on public."Marks".id = public."Subjects".marksid
            join public."Teachers" on public."Marks".teachersid = public."Teachers".id
            
            where public."Subjects".name like '{}'
                and public."Marks".time > '{}'
        """.format(subj, markTime)
        print("SQL query => ", select)
        beg = int(time.time() * 1000)
        cursor.execute(select)
        end = int(time.time() * 1000) - beg
        datas = cursor.fetchall()
        print('Time of request {} ms'.format(end))
        print('Selected')
        cursor.close()
        Database.close(connect)
        return datas

    @staticmethod
    def selectionthree(teachersS, pupilsS):
        connect = Database.connect()
        cursor = connect.cursor()
        select = """
        select public."Subjects".name from public."Subjects"

            join public."Marks"on public."Marks".id = public."Subjects".marksid
            
            join public."TeachersSubjects" 
                on public."TeachersSubjects".subjectsid = public."Subjects".id
                and public."TeachersSubjects".teachersid = public."Marks".teachersid
            
            join public."PupilsSubjects" 
                on public."PupilsSubjects".subjectsid = public."Subjects".id
                and public."PupilsSubjects".pupilsid = public."Marks".pupilsid 
            
            join public."Pupils" on "PupilsSubjects".pupilsid = public."Pupils"."Id"
            join public."Teachers" on public."TeachersSubjects".teachersid = public."Teachers".id
                
            where public."Teachers".surname like '{}'
                and public."Pupils"."Surname" like '{}'
                
            group by public."Subjects".name
        """.format(teachersS, pupilsS)
        print("SQL query => ", select)
        beg = int(time.time() * 1000)
        cursor.execute(select)
        end = int(time.time() * 1000) - beg
        datas = cursor.fetchall()
        print('Time of request {} ms'.format(end))
        print('Selected')
        cursor.close()
        Database.close(connect)
        return datas




    @staticmethod
    def randomik(table, kolvo):
            connect = Database.connect()
            cursor = connect.cursor()
            check = True
            while check:
                if table == 1:
                    res = 0
                    while (True):
                        insert = "INSERT INTO public.\"Subjects\"(Name, MarksID) select chr(trunc(65 + random()*26)::int)||chr(trunc(65 + r" \
                             "andom()*26)::int)," \
                             "(select id from public.\"Marks\" order by random() limit 1)" \
                             " from generate_series(1,{})".format(kolvo)
                        cursor.execute(insert)
                        res = res + 1
                        if(res == int(kolvo)):
                            break
                    check = False
                elif table == 2:
                    res = 0
                    while (True):
                        insert = "INSERT INTO public.\"Teachers\"(Name, Surname) select chr(trunc(65 + random()*26)::int)||chr(trunc(65 + r" \
                             "andom()*26)::int), " \
                             "chr(trunc(65 + random()*26)::int)||chr(trunc(65 + random()*26)::int) " \
                             "from generate_series(1,{})".format(kolvo)
                        cursor.execute(insert)
                        res = res + 1
                        if(res == int(kolvo)):
                            break
                    check = False
                elif table == 3:
                    res = 0
                    while (True):
                        insert = "INSERT INTO public.\"Pupils\"(\"Name\", \"Surname\", \"Patronymic\") select chr(trunc(65 + random()*26)::int)||chr(trunc(65 + r" \
                             "andom()*26)::int), " \
                             "chr(trunc(65 + random()*26)::int)||chr(trunc(65 + random()*26)::int), " \
                             "chr(trunc(65 + random()*26)::int)||chr(trunc(65 + random()*26)::int)" \
                             "from generate_series(1,{})".format(kolvo)
                        cursor.execute(insert)
                        res = res + 1
                        if(res == int(kolvo)):
                            break
                    check = False
                elif table == 4:
                    res = 0
                    while (True):
                        insert = "INSERT INTO public.\"Marks\"(Time, PupilsID, TeachersID) values(" \
                                 "(select NOW() + (random() * (NOW()+'90 days' - NOW())) + '{} days')," \
                                 "(select \"Id\" from public.\"Pupils\" order by random() limit 1)," \
                                 "(select id from public.\"Teachers\" order by random() limit 1))".format(kolvo)
                        cursor.execute(insert)
                        res = res + 1
                        if (res == int(kolvo)):
                            break
                    check = False
                elif table == 5:
                    res = 0
                    while (True):
                        insert = "INSERT INTO public.\"PupilsSubjects\"(PupilsID, SubjectsID) values(" \
                                 "(select \"Id\" from public.\"Pupils\" order by random() limit 1)," \
                                 "(select id from public.\"Subjects\" order by random() limit 1))".format(kolvo)
                        cursor.execute(insert)
                        res = res + 1
                        if (res == int(kolvo)):
                            break
                    check = False
                elif table == 6:
                    res = 0
                    while (True):
                        insert = "INSERT INTO public.\"TeachersSubjects\"(TeachersID, SubjectsID) values(" \
                                 "(select id from public.\"Teachers\" order by random() limit 1)," \
                                 "(select id from public.\"Subjects\" order by random() limit 1))".format(kolvo)
                        cursor.execute(insert)
                        res = res + 1
                        if (res == int(kolvo)):
                            break
                    check = False
            print(Tables[table])
            print("SQL query => ", insert)
            connect.commit()
            print('Inserted randomly')
            cursor.close()
            Database.close(connect)