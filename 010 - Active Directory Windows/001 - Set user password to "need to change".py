##############################################################################################################
### Este programita busca a un usuario en concreto en nuestro AD y comprueba si su contraseña estça caducada. 
### Si está caducada, la lectura nos dará '1601-01-01 00:00:00+00:00'
### Si no está caducada, nos dará la fecha en que caducará
##########
### El programa, si está caducada, la "descaduca, escribiendo un -1 
### El programa, si no está caducada, la "caduca, escribiendo un 0
##############################################################################################################

from ldap3 import Server, Connection, ALL, SUBTREE, MODIFY_REPLACE
from ldap3.core.exceptions import LDAPException, LDAPBindError

from datetime import datetime, timezone
import time

domainName = 'domain'
userName = 'user with privileges'
PASSWORD = 'password user with privileges'

def connect_ldap_server():

    print('==>>Entro en conn')
    try:
        
        # Provide the hostname and port number of the openLDAP      
        server_uri = f"ldap://192.168.169.170"
        
        server = Server(server_uri, get_info=ALL)
        # username and password can be configured during openldap setup
        connection = Connection(server,          
                                user='{0}\\{1}'.format(domainName, userName), 
                                password=PASSWORD)
        #conn = Connection(server, read_only=True, user='{0}\\{1}'.format(domainName, userName), password=password, auto_bind=True)
        bind_response = connection.bind() # Returns True or False 
    except LDAPBindError as e:
        connection = e

    return (connection)


def get_ldap_users():
    print('==>> Entro en búsqueda')
    # Provide a search base to search for.
    search_base = 'CN=nombre del usuario,OU=OU1,OU=OU2,OU=OU3,DC=dominio,DC=loc'
        
    # Establish connection to the server
    ldap_conn = connect_ldap_server()
    try:
        # only the attributes specified will be returned
        ldap_conn.search(search_base, '(objectclass=person)', attributes=['displayName', 'mail', 'userAccountControl','sAMAccountName', 'pwdLastSet'])
        #ldap_conn.search(search_base=search_base, '(objectclass=person)',
        #                 attributes=['cn','sn','pwdLastSet','uidNumber'])
        # search will not return any values.
        # the entries method in connection object returns the results 
        results = ldap_conn.entries
    except LDAPException as e:
        results = e

    mifecha = ldap_conn.entries[0].pwdLastset
    
    print (mifecha)

    ahora_var = time.time() 
 
    # perform the Modify operation
    if(str(ldap_conn.entries[0].pwdLastSet) ==  '1601-01-01 00:00:00+00:00'):
        print('SI caducada')
        ldap_conn.modify('CN=usuario_a_acambiar,OU=OU1, OU=2, OU=3, DC=dominio,DC=loc',
             {'pwdLastSet': [(MODIFY_REPLACE, [-1])]})
        print('Cambiada a NO caducada')
    else:
        print('NO caducada')
        ldap_conn.modify('CN=usuario_a_acambiar,OU=OU1, OU=2, OU=3, DC=dominio,DC=loc',
             {'pwdLastSet': [(MODIFY_REPLACE, [0])]})
        print('Cambiada a SI caducada')

    print(ldap_conn.result)

        
print('||^^ Llamo a Connect LDAP')
print('||^^ Llamo a la búsqueda')
get_ldap_users()

print('FIN:::::::::::')
