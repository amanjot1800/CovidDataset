"""
Author: Amanjot Singh
Student number: 040956152

This file is controller of the program. It holds and operates all the Create, Read, Update and Delete functions.
This class is invoked by the view file.

"""
# imports the MySQL connector used to communicate with the database
import mysql.connector as dbc
# imports the record object to instantiate new objects
from model import Record
# imports the file for reading csv operations
import read_data
import pandas as pd
import matplotlib.pyplot as plt


# keeps track of the object id
ids = 0
# this is the main list that stores all the created objects
master_list = []
# database connection
db = dbc.connect(
    host="localhost",
    user="root",
    password="root",
    database="covid_dataset"
)
# cursor object
cur = db.cursor()


def fetch_and_populate():
    """
    This function creates the Record objects by fetching the database with 100 rows only. It loops over all the rows,
    reads the data from each column and creates the object.
    :return: it returns nothing
    """
    cur.execute("SELECT * FROM record")

    result = cur.fetchall()

    empty_list()
    for x in result:
        lst = [x[0], x[1], x[2], x[3], x[4], int(x[5]), int(x[6]), float(x[7]), int(x[8]), int(x[9]), float(x[10])]
        master_list.append(Record(lst))


def create_record(lst):
    """
    This method is passed a list of parameters and it creates a new row in database. It then calls the fetch_and_populate
    function to refresh the list with newly created data.
    :param lst: list of all the parameters of Record object
    :return: A message saying record creating was successful.
    """

    sql = "INSERT INTO record(pruid, prname, prnameFR, date, numconf, numprob, numdeaths, numtotal, numtoday, " \
          "ratetotal) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"

    cur.execute(sql, lst)

    fetch_and_populate()
    db.commit()

    return "Record Created"


def delete_record(idd):
    """
    this method is given a id and it then deletes the record from the database and then refreshes the master_list.
    :param idd: id of the object to be passed
    :return: A message saying successful deletion
    """

    sql = "DELETE FROM record where id = %s"
    cur.execute(sql, [idd])
    db.commit()

    fetch_and_populate()

    return "Record Deleted"


def update_record(idd, new_record):
    """
    This function is given an id which it uses to run a update query on the database to update the object values. After
    updating, it refreshes the master_list
    :param new_record: record to be updated in the database
    :return: success message
    """

    sql = "UPDATE record SET " \
          "pruid = %s, " \
          "prname = %s, " \
          "prnameFR = %s, " \
          "date = %s, " \
          "numconf = %s, " \
          "numprob = %s, " \
          "numdeaths = %s, " \
          "numtotal = %s, " \
          "numtoday = %s, " \
          "ratetotal = %s " \
          "WHERE id = %s"

    cur.execute(sql, [new_record.pruid, new_record.prname, new_record.prnameFR,
                      new_record.date, new_record.numconf, new_record.numprob,
                      new_record.numdeaths, new_record.numtotal, new_record.numtoday,
                      new_record.ratetotal, idd])

    db.commit()

    fetch_and_populate()
    return "Record Updated"


def get_record(idd):
    """
    This function just loops over all the objects in master_list and returns the object with given id.
    :param idd: id of an object
    :return: record object corresponding to given id
    """
    for rec in master_list:
        if rec.id == idd:
            return rec


def empty_list():
    """
    It empties the list and resets the id to 0.
    :return: nothing
    """
    global master_list
    master_list.clear()


def print_records():
    """
    iterates over all the object and prints them
    :return: prints objects, returns nothing.
    """
    for records in master_list:
        print(records)
    print("Showing " + str(len(master_list)) + " records.")


def create_objects_from_file(data_dict):
    """
    This function creates the Record objects by looping over the data_dict list and pulling out all the data from its
    sub-dictionaries. It also updates the id each time it creates a object. All the new objects are stored in
    master_list list.
    :param data_dict: this list contains dictionary corresponding to each record
    :return: it returns nothing
    """
    global ids
    for index in data_dict:
        data_list = [ids]
        for values in index.values():
            data_list.append(values)
        global master_list
        master_list.append(Record(data_list))
        ids += 1


def populate_db():
    """
    This method was called only once in the very beginning when we needed to populate the database with all the
    records from the csv file. It is also used to recreate all the records from the csv file.
    """

    cur.execute("DELETE FROM record")

    empty_list()

    data = read_data.import_data()
    data_dict = data.to_dict("records")
    create_objects_from_file(data_dict)

    sql = "INSERT INTO record(pruid, prname, prnameFR, date, numconf, numprob, numdeaths, numtotal, numtoday, " \
          "ratetotal) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"

    for obj in master_list:
        val = [obj.pruid, obj.prname, obj.prnameFR, obj.date, obj.numconf, obj.numprob, obj.numdeaths, obj.numtotal,
               obj.numtoday, obj.ratetotal]
        cur.execute(sql, val)

    db.commit()


def generate_bar_plot_by_province(provinces):
    """
    This method creates a dictionary to aggregate the numconf and numdeaths data by province. It then plots that data
    using the pandas library and matplotlib library.
    :param provinces: the list of provinces to select and plot
    :return: the plot of numconf and numdeaths by province
    """

    dic = {}

    if 'all' in provinces:
        for record in master_list:
            if record.prname in dic:
                dic[record.prname][0] += record.numconf
                dic[record.prname][1] += record.numdeaths
            else:
                dic[record.prname] = [record.numconf]
                dic[record.prname].append(record.numdeaths)

        df = pd.DataFrame.from_dict(dic, columns=['numconf', 'numdeaths'], orient='index')
        df.plot.bar(rot=90, figsize=(15, 8))
        plt.yscale("log")
        plt.ylabel("Log scale of numconf and numdeaths")
        plt.show()

    else:
        for record in master_list:
            if record.prname in provinces:
                if record.prname in dic:
                    dic[record.prname][0] += record.numconf
                    dic[record.prname][1] += record.numdeaths
                else:
                    dic[record.prname] = [record.numconf]
                    dic[record.prname].append(record.numdeaths)

        df = pd.DataFrame.from_dict(dic, columns=['numconf', 'numdeaths'], orient='index')
        df.plot.bar(rot=90, figsize=(15, 8))
        plt.ylabel("Number of people")
        plt.show()


def generate_bar_plot_total():
    """
    This function sums up the data for various columns like numconf, numdeaths, numtotal and ratetotal and adds that to
    a dictionary. It then creates a plot using pandas library and matplotlib.
    :return: A plot of cases in each category or column.
    """

    dic = {'numconf': 0, 'numprob': 0, 'numdeaths': 0, 'numtotal': 0, 'ratetotal': 0}

    for record in master_list:
        if record.prname == "Canada":
            dic["numconf"] += record.numconf
            dic["numprob"] += record.numprob
            dic["numdeaths"] += record.numdeaths
            dic["numtotal"] += record.numtotal
            dic["ratetotal"] += record.ratetotal

    df = pd.DataFrame.from_dict(dic, orient='index', columns=['number of people'])
    df.plot.bar(rot=0)
    plt.yscale('log')
    plt.ylabel("Log scale of number of people")
    plt.show()

