from ncclient import manager

router_ip = "192.168.56.119"

with manager.connect(
    host=router_ip,
    port=830,
    username="cisco",
    password="cisco123!",
    hostkey_verify=False
) as m:
    print("Conexión NETCONF exitosa al CSR1000v")
