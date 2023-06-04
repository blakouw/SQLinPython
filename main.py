"""Skrypt z kodem do tworzenia, edytowania, wyswietlania i usuwania tabel w jezyku MySql"""
from time import sleep
import mysql.connector
from sqlalchemy import false
from mysql.connector import errorcode
from schemes import TABLES
from tabulate import tabulate
"""Łączenie się z baza danych poprzez localhost"""
db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "root",
    database = "userdatabase"
    )
"""Narzedzie do wykonywania komend w MySQL"""
mycursor=db.cursor()


def create_table(mycursor):
    """Tworzenie tabel"""
    table_name = input("Którą tabele chciałbyś utworzyć?\n [czlowiek]\n [uczelnie]\n [zwierzeta]\n [student]\n")
    if table_name == 'czlowiek':
        table_description = TABLES[table_name]
        try:
            print(f"Tworzenie tabeli {table_name}: ",end='')
            mycursor.execute(table_description)
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
                print(f"Tabela {table_name} już istnieje")
            else:
                print(err.msg)
        else:
            print("Utworzono tabele!")
    if table_name == 'uczelnie':
        table_description = TABLES[table_name]
        try:
            print(f"Tworzenie tabeli {table_name}: ",end='')
            mycursor.execute(table_description)
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
                print(f"Tabela {table_name} już istnieje")
            else:
                print(err.msg)
        else:
            print("Utworzono tabele!")
    if table_name == 'zwierzeta':
        table_description = TABLES[table_name]
        try:
            print(f"Tworzenie tabeli {table_name}: ",end='')
            mycursor.execute(table_description)
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
                print(f"Tabela {table_name} już istnieje")
            else:
                print(err.msg)
        else:
            print("Utworzono tabele!")
    if table_name == 'student':
        table_description = TABLES[table_name]
        try:
            print(f"Tworzenie tabeli {table_name}: ",end='')
            mycursor.execute(table_description)
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
                print(f"Tabela {table_name} już istnieje")
            else:
                print(err.msg)
        else:
            print("Utworzono tabele!")

def insert_into(user_decision):
    """Dodawanie wartosci do danej tabeli"""
    if user_decision == "czlowiek":
        phone_number = int(input("Phone nuber: "))
        name = input("Name: ")
        surname = input("Surname: ")
        sex = input("Sex [M/F]: ")
        city = input("City: ")
        add_human = "INSERT INTO czlowiek(phone_number, name, surname,sex,city) values('{}','{}','{}','{}','{}')".format(phone_number, name, surname, sex, city)
        mycursor.execute(add_human)
        db.commit()
    if user_decision == "uczelnie":
        collage_name = input("Nazwa uczelni: ")
        collage_city = input("Miasto: ")
        add_collage = "INSERT INTO uczelnie(nazwa_uczelni, miasto) values('{}','{}')".format(collage_name,collage_city)
        mycursor.execute(add_collage)
        db.commit()
    if user_decision == "zwierzeta":
        animal_species = input("Gatunek: ")
        animal_name = input("Imie: ")
        animal_colour = input("Kolor: ")
        add_animal = "INSERT INTO zwierzeta(gatunek, imie, kolor) values('{}','{}','{}')".format(animal_species, animal_name, animal_colour)
        mycursor.execute(add_animal)
        db.commit()
    if user_decision == "student":
        student_age = int(input("Wiek: "))
        student_name = input("Iime: ")
        student_surname = input("Nazwisko: ")
        student_sex = input("Plec[M/F]: ")
        student_city = input("Miasto: ")
        student_collage = input("Nazwa uczelni: ")
        student_grade = int(input("Ocena: "))
        add_student = "INSERT INTO student(wiek, imie, nazwisko, plec, miasto, nazwa_uczelni, ocena) values('{}','{}','{}','{}','{}','{}','{}')".format(student_age, student_name, student_surname, student_sex, student_city, student_collage, student_grade)
        mycursor.execute(add_student)
        db.commit()

