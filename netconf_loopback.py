from ncclient import manager

router_ip = "192.168.56.119"

config = """
<config>
 <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
  <interface>
   <Loopback>
    <name>11</name>
    <ip>
     <address>
      <primary>
       <address>11.11.11.11</address>
       <mask>255.255.255.255</mask>
      </primary>
     </address>
    </ip>
   </Loopback>
  </interface>
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
    print("Loopback 11 creada correctamente")
