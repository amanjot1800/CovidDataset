"""
Author: Amanjot Singh
Student number: 040956152

This is the view of the program. It manages all the user input and output. It starts the program and also ends it.
This class holds all the functions that correspond to various CRUD operations.

"""
# imports the controller file to use its methods
import controller as con


def inn():
    """
    This function is called by various other methods to take repeated user input.
    :return: the input entered by the user
    """
    return input('\033[33m' + "Record Editor> Enter new value: " + '\033[0m')


def update():
    """
    this function do the work of giving and taking all the information to the user. First it asks for the id of object
    to update, and then brings the object and prints it. It then asks the properties to be edited and finally asks for
    the new values. When the user is finished adding information, he must enter 'done' to submit the new data and
    update the object. It uses a while loop to ask for fields again and again until user is done editing.
    :return: this method returns nothing
    """
    print('\033[33m' + "Record editor> Enter the id of record to update:  " + '\033[0m')
    idd = input("\033[33m> \033[0m")
    rec = con.get_record(int(idd))
    if rec is None:
        print("\033[33mNo record found with Id " + idd + ". try again. \033[0m")
    else:
        print("\033[33m" + str(rec) + "\033[0m")
        while rec is not None:
            print("\033[33mEnter 'done' when done editing. Enter the field you want to edit: \033[0m")
            field = input('\033[33m' + "Record Editor> " + '\033[0m')

            if field == 'pruid':
                rec.pruid = inn()
            elif field == 'prname':
                rec.prname = inn()
            elif field == 'prnameFR':
                rec.prnameFR = inn()
            elif field == 'date':
                rec.date = inn()
            elif field == 'numconf':
                rec.numconf = inn()
            elif field == 'numprob':
                rec.numprob = inn()
            elif field == 'numdeaths':
                rec.numdeaths = inn()
            elif field == 'numtotal':
                rec.numtotal = inn()
            elif field == 'numtoday':
                rec.numtoday = inn()
            elif field == 'ratetotal':
                rec.ratetotal = inn()
            elif field == 'done':
                break
            else:
                print("\033[1;31m" + "Invalid field name" + "\033[0m")
        con.update_record(int(idd), rec)
        print("\033[1;32m" + "Record updated." + "\033[0m")


def create():
    """
    This function helps in creating a new record in memory. It asks for various fields of the object and creates a
    list. It then passes that list to create_record function in controller to create and submit the object in
    master_list list of all the objects.
    :return: this function returns nothing
    """
    print("\033[33m" + "Create a new record" + "\033[0m")
    lst = [input("\033[33m" + "pruid: " + "\033[0m"),
           input("\033[33m" + "prname: " + "\033[0m"),
           input("\033[33m" + "prnameFR: " + "\033[0m"),
           input("\033[33m" + "date: " + "\033[0m"),
           input("\033[33m" + "numconf: " + "\033[0m"),
           input("\033[33m" + "numprob: " + "\033[0m"),
           input("\033[33m" + "numdeaths: " + "\033[0m"),
           input("\033[33m" + "numtotal: " + "\033[0m"),
           input("\033[33m" + "numtoday: " + "\033[0m"),
           input("\033[33m" + "ratetotal: " + "\033[0m")]

    msg = con.create_record(lst)
    print("\033[1;32m \n" + msg + "\033[0m")


def get_by():
    """
    this function is used when user just wants to see an object with a specific id. It takes the id and sends it to
    get_record function in controller which sends a Record object. This function then prints the record object.
    :return: it returns nothing.
    """
    idd = int(input("Enter id to get record: "))
    rec = con.get_record(idd)
    if rec is None:
        print("\033[1;31m" + "Record not found" + "\033[0m")
    else:
        print(rec)


def reload():
    """
    This method is used to erase all data in memory and reload the fresh data from covid19.csv dataset.
    It calls the populate_db functions, which clears all data in database and adds fresh data form csv file.
    :return: it returns nothing.
    """
    con.populate_db()
    print("\033[1;32m" + "Data reloaded" + "\033[0m")


def main():
    """
    This is the starting point for this filer and also the program. This method calls the start function in controller
    which then loads up everything and create objects. It method also starts the UI layer and shows information on
    the console. it starts a while loop for various options when continues until the user terminates it by entering
    'exit'.
    :return: it returns nothing
    """

    con.fetch_and_populate()

    print("\033[1;34m" + "Welcome to Python Covid-19 dataset program" + "\033[0m")
    print("\033[1;43;30m" + " Program by Amanjot Singh " + "\033[0m")
    print("Enter 'show', 'reload', 'get by id', 'create', 'update', 'delete', 'save', "
          "'generate plot by province', 'generate plot totals', 'exit'")
    ans = input("> ")

    while ans != 'exit':

        if ans == 'reload':
            reload()

        elif ans == 'show':
            con.print_records()

        elif ans == 'delete':
            print("Enter the id of record you wish to delete: ")
            print('\033[1;31m' + con.delete_record(int(input("> "))) + '\033[0m')

        elif ans == 'update':
            update()

        elif ans == 'create':
            create()

        elif ans == 'get by id':
            get_by()

        elif ans == 'generate plot by province':
            print("Enter province names separated by comma and space or 'all'")
            pro = input("> ")
            con.generate_bar_plot_by_province(pro.split(", "))

        elif ans == 'generate plot totals':
            con.generate_bar_plot_total()

        else:
            print("\033[1;31m" + "Invalid input" + "\033[0m")

        print("\n\nEnter 'show', 'reload', 'get by id', 'create', 'update', 'delete', 'save',"
              " 'generate plot by province', 'generate plot totals',  'exit'")
        print("\033[1;43;30m" + " Program by Amanjot Singh " + "\033[0m")
        ans = input("> ")


# calls the main() function
if __name__ == '__main__':
    main()
