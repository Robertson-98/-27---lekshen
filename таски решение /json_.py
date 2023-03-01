##====================1

import json
with open("task1.json") as file:
    python_obj = json.load(file)

with open("task1.py", "w") as f:
    f.write(str(python_obj))

##====================2