#!/usr/bin/env python
# coding: utf-8

# **Service side**

# In[ ]:


from spyne.application import Application
from spyne.decorator import rpc
from spyne.service import ServiceBase
from spyne.model.primitive import Unicode, Double
from spyne.protocol.soap import Soap11
from spyne.server.wsgi import WsgiApplication

class LoanApprovalService(ServiceBase):
    @rpc(Unicode, Double, _returns=Unicode)
    def approve_loan(ctx, customer_id, loan_amount):
        if loan_amount <= 10000:
            return "Approved"
        else:
            return "Denied"

application = Application([LoanApprovalService],
                          tns='com.bank.service',
                          in_protocol=Soap11(validator='lxml'),
                          out_protocol=Soap11())

if __name__ == '__main__':
    from wsgiref.simple_server import make_server
    server = make_server('127.0.0.1', 8000, WsgiApplication(application))
    print("SOAP server starting on http://127.0.0.1:8000")
    server.serve_forever()


# **Client side**

# In[ ]:


from zeep import Client

# 替换成实际运行的SOAP服务WSDL URL
wsdl = 'http://127.0.0.1:8000/?wsdl'
client = Client(wsdl=wsdl)

# 调用服务
response = client.service.approve_loan("123456", 5000)
print(f"Loan Approval Response: {response}")

