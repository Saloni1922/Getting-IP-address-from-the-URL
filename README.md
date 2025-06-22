# To get the IP address from a URL, you're essentially resolving the domain name in the URL (like www.google.com) to its corresponding IP address using DNS (Domain Name System). 

The script prompts the user for a URL.

It uses Python’s built-in socket module to perform DNS resolution.

If the domain is invalid or unreachable, it catches the error and shows a message.

# Explaination for thr code 
1. import socket
This imports Python’s socket module.

The socket module provides low-level networking functions.

We'll use it to convert the domain name (URL) into its IP address.

2. url = input("Enter the URL (e.g., www.google.com): ")
This line prompts the user to enter a URL (e.g., www.google.com).

The input is stored in the variable url as a string.

Note: We expect just the domain name or subdomain, not the full URL with http://.

3. try:
This begins a try-except block, which is used to catch errors (e.g., if the user types an invalid domain).

4. ip_address = socket.gethostbyname(url)
This line does the main job:

socket.gethostbyname() converts the given domain name to its IPv4 address.

For example, socket.gethostbyname('www.google.com') might return 142.250.182.100.

5. print(f"IP address of {url} is: {ip_address}")
If the domain is successfully resolved, it prints the IP address in a formatted message.

6. except socket.gaierror:
This catches an error if the domain name is invalid or there’s no network connection.

gaierror stands for get address info error—a common DNS lookup failure.

7. print("Invalid URL or unable to resolve IP address.")
This message is printed only when the program cannot resolve the domain to an IP address.

