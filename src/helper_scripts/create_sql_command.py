import os

database_name = "running_gag_database"

create_database = "create database " + database_name + ";"
create_table = "create table Customer(\n\tID UUID primary key not null,\n\tfirstName varchar(50) not null,\n\tlastName varchar(50)\n\t);"
crate = create_database + "\nuse " + database_name + "\n" + create_table

with open(os.path.join("..", "..", "files", "dataset.txt"), "r") as dataset_file:
    dataset = dataset_file.readlines()
    with open(os.path.join("..", "..", "files", "sql_command.txt"), "w") as sql_command_file:
        sql_command_file.write(crate + "\n")
        for date in dataset:
            if date == "":
                continue
            data_split = date.split(",")
            insert = "insert into customer (ID, firstName, lastName) values (\"" + data_split[0] + "\", \"" + data_split[1] + "\", \"" + data_split[2] + "\");"
            sql_command_file.write(insert.replace("\n", "") + "\n")
            