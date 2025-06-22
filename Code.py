import socket

# Get URL input from the user
url = input("Enter the URL (e.g., www.google.com): ")

try:
    # Resolve the IP address
    ip_address = socket.gethostbyname(url)
    print(f"IP address of {url} is: {ip_address}")
except socket.gaierror:
    print("Invalid URL or unable to resolve IP address.")
