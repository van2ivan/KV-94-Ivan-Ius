import random

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine, Sequence, delete, insert, update, select
from sqlalchemy import String, Integer, Float, Boolean, Column
from sqlalchemy.orm import sessionmaker

import Database
import time
from ORMModels import *

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
    def getTableClass(choice):
        if choice == 1:
            return Subject
        elif choice == 2:
            return Teacher
        elif choice == 3:
            return Pupil
        elif choice == 4:
            return Mark
        elif choice == 5:
            return PupilsSubject
        elif choice == 6:
            return TeachersSubject

    @staticmethod
    def outputonetable(table):
        engine = Database.getEngine()
        Session = sessionmaker(bind=engine)
        session = Session()

        return session.query(Model.getTableClass(table)).all()


    @staticmethod
    def insertSubject(f,s,added,notice):
        try:
            engine = Database.getEngine()
            Session = sessionmaker(bind=engine)
            session = Session()

            subj = Subject(name=f, marksid=int(s))
            session.add(subj)
            session.commit()
            print(added)
        except:
            print(notice)

    @staticmethod
    def insertTeacher(f, s, added, notice):
        try:
            engine = Database.getEngine()
            Session = sessionmaker(bind=engine)
            session = Session()

            subj = Teacher(name=f, surname=s)
            session.add(subj)
            session.commit()
            print(added)
        except:
            print(notice)

    @staticmethod
    def insertPupil(f,s,t,added,notice):
        try:
            engine = Database.getEngine()
            Session = sessionmaker(bind=engine)
            session = Session()

            subj = Pupil(Name=f, Surname=s, Patronymic=t)
            session.add(subj)
            session.commit()
            print(added)
        except:
            print(notice)

    @staticmethod
    def insertMark(f,s,t,added,notice):
        try:
            engine = Database.getEngine()
            Session = sessionmaker(bind=engine)
            session = Session()

            subj = Mark(time=t, pupilsid=f, teachersid=s)
            session.add(subj)
            session.commit()
            print(added)
        except:
            print(notice)

    @staticmethod
    def deleteSubject(idk, delete, notice):
        try:
            engine = Database.getEngine()
            Session = sessionmaker(bind=engine)
            session = Session()

            subject = session.query(Subject).where(Subject.id == idk).one()
            session.delete(subject)
            session.query(Mark).where(Mark.id == subject.marksid).delete()
            session.commit()
            print(delete)
        except:
           print(notice)

    @staticmethod
    def deleteTeachers(idk, delete, notice):
        try:
            engine = Database.getEngine()
            Session = sessionmaker(bind=engine)
            session = Session()

            session.query(Teacher).where(Teacher.id == idk).delete()
            session.query(Mark).where(Mark.teachersid == idk).delete()
            session.query(TeachersSubject).where(TeachersSubject.teachersid == idk).delete()
            session.commit()
            print(delete)
        except:
           print(notice)

    @staticmethod
    def deletePupils(idk, delete, notice):
        try:
            engine = Database.getEngine()
            Session = sessionmaker(bind=engine)
            session = Session()

            session.query(Pupil).where(Pupil.Id == idk).delete()
            session.query(Mark).where(Mark.pupilsid == idk).delete()
            session.query(PupilsSubject).where(PupilsSubject.pupilsid == idk).delete()
            session.commit()
            print(delete)
        except:
            print(notice)

    @staticmethod
    def deleteMarks(idk, delete, notice):
        try:
            engine = Database.getEngine()
            Session = sessionmaker(bind=engine)
            session = Session()

            session.query(Mark).where(Mark.id == idk).delete()
            session.commit()
            print(delete)
        except:
            print(notice)

    @staticmethod
    def UpdateSubject(idk, name, updated, notice):
        try:
            engine = Database.getEngine()
            Session = sessionmaker(bind=engine)
            session = Session()

            subject = session.query(Subject).where(Subject.id == idk).one()
            subject.name = name
            session.commit()
            print(updated)
        except:
           print(notice)


    @staticmethod
    def UpdateTeachers(idk, set1, set2, updated, notice):
        try:
            engine = Database.getEngine()
            Session = sessionmaker(bind=engine)
            session = Session()

            teacher = session.query(Teacher).where(Teacher.id == idk).one()
            teacher.name = set1
            teacher.surname = set2
            session.commit()
            print(updated)
        except:
           print(notice)

    @staticmethod
    def UpdatePupils(idk, name, patronymic, surname, updated, notice):
        try:
            engine = Database.getEngine()
            Session = sessionmaker(bind=engine)
            session = Session()

            pupil = session.query(Pupil).where(Pupil.Id == idk).one()
            pupil.Name = name
            pupil.Patronymic = patronymic
            pupil.Surname = surname
            session.commit()
            print(updated)
        except:
           print(notice)

    @staticmethod
    def UpdateMarks(idk, date, updated, notice):
        try:
            engine = Database.getEngine()
            Session = sessionmaker(bind=engine)
            session = Session()

            mark = session.query(Mark).where(Mark.id == idk).one()
            mark.time = date
            session.commit()
            print(updated)
        except:
           print(notice)

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