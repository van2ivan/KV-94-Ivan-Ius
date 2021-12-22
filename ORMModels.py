from sqlalchemy import BigInteger, Column, DateTime, Float, ForeignKey, Numeric, String, Table, Text, text
from sqlalchemy.dialects.postgresql import OID
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class Pupil(Base):
    __tablename__ = 'Pupils'

    Id = Column(BigInteger, primary_key=True, server_default=text("nextval('\"Pupils_Id_seq\"'::regclass)"))
    Name = Column(String(20), nullable=False)
    Patronymic = Column(String(20), nullable=False)
    Surname = Column(String(20), nullable=False)


class Teacher(Base):
    __tablename__ = 'Teachers'

    id = Column(BigInteger, primary_key=True, unique=True, server_default=text("nextval('\"Teachers_id_seq\"'::regclass)"))
    name = Column(String(20), nullable=False)
    surname = Column(String(20), nullable=False)

class Mark(Base):
    __tablename__ = 'Marks'

    id = Column(BigInteger, primary_key=True, unique=True, server_default=text("nextval('\"Marks_id_seq\"'::regclass)"))
    time = Column(DateTime, nullable=False)
    pupilsid = Column(ForeignKey('Pupils.Id'), nullable=False)
    teachersid = Column(ForeignKey('Teachers.id'), nullable=False)

    Pupil = relationship('Pupil')
    Teacher = relationship('Teacher')


class Subject(Base):
    __tablename__ = 'Subjects'

    id = Column(BigInteger, primary_key=True, unique=True, server_default=text("nextval('\"Subjects_id_seq\"'::regclass)"))
    name = Column(String(20), nullable=False)
    marksid = Column(ForeignKey('Marks.id'), nullable=False)

    Mark = relationship('Mark')


class PupilsSubject(Base):
    __tablename__ = 'PupilsSubjects'

    id = Column(BigInteger, primary_key=True, unique=True, server_default=text("nextval('\"PupilsSubjects_id_seq\"'::regclass)"))
    pupilsid = Column(ForeignKey('Pupils.Id'), nullable=False)
    subjectsid = Column(ForeignKey('Subjects.id'), nullable=False)

    Pupil = relationship('Pupil')
    Subject = relationship('Subject')


class TeachersSubject(Base):
    __tablename__ = 'TeachersSubjects'

    id = Column(BigInteger, primary_key=True, unique=True, server_default=text("nextval('\"TeachersSubjects_id_seq\"'::regclass)"))
    teachersid = Column(ForeignKey('Teachers.id'), nullable=False)
    subjectsid = Column(ForeignKey('Subjects.id'), nullable=False)

    Subject = relationship('Subject')
    Teacher = relationship('Teacher')
