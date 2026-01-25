from ncclient import manager

router_ip = "192.168.56.119"

config = """
<config>
 <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
  <hostname>Marin-Pizarro-Aguirre</hostname>
 </native>
</config>
"""

with manager.connect(
    host=router_ip,
    port=830,
    username="cisco",
    password="cisco123!",
    hostkey_verify=False
) as m:
    m.edit_config(target="running", config=config)
    print("Hostname cambiado correctamente")
