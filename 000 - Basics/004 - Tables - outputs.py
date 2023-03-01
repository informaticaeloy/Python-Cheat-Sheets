from tabulate import tabulate

class bcolors:
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    
d = [ ["Mark", 12, 95, "contoso@contoso.com"],
     ["Jay", 11, 88, "johndoe@microsoft.com"],
     ["Jack", 14, 90, "emaillargodepruebas@dominiotambienlargo.com"]]

mis_estilos = ["plain","simple","github","grid","simple_grid","rounded_grid","heavy_grid","mixed_grid","double_grid","fancy_grid","outline","simple_outline","rounded_outline","heavy_outline","mixed_outline","double_outline","fancy_outline","pipe","orgtbl","asciidoc","jira","presto","pretty","psql","rst","mediawiki","moinmoin","youtrack","html","unsafehtml","latex","latex_raw","latex_booktabs","latex_longtable","textile","tsv"]

print("Sin estilo definido => ")
print(tabulate(d, headers=["Name", "Age", "Percent", "e-mail"]))

#print(len(mis_estilos))

for i in range((len(mis_estilos)-1)):
    print(bcolors.FAIL + "Estilo => " + mis_estilos[i] + bcolors.ENDC)
    if (i % 2 == 0):
        print(bcolors.OKBLUE)
    else:
        print(bcolors.OKGREEN)

    print(tabulate(d, headers = ["Name", "Age", "Percent", "e-mail"], tablefmt = mis_estilos[i]))    
    print(bcolors.ENDC)
