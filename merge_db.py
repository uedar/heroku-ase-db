import os
from ase.db import connect

paths = [
    os.path.join(root, file)
    for root, dirs, files in os.walk("./data/contribute")
    for file in files
]

# remove db
if os.path.isfile("./data/main.json") == True:
    os.remove("./data/main.json")


print(paths)
db_main = connect("./data/main.json")
for arg in paths:
    db_to_append = connect(arg)
    for row in db_to_append.select():
        key_value_pairs = row.key_value_pairs
        key_value_pairs["Functional"] = row.calculator_parameters["input_data"][
            "XCTYPE"
        ]
        db_main.write(
            row.toatoms(add_additional_information=True),
            key_value_pairs=key_value_pairs,
            data=row.calculator_parameters,
        )
