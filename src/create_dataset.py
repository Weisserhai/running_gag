import os

with open(os.path.join("..", "files", "dataset.txt"), "w") as dataset_file:
    with open(os.path.join("..", "files", "first_names.txt"), "r") as first_name_file:
        first_names = first_name_file.readlines()
        with open(os.path.join("..", "files", "last_names.txt"), "r") as last_name_file:
            last_names = last_name_file.readlines()
            with open(os.path.join("..", "files", "uuids.txt"), "r") as uuid_file:
                uuids = uuid_file.readlines()

                for i in range(0, len(first_names)):
                    dataset = (uuids[i] + "," + first_names[i] + "," + last_names[i]).replace("\n", "")
                    dataset_file.write(dataset + "\n")
