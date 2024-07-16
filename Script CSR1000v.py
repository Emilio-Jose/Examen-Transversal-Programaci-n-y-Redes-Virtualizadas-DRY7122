from netmiko import ConnectHandler

# Configuración del dispositivo
router = {
    'device_type': 'cisco_ios',
    'host': '192.168.56.103',  
    'username': 'Emilio-Jose',   
    'password': 'Cisco123',      
    'secret': 'Cisco123',        
}

# Conectar al dispositivo
net_connect = ConnectHandler(**router)
net_connect.enable()

# Configurar EIGRP para IPv4 e IPv6
as_number = 100  # Número de sistema autónomo
ipv4_network = '192.168.1.0'
wildcard_mask = '0.0.0.255'
ipv6_network = '2001:db8::/32'
passive_interfaces = ['GigabitEthernet0/1', 'GigabitEthernet0/2']

config_commands = [
    f'router eigrp {as_number}',
    f'network {ipv4_network} {wildcard_mask}',
    f'network {ipv6_network}',
]

# Añadir comandos para interfaces pasivas
for interface in passive_interfaces:
    config_commands.append(f'passive-interface {interface}')

net_connect.send_config_set(config_commands)

# Obtener el `running-config` para EIGRP
running_config_eigrp = net_connect.send_command('show running-config | section eigrp')
print("Running Config - EIGRP:")
print(running_config_eigrp)

# Obtener información de IP y estado de las interfaces
interface_info = net_connect.send_command('show ip interface brief')
print("IP Interface Brief:")
print(interface_info)

# Obtener el `running-config`
running_config = net_connect.send_command('show running-config')
print("Running Config:")
print(running_config)

# Obtener la versión del software
version_info = net_connect.send_command('show version')
print("Version Info:")
print(version_info)

# Cerrar la conexión
net_connect.disconnect()
