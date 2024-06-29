DEFAULT_ASN = 393577
CUSTOMER_BGP_COMMUNITY = '393577:0:15'  # Prefixes learned from directly connected customers
TRANSIT_BGP_COMMUNITY = '393577:0:12'  # Prefixes learned from *paid* transit providers
PEER_BGP_COMMUNITY = '393577:0:13'  # Prefixes learned from bilateral peers and exchanges
BGP_COMMUNITY_MAP = {
      "393577:0:12" : "Transit",
      "393577:0:13" : "IX Peer",
      "393577:0:15" : "Customer",
      "393577:0:16" : "Internal BGP",
      "393577:0:666" : "Blackhole",
      '65535:65535': 'No-Export',
}


