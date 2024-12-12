# Example of an XML rpc client communicating with the server. 
import xmlrpc.client

# Connect to the server
server = xmlrpc.client.ServerProxy("http://localhost:8000/")

# Call remote functions
print("Addition (5 + 3):", server.add(5, 3))
print("Subtraction (10 - 7):", server.subtract(10, 7))
print("Multiplication (4 * 6):", server.multiply(4, 6))
