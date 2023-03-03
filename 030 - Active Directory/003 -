from ldap3 import Server, Connection, ALL
from ldap3.core.exceptions import LDAPException, LDAPBindError

from tabulate import tabulate

domainName = 'MI_DOMINIO'
userName = 'NOMBRE_USUARIO'
unidad_organizativa = 'MI_UNIDAD_ORGANIZATIVA'
PASSWORD = 'MI_PASSWORD'

def connect_ldap_server():

    print('==>>Entro en conn')
    try:
        
        server_uri = f"ldap://192.168.170.171"
        
        server = Server(server_uri, get_info=ALL)

        connection = Connection(server,          
                                user='{0}\\{1}'.format(domainName, userName), 
                                password=PASSWORD)

        bind_response = connection.bind() # Returns True or False
    except LDAPBindError as e:
        connection = e

    return (connection)


def get_ldap_users():
    print('==>> Entro en búsqueda')
    # Provide a search base to search for.
    search_base = 'OU=' + unidad_organizativa + ',DC=' + domainName + ',DC=loc'
    
    # Establish connection to the server
    ldap_conn = connect_ldap_server()
    try:
        # only the attributes specified will be returned
        ldap_conn.search(search_base, '(sAMAccountType=805306368)', attributes=['displayName', 'mail', 'company'])
    
        results = ldap_conn.entries
    except LDAPException as e:
        results = e

    print('LISTADO DE USUARIOS DE LA UO ' + unidad_organizativa)
    print('***************************************************')
    
    lista_usuarios = []
    for i in range(len(ldap_conn.entries)):
        lista_usuarios.append([ldap_conn.entries[i].DisplayName, ldap_conn.entries[i].mail,ldap_conn.entries[i].company])
    
    print(tabulate(lista_usuarios, headers = ["DISPLAY NAME", "MAIL","COMPANY"], tablefmt = 'rounded_outline'))  


print('******************************************************* FIN ***********')
print('||^^ Llamo a Connect LDAP')
connect_ldap_server()
print('||^^ Llamo a la búsqueda')
get_ldap_users()
