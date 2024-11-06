import csv
import subprocess
import dns.resolver
from datetime import datetime
import time

# Resolver DNS personalizado para usar 8.8.8.8 como servidor DNS
custom_resolver = dns.resolver.Resolver()
custom_resolver.nameservers = ['8.8.8.8']


# Funciones auxiliares para obtener datos DNS con reintentos
def get_ip(domain, retries=3):
    for attempt in range(retries):
        try:
            ip_address = custom_resolver.resolve(domain, 'A')
            return ["'" + ip.to_text() for ip in ip_address]  # Agregar ' al inicio de la IP
        except Exception as e:
            print(f"Intento {attempt + 1}: Error obteniendo IP para {domain}: {e}")
            time.sleep(1)
    return []


def get_ns_records(domain, retries=3):
    for attempt in range(retries):
        try:
            ns_records = custom_resolver.resolve(domain, 'NS')
            return [ns.to_text() for ns in ns_records]
        except Exception as e:
            print(f"Intento {attempt + 1}: Error obteniendo registros NS para {domain}: {e}")
            time.sleep(1)
    return []


def get_mx_records(domain, retries=3):
    for attempt in range(retries):
        try:
            mx_records = custom_resolver.resolve(domain, 'MX')
            return [(mx.preference, mx.exchange.to_text()) for mx in mx_records]
        except Exception as e:
            print(f"Intento {attempt + 1}: Error obteniendo registros MX para {domain}: {e}")
            time.sleep(1)
    return []


# Función para obtener datos WHOIS usando el comando de sistema 'whois'
def get_whois_data(domain):
    try:
        result = subprocess.run(['.\\.\whois', domain], capture_output=True, text=True, encoding="utf-8")
        output = result.stdout

        if "No match" in output or "not found" in output:
            print(f"Dominio {domain} no registrado según WHOIS.")
            return None

        # Procesar la salida WHOIS para extraer fechas
        data = {}
        for line in output.splitlines():
            if "Creation Date" in line:
                data['creation_date'] = line.split(":")[1].strip()
            elif "Expiration Date" in line:
                data['expiration_date'] = line.split(":")[1].strip()
            elif "Updated Date" in line:
                data['last_updated'] = line.split(":")[1].strip()

        # Si faltan fechas, coloca 'N/A'
        data['creation_date'] = data.get('creation_date', "N/A")
        data['expiration_date'] = data.get('expiration_date', "N/A")
        data['last_updated'] = data.get('last_updated', "N/A")

        return data
    except Exception as e:
        print(f"Error obteniendo WHOIS para {domain}: {e}")
        return None


# Función principal para procesar cada dominio
def process_domain(domain):
    whois_data = get_whois_data(domain)

    if whois_data is None:
        return {"domain": domain, "status": "No registrado", "ip": "", "creation_date": "N/A", "expiration_date": "N/A", "last_updated": "N/A"}

    # Obtener registros NS y MX
    ns_records = get_ns_records(domain)
    mx_records = get_mx_records(domain)

    # Construir el diccionario con la información del dominio
    domain_info = {
        "domain": domain,
        "status": "Registrado",
        "ip": ', '.join(get_ip(domain)),
        "creation_date": whois_data.get('creation_date', 'N/A'),
        "expiration_date": whois_data.get('expiration_date', 'N/A'),
        "last_updated": whois_data.get('last_updated', 'N/A'),
        "ns_records": ns_records,
        "mx_records": mx_records
    }
    return domain_info


# Leer dominios de un archivo de texto
input_file = 'dominios.txt'  # Cambia esto a tu archivo de entrada
timestamp = datetime.now().strftime("%Y_%m_%d_%H%M%S")
output_file = f'dominios_whois_{timestamp}.csv'

# Lista para almacenar los datos procesados
data = []

# Procesar cada dominio
with open(input_file, 'r', encoding='utf-8') as file:
    for line in file:
        domain = line.strip()
        if domain:
            domain_info = process_domain(domain)
            if domain_info:
                data.append(domain_info)

# Verificar si hay dominios registrados en los datos antes de calcular el máximo
if any(d["status"] == "Registrado" for d in data):
    max_ns_records = max((len(d.get('ns_records', [])) for d in data if d["status"] == "Registrado"), default=0)
    max_mx_records = max((len(d.get('mx_records', [])) for d in data if d["status"] == "Registrado"), default=0)
else:
    max_ns_records = 0
    max_mx_records = 0

# Crear nombres de columna para registros NS y MX en el formato requerido
fieldnames = ["domain", "status", "ip", "creation_date", "expiration_date", "last_updated"]
fieldnames += [f"NS_Record_{i+1}" for i in range(max_ns_records)]
for i in range(max_mx_records):
    fieldnames += [f"priority_{i+1}", f"mx_{i+1}"]

# Escribir los datos en el archivo CSV
with open(output_file, 'w', newline='') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()

    for entry in data:
        # Rellena los datos comunes
        row = {
            "domain": entry["domain"],
            "status": entry["status"],
            "ip": entry.get("ip", ""),
            "creation_date": entry.get("creation_date", ""),
            "expiration_date": entry.get("expiration_date", ""),
            "last_updated": entry.get("last_updated", "")
        }

        # Añadir los registros NS en columnas separadas
        if entry["status"] == "Registrado":
            for i, ns in enumerate(entry["ns_records"]):
                row[f"NS_Record_{i + 1}"] = ns

            # Añadir los registros MX y sus prioridades en columnas alternadas
            for i, (priority, mx) in enumerate(entry["mx_records"]):
                row[f"priority_{i + 1}"] = priority
                row[f"mx_{i + 1}"] = mx

        # Escribir la fila completa en el CSV
        writer.writerow(row)
