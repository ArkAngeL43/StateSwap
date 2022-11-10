import os
country_a=input(str("1st Country tag >>> "))
print("..........")
country_b=input(str("2nd Country tag >>> "))
print("..........")
###Steam is properly installed###
try:
    with open("C:\\Program Files (x86)\\Steam\\steamapps\\common\\Hearts of Iron IV\\history\\states\\1-France.txt","r") as F:
        filedir="C:\\Program Files (x86)\\Steam\\steamapps\\common\\Hearts of Iron IV\\history\\states"
        print(f"Default file path found in {filedir}")
###if Steam is not installed properly the chunk below will search for the state files in the C drive###
except Exception:
    print("Could not find default HOI4 path, searching C: for HOI4 path....")
    for root,directory,files in os.walk("C:\\"):
        if "1-France.txt" in files:
            with open(f"{os.path.join(root,'1-France.txt')}","r") as F:
                filedir=root
            break
    print(f"Found HOI4 path in {filedir}")
if os.path.exists(os.getcwd()+"\\OUT") == 0:
    os.mkdir(os.getcwd()+"\\OUT")#creates the out file if not present
for x,y,z in os.walk(filedir):#iterate over the file path
    print("Swapping state files...")
    for n in z:#iterate over files in path
        with open(os.path.join(filedir,n),"r") as F:
            filedat=F.read()#load the file data
            if str(f"owner = {country_a}") in filedat:
                filedat=filedat.replace(f"owner = {country_a}",f"owner = {country_b}")#swaps owner tags
                filedat=filedat.replace(f"add_core_of = {country_a}",f"add_core_of = {country_b}")#swap core tags
                with open(os.path.join(os.getcwd()+"\\OUT",n),"w+") as F:
                    F.write(filedat)#writes to the out folder in the current directory
            elif str(f"owner = {country_b}") in filedat:
                filedat=filedat.replace(f"owner = {country_b}",f"owner = {country_a}")
                filedat=filedat.replace(f"add_core_of = {country_b}",f"add_core_of = {country_a}")
                with open(os.path.join(os.getcwd()+"\\OUT",n),"w+") as F:
                    F.write(filedat)
    print("Done!")