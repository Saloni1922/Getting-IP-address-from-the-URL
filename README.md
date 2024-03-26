import socket
def scan_host(host, port):
  try:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1) # Set a timeout value for the connection attempt
    result = sock.connect_ex((host, port))
    if result == 0:
      print(f"Port {port} on {host} is open")
    else:
      print(f"Port {port} on {host} is closed")
    sock.close()
  except socket.error:
    print(f"Could not connect to {host}:{port}")
def scan_network(network_prefix, start_host, end_host, port):
  for host in range(start_host, end_host + 1):
    ip_address = f"{network_prefix}.{host}"
    scan_host(ip_address, port)
# Example usage
network_prefix = "192.168.1" # Replace with your network prefix
start_host = 1 # Start host number
end_host = 10 # End host number
port = 80 # Port number to scan
scan_network(network_prefix, start_host, end_host, port)
