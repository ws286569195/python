# -- coding:UTF-8 --<code>
# 查验发票测试
from suds.client import Client
chayan = Client('http://fpcy.sdaisino.com:8085/CheckCodeService/CXF/GetInvoiceService?wsdl')
print(chayan.service.getInvoice('<?xml version="1.0" encoding="UTF-8"?>\
<CheckData>\
<InvData>\
<TaxCode>91110000700215459N</TaxCode>\
<Password>c4ca4238a0b923820dcc509a6f75849b</Password>\
<InvCode>011002000311</InvCode>\
<InvNo>37141233</InvNo>\
<InvTime>2020-08-04</InvTime>\
<InvOther>491104</InvOther>\
</InvData>\
</CheckData>\
'))