from ncclient import manager

router = {
    'host': '192.168.56.101',  # IP de tu router CSR1000v
    'port': 830,
    'username': 'admin',
    'password': 'admin',
    'hostkey_verify': False,
}

with manager.connect(**router) as m:
    print("Conexión establecida con NETCONF.")
    print(m.server_capabilities)