def print_table(user_choice):
    """Wyswietlanie tabeli wedlug wyboru uzytkownika"""
    if user_choice == "czlowiek":
        mycursor.execute("SELECT* FROM czlowiek")
        myresult = mycursor.fetchall()
        print(tabulate(myresult, headers=['phone_number', 'name','surname','sex','city'], tablefmt='psql'))
        sleep(8)
    if user_choice == "uczelnie":
        mycursor.execute("SELECT* FROM uczelnie")
        myresult = mycursor.fetchall()
        print(tabulate(myresult, headers=['nazwa_uczelni', 'miasto'], tablefmt='psql'))
        sleep(8)
    if user_choice == "zwierzeta":
        mycursor.execute("SELECT* FROM zwierzeta")
        myresult = mycursor.fetchall()
        print(tabulate(myresult, headers=['gatunek', 'imie','kolor'], tablefmt='psql'))
        sleep(8)
    if user_choice == "student":
        mycursor.execute("SELECT* FROM student")
        myresult = mycursor.fetchall()
        print(tabulate(myresult, headers=['wiek', 'imie','nazwisko','plec','miasto', 'nazwa_uczelni', 'ocena'], tablefmt='psql'))
        sleep(8)

def drop_table(user_choice):
    """Usuwanie tabeli wedlug wyboru uzytkownika"""
    if user_choice == "czlowiek":
        mycursor.execute("DROP TABLE IF EXISTS czlowiek")
        print(f"Usunięto tabele {user_choice}!")
    if user_choice == "uczelnie":
        mycursor.execute("DROP TABLE IF EXISTS uczelnie")
        print(f"Usunięto tabele {user_choice}!")
    if user_choice == "zwierzeta":
        mycursor.execute("DROP TABLE IF EXISTS zwierzeta")
        print(f"Usunięto tabele {user_choice}!")
    if user_choice == "student":
        mycursor.execute("DROP TABLE IF EXISTS student")
        print(f"Usunięto tabele {user_choice}!")

print("\nWitaj w menadżerze bazy danych!!!\n")
"""Glowna petla"""
while True:
    print("\nWybierz co chciałbyś zrobić\n [1] Stworz tabele\n [2] Dodaj do tabeli\n [3] Pokaz wszystkie tabele\n [4] Pokaz tabele\n [5] Usun tabele\n [6] Wyjdź\n")
    user_input = int(input(">"))
    if user_input == 1:
        create_table(mycursor)

    if user_input == 2:
        which = input("Do której tabeli chciałbyś dodać?\n [czlowiek]\n [uczelnie]\n [zwierzeta]\n [student]\n")
        if which == "czlowiek":
            insert_into(which)
        if which == "uczelnie":
            insert_into(which)
        if which == "zwierzeta":
            insert_into(which)
        if which == "student":
            insert_into(which)

    if user_input == 3:
        try:
            mycursor.execute("SHOW TABLES")
            myresult = mycursor.fetchall()
            for x in myresult:
                print(x)
                print("\n")
            sleep(5)
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_NO_TABLES_USED:
                print(f"Nie ma tabel!")
            else:
                print(err.msg)

    if user_input == 4:
        which = input("Którą tabele chciałbyś usunąć?\n [czlowiek]\n [uczelnie]\n [zwierzeta]\n [student]\n")
        if which == "czlowiek":
            print_table(which)
        if which == "uczelnie":
            print_table(which)
        if which == "zwierzeta":
            print_table(which)
        if which == "student":
            print_table(which)

    if user_input == 5:
        which = input("Którą tabele chciałbyś wyświetlić?\n [czlowiek]\n [uczelnie]\n [zwierzeta]\n [student]\n")
        if which == "czlowiek":
            drop_table(which)
        if which == "uczelnie":
            drop_table(which)
        if which == "zwierzeta":
            drop_table(which)
        if which == "student":
            drop_table(which)

    if user_input == 6:
        break

