# -*- coding: utf-8 -*-
"""
Created on Sat Jan 20 10:19:12 2024

@author: DELL
"""

import pandas as pd
import matplotlib.pyplot as plt

print("*" * 40)
print(" Welcome to Resort Management System")
print("*" * 40)

f = 1

while f != -1:
    print("-" * 40)
    print("List of files:")
    print("Enter 1 to open Employee File")
    print("Enter 2 to open Visitor File")
    print("Enter 3 to open Rooms File")
    print("Enter 4 to open Payment File")
    print("Enter -1 to stop the Application")
    print("-" * 40)
    
    try:
        f = int(input("Enter the file number "))
        
        if f == 1:
            df = pd.read_csv("C:/csv_files/Employee.csv")
            print("Employee file opened")
            ch = 1
            
            while ch != -1:
                print("-" * 40)
                print("Enter your choice")
                print("1-To display the full  dataframe")
                print("2-Add a column")
                print("3-To add a row")
                print("4-To delete a column")
                print("5-To delete a row")
                print("6-To search for a row")
                print("7-To see the entire record of an employee")
                print("8-To sort the salary values in descending order")
                print("9-For grouping of records")
                print("10-To display the required columns")
                print("11-to display first n rows")
                print("12-to display last n rows")
                print("13-to generate a bar chart between job title and salary")
                print("14-to generate a pie chart between job title and salary")
                print("15-to generate a histogram for salary")
                print("-1 – Save and close the file")
                print("-" * 40)
                
                try:
                    ch = int(input("Enter your choice"))

                    if ch == 1:
                        print(df.loc[:, :])
                    elif ch == 2:
                        n = input("Enter your column heading: ")
                        v = eval(input("Enter the 3 values in list: "))
                        df[n] = v
                        print("The new column is added successfully")
                    elif ch == 3:
                        r = input("Enter the row label: ")
                        v = eval(input("Enter the 7 values: "))
                        df.loc[r, :] = v
                        print("The new row is added successfully")
                    elif ch == 4:
                        v = input("Enter the name of the column which you want to delete: ")
                        df = df.drop(v, axis=1, inplace=True)
                        print("The specified column is deleted successfully")
                    elif ch == 5:
                        v = input("Enter the column label which you want to delete: ")
                        df = df.drop(v, axis=0, inplace=True)
                        print("The specified row is deleted successfully")
                    elif ch == 6:
                        v = input("Enter the label of that row which you want to search: ")
                        print(df.loc[v, :])
                        print("Your required row")
                    elif ch == 7:
                        v = input("Enter the employee name whose record you want to see: ")
                        print(df[df.name == v])
                    elif ch == 8:
                        print(df.sort_values(by='Salary', ascending=False))
                    elif ch == 9:
                        gdf = df.groupby("Gender")
                        print(gdf["Salary"].sum())
                    elif ch == 10:
                        v = input("Enter the name of the column which you want to search: ")
                        print(df.loc[:, v])
                        print("Your required columns")
                    elif ch == 11:
                        print("Your dataframe contains just 3 rows")
                        v = int(input("Enter how many rows you want to display: "))
                        print(df.head(v))
                    elif ch == 12:
                        print("Your dataframe contains just 3 rows")
                        v = int(input("Enter how many rows you want to display from the last: "))
                        print(df.tail(v))
                    elif ch == 13:
                        e = ['Cook', 'Receptionist', 'Manager']
                        m = [100000, 75000, 90000]
                        plt.figure(figsize=(5, 7), facecolor="c ")
                        plt.bar(e, m)
                        plt.xlabel('POST')
                        plt.ylabel('SALARY')
                        plt.title("Salary and Post Analysis")
                        plt.show()
                    elif ch == 14:
                        e = ['Cook', 'Receptionist', 'Manager']
                        m = [100000, 75000, 90000]
                        plt.pie(m, labels=e, colors=['b', 'r', 'g'], autopct='%3.2f%%')
                        plt.show()
                    elif ch == 15:
                        salary = [100000, 75000, 90000]
                        plt.hist(salary, bins=5, edgecolor='m', linewidth=3)
                        plt.show()
                    elif ch == -1:
                        df.to_csv("C:/csv_files/Employee.csv", index=False)
                        print("Employee file saved and closed")
                        break
                    else:
                        print("Invalid operation number/data ")
                
                except:
                    print("Error in operation")

        elif f == 2:
            # Similar corrections for the Visitor, Rooms, and Payment sections...
            pass

        elif f == 3:
            # Similar corrections for the Rooms section...
            pass

        elif f == 4:
            # Similar corrections for the Payment section...
            pass

        elif f == -1:
            print("Application Closed")
            break

        else:
            print("Invalid file number")

    except:
        print("Error")