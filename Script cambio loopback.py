from ncclient import manager

router = {
    'host': '192.168.56.101',  # IP de tu router CSR1000v
    'port': 830,
    'username': 'admin',
    'password': 'admin',
    'hostkey_verify': False,
}

loopback_config = """
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

with manager.connect(**router) as m:
    m.edit_config(target='running', config=loopback_config)
    print("Interfaz Loopback 11 configurada con la dirección IP 11.11.11.11/32.")
