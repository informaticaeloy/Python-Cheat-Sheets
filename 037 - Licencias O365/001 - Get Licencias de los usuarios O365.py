### DESCRIPCIÓN
### *******************************************************************************************************
### Este programa realiza los siguiente:
### 1- Se conecta a O365 y obtiene un listado de los usuarios
### 1.1 - Como solo nos da Microsoft Graph 100 líneas, recorremos el request hasta que no haya más páginas
### 2- Obtiene los tipos de licencia que tiene asociados
### 3- Busca el mail de dicho usuario en el AD local
### 4- Si existe dicho usuario y lo encuentrea por el mail, recoge el campo "Company" (puede salir en tu server cono "organization")
### 5- Crea un array con los datos -> ID de caso, ID de usuario, mail, displayName, Tipo de licencia O365, Tipo de licencia POWER BI, Company
### 6- Lo escribe a un fichero .txt
### *******************************************************************************************************
import json
import sys
import requests
from msal import ConfidentialClientApplication
from ldap3 import Server, Connection, ALL
from ldap3.core.exceptions import LDAPException, LDAPBindError

domainName = 'TU NOMBRE DE DOMINIO'
userName = 'USUARIO CON PERSMISOS'
PASSWORD = 'TU CONTRASEÑA'
unidad_organizativa = 'UNIDAD ORGANIZATIVA DONDE BUSCAR'

global ldap_conn

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def connect_ldap_server():
    print('==>>Entro en conn')
    try:
        server_uri = f"ldap://192.168.176.258" #LA IP DE TU CONTROLADOR DE DOMINIO
        server = Server(server_uri, get_info=ALL)
        connection = Connection(server,
                                user='{0}\\{1}'.format(domainName, userName),
                                password=PASSWORD)
        bind_response = connection.bind()  # Returns True or False
        if bind_response:
            print("CONECTADO !!!!!!!!!!")
    except LDAPBindError as e:
        connection = e
        print("E R R O R         CONECTANDO !!!!!!!!!!")
    return (connection)

def get_ldap_users(mail_a_buscar):
    search_base = 'mail=' + mail_a_buscar + ',OU=' + unidad_organizativa + ',DC=' + domainName + ',DC=loc'
    print("╠" + '>>', end='')
    print(bcolors.OKGREEN + " BUSCANDO ****************** => " + search_base + bcolors.ENDC)
    result = ldap_conn.search('DC=NOMBRE_DE_TU_DOMINIO,DC=loc',
                              f'(mail={mail_a_buscar})',
                              attributes=['displayName', 'mail', 'company'])
    if len(ldap_conn.entries) > 0:
        print("╠", end='')
        print(">> ENCONTRADA COMPANY => ", end='')
        print(ldap_conn.entries[0].company.value, end=' <=>')
        print(ldap_conn.entries[0].company)
        return ldap_conn.entries[0].company.value
    else:
        print("╠", end='')
        print(">> NO ENCONTRADA COMPANY")
        return None

print('******************************************************* INICIO ***********')
print('||^^ Llamo a Connect LDAP')

ldap_conn = connect_ldap_server()

client_id = "EL_CLIENTE_ID_DE_TU_TENANT_DE_AZURE"
client_secret = "EL_SECRETO_DE_TU_TENANT_DE_AZURE"
tenant_id = "EL_ID_DE_TU_TENANT_DE_AZURE"

msal_authority = f"https://login.microsoftonline.com/{tenant_id}"
msal_scope = ["https://graph.microsoft.com/.default"]
msal_app = ConfidentialClientApplication(
    client_id=client_id,
    client_credential=client_secret,
    authority=msal_authority,
)

result = msal_app.acquire_token_silent(
    scopes=msal_scope,
    account=None,
)

if not result:
    result = msal_app.acquire_token_for_client(scopes=msal_scope)

if "access_token" in result:
    access_token = result["access_token"]
else:
    raise Exception("No Access Token found")

