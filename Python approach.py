#!/usr/bin/env python
# coding: utf-8

# // LoggingService.proto
# 
# syntax = "proto3";
# 
# package logging;
# 
# // The logging service definition.
# service LoggingService {
#   // Sends a log message to be stored by the logging server.
#   rpc SendLog (LogRequest) returns (LogResponse) {}
# }
# 
# // The request message containing the log information.
# message LogRequest {
#   string service_name = 1;
#   string log_level = 2;
#   string message = 3;
#   string timestamp = 4;
# }
# 
# // The response message containing the result of the log operation.
# message LogResponse {
#   bool success = 1;
# }
# 

# In[ ]:


from rpc_library import RpcClient
from LoggingService_pb2 import LogRequest

def send_log(service_name, log_level, message, timestamp):
    client = RpcClient(server_address="logging.server.address", service="LoggingService")
    log_request = LogRequest(service_name=service_name, log_level=log_level, message=message, timestamp=timestamp)
    response = client.SendLog(log_request)
    if response.success:
        print("Log message sent successfully.")
    else:
        print("Failed to send log message.")

# Example usage
send_log("OrderService", "INFO", "Order processed successfully.", "2024-02-15T12:34:56Z")


# In[ ]:


from rpc_library import RpcServer
from LoggingService_pb2 import LogResponse

class LoggingService:
    def SendLog(self, request):
        # Logic to store the log message
        print(f"Received log from {request.service_name}: {request.message}")
        # For demonstration, we'll just print the message and assume storage was successful
        return LogResponse(success=True)

server = RpcServer(service=LoggingService(), address="logging.server.address")
server.start()


# In[ ]:


from xmlrpc.server import SimpleXMLRPCServer

class CalculatorService:
    def add(self, x, y):
        return x + y

    def subtract(self, x, y):
        return x - y

    def multiply(self, x, y):
        return x * y

    def divide(self, x, y):
        if y == 0:
            return "Error: Division by zero"
        return x / y

# Create server
server = SimpleXMLRPCServer(("localhost", 8000))
print("Listening on port 8000...")

# Register CalculatorService with the server
server.register_instance(CalculatorService())

# Run the server's main loop
server.serve_forever()


# In[ ]:


import xmlrpc.client

# Connect to the server
s = xmlrpc.client.ServerProxy('http://localhost:8000')

# Perform remote procedure calls
print("3 + 5 =", s.add(3, 5))
print("10 - 2 =", s.subtract(10, 2))
print("7 * 3 =", s.multiply(7, 3))
print("10 / 2 =", s.divide(10, 2))

# Attempt to divide by zero
print("10 / 0 =", s.divide(10, 0))


# 

# In[ ]:





# 

# In[ ]:





# 

# In[ ]:





# 

# In[ ]:





# 

# In[ ]:





# 

# In[ ]:





# In[7]:




