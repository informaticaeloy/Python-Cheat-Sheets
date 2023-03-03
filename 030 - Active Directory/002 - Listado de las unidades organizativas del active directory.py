from ldap3 import Server, Connection, ALL
from ldap3.core.exceptions import LDAPException, LDAPBindError

from tabulate import tabulate

domainName = 'dominio'
userName = 'usuario_con_privilegios'
unidad_organizativa = 'mi-unidad_organizativa'
PASSWORD = 'password_del_user'


def connect_ldap_server():

    print('==>>Entro en conn')
    try:
        
        # Nombre del equipo AD, o IP. También se puede indicar el puerto
        server_uri = f"ldap://192.168.169.170"
        
        server = Server(server_uri, get_info=ALL)
        
        connection = Connection(server,          
                                user='{0}\\{1}'.format(domainName, userName), 
                                password=PASSWORD)
        
        bind_response = connection.bind() # Returns True or False 
    except LDAPBindError as e:
        connection = e

    return (connection)



def get_ldap_UO():
    print('==>> Entro en búsqueda')
    # Provide a search base to search for.
    search_base = 'OU=' + unidad_organizativa + ',DC=' + domainName + ',DC=loc'
    
    # Establece conexión con el server
    ldap_conn = connect_ldap_server()
    try:
        # sólo devuelve los atributos definidos, en este ejemplo el nombre
        #  (ver más en el editor de atributos de las propiedades de la UO)
        ldap_conn.search(search_base, '(objectClass=organizationalUnit)', attributes=['name'])
        results = ldap_conn.entries
    except LDAPException as e:
        results = e
    
    listado = []
    
    for i in range(len(ldap_conn.entries)):
        listado.append(ldap_conn.entries[i].name)
    # Listamos por pantalla en formato tabla los resultados de la búsqueda
    # Elejimos el formato 'rounded_outline' para la tabla
    print(tabulate(listado, headers = ["NOMBRE UO"], tablefmt = 'rounded_outline'))   

print('||^^ Llamo a Connect LDAP')
connect_ldap_server()
print('||^^ Llamo a la búsqueda')
get_ldap_UO()

print('******************************************************* FIN ***********')