headers = {
    "Authorization": f"Bearer {access_token}",
    "Content-Type": "application/json",
}

response = requests.get(
    # url="https://graph.microsoft.com/v1.0/auditLogs/signIns", #Get Logs. Need P1 or P2 license
    url="https://graph.microsoft.com/v1.0/users?$select=displayName,id,mail&$top=100",
    # Get Users from Azure Active Directory
    headers=headers,
)

list_of_users = json.loads(json.dumps(response.json()))
print(type(list_of_users))

print(list_of_users[u'value'])
print(list_of_users['@odata.nextLink'])

final_array = []

contador_de_usuarios_O365 = 0
USUARIOS_CON_ERROR = 0
OFFICE_E1 = 0
EXCHANGE_ONLINE_P1 = 0
EXCHANGE_ONLINE_P2 = 0
OFFICE_E3 = 0
OFFICE_F3 = 0
while True:

    for cada_usuario in list_of_users[u'value']:
        array_temp = ['', '', '', '', '', '', '']
        response_license = requests.get(
            # url="https://graph.microsoft.com/v1.0/auditLogs/signIns", #Get Logs. Need P1 or P2 license
            url="https://graph.microsoft.com/v1.0/users/" + cada_usuario['id'] + "/licenseDetails",
            # Get Users from Azure Active Directory
            headers=headers,
        )
        contador_de_usuarios_O365 += 1
        print("╔" + '>>', end='')
        if (cada_usuario['id'] == None):
            print(bcolors.FAIL + " ERROR EN LA OBTENCIÓN DEL ID" + bcolors.ENDC)
            USUARIOS_CON_ERROR += 1
        elif (cada_usuario['mail'] == None):
            print(bcolors.FAIL + " ERROR EN LA OBTENCIÓN DEL MAIL" + bcolors.ENDC)
            USUARIOS_CON_ERROR += 1
        elif (cada_usuario['displayName'] == None):
            print(bcolors.FAIL + " ERROR EN LA OBTENCIÓN DEL DISPLAYNAME" + bcolors.ENDC)
            USUARIOS_CON_ERROR += 1
        else:
            print(bcolors.OKBLUE + " #" + str(contador_de_usuarios_O365) + bcolors.ENDC, end="")
            print(bcolors.OKGREEN + " ID:" + bcolors.ENDC + cada_usuario['id'] + bcolors.ENDC, end="")
            print(bcolors.OKGREEN + " Mail:" + bcolors.ENDC + cada_usuario['mail'] + bcolors.ENDC, end="")
            print(bcolors.OKGREEN + " Nombre:" + bcolors.ENDC + cada_usuario['displayName'] + bcolors.ENDC, end="")
            array_temp[0] = contador_de_usuarios_O365
            array_temp[1] = cada_usuario['id']
            array_temp[2] = cada_usuario['mail']
            array_temp[3] = cada_usuario['displayName']
        list_of_licenses = json.loads(json.dumps(response_license.json()))

        array_temp[4] = "SIN LICENCIA DE OFFICE/EXCHANGE"
        array_temp[5] = "SIN LICENCIA DE POWER BI"
        for cada_licencia in list_of_licenses[u'value']:
            if cada_licencia[u'skuId'] == "18181a46-0d4e-45cd-891e-60aabd171b4e":
                print(bcolors.OKCYAN + " Licencia encontrada =>>" + cada_licencia[u'skuId'] + bcolors.ENDC, end=" -> ")
                print("OFFICE 365 E1")
                OFFICE_E1 += 1
                array_temp[4] = "OFFICE 365 E1"
            elif cada_licencia[u'skuId'] == "4b9405b0-7788-4568-add1-99614e613b69":
                print(bcolors.OKCYAN + " Licencia encontrada =>>" + cada_licencia[u'skuId'] + bcolors.ENDC, end=" -> ")
                print("EXCHANGE ONLINE PLAN 1")
                EXCHANGE_ONLINE_P1 += 1
                array_temp[4] = "EXCHANGE_ONLINE_PLAN_1"
            elif cada_licencia[u'skuId'] == "19ec0d23-8335-4cbd-94ac-6050e30712fa":
                print(bcolors.OKCYAN + " Licencia encontrada =>>" + bcolors.OKCYAN + cada_licencia[u'skuId'] + bcolors.ENDC, end=" -> ")
                print("EXCHANGE ONLINE PLAN 2")
                EXCHANGE_ONLINE_P2 += 1
                array_temp[4] = "EXCHANGE_ONLINE_PLAN_2"
            elif cada_licencia[u'skuId'] == "6fd2c87f-b296-42f0-b197-1e91e994b900":
                print(bcolors.OKCYAN + " Licencia encontrada =>>" + bcolors.OKCYAN + cada_licencia[u'skuId'] + bcolors.ENDC, end=" -> ")
                print("OFFICE 365 E3")
                OFFICE_E3 += 1
                array_temp[4] = "OFFICE 365 E3"
            elif cada_licencia[u'skuId'] == "4b585984-651b-448a-9e53-3b10f069cf7f":
                print(bcolors.OKCYAN + " Licencia encontrada =>>" + bcolors.OKCYAN + cada_licencia[u'skuId'] + bcolors.ENDC, end=" -> ")
                print("OFFICE 365 F3")
                OFFICE_F3 += 1
                array_temp[4] = "OFFICE 365 F3"

            if cada_licencia[u'skuId'] == 'f8a1db68-be16-40ed-86d5-cb42ce701560':
                array_temp[5] = "POWER BI PRO"
            elif cada_licencia[u'skuId'] == 'c1d032e0-5619-4761-9b5c-75b6831e1711':
                array_temp[5] = "POWER BI PREMIUM"

        print("╠" + '>>', end='')
        print(' Llamo a la búsqueda')
        if cada_usuario['mail'] is None:
            company_del_usuario = 'SIN COMPANY'
        else:
            company_del_usuario = get_ldap_users(cada_usuario['mail'])
        array_temp[6] = company_del_usuario
        final_array.append(array_temp)
        print('╚', end='')
        print(">> Datos recopilados :" , end=' ')
        print(bcolors.WARNING, end='')
        print(array_temp[0], end=' ')
        print(array_temp[1], end=' ')
        print(array_temp[2], end=' ')
        print(array_temp[3], end=' ')
        print(array_temp[4], end=' ')
        print(array_temp[5], end=' ')
        print(array_temp[6], end=' ')
        print(bcolors.ENDC)
    if not ('@odata.nextLink' in list_of_users):
        break

    response = requests.get(
        # url="https://graph.microsoft.com/v1.0/auditLogs/signIns", #Get Logs. Need P1 or P2 license
        url=list_of_users['@odata.nextLink'],
        # Get Users from Azure Active Directory
        headers=headers,
    )
    list_of_users = json.loads(json.dumps(response.json()))
    if ('@odata.nextLink' in list_of_users):
        print(list_of_users['@odata.nextLink'])

print("OFFICE_E1 -> " + str(OFFICE_E1))
print("EXCHANGE_ONLINE_P1 -> " + str(EXCHANGE_ONLINE_P1))
print("EXCHANGE_ONLINE_P2 -> " + str(EXCHANGE_ONLINE_P2))
print("OFFICE_E3 -> " + str(OFFICE_E3))
print("OFFICE_F3 -> " + str(OFFICE_F3))
print("USUARIOS_CON_ERROR -> " + str(USUARIOS_CON_ERROR))

original_stdout = sys.stdout

with open('filename.txt', 'w') as f:
    sys.stdout = f  # Change the standard output to the file we created.
    for cada_dato in final_array:
        print(cada_dato)
    sys.stdout = original_stdout  # Reset the standard output to its original value

print("END!!!")
