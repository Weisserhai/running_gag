Helper script documentation for the project "running_gag".

"create_dataset.py":
    Takes UUIDs, first names and last names form "running_gag/files" and creates a dataset for a database in scheme "UUID,firstName,lastName" and saves it to "running_gag/files/dataset.txt".

"create_sql_command.py":
    Takes the data from "running_gag/files/dataset.txt" and crates a sql command to create the database "running_gag_database" and the table "Customer" and inserts them. Execute it in the MariaDB command line.