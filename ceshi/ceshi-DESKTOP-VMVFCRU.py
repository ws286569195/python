# -- coding:UTF-8 --<code>
# 查验发票测试1
from suds.client import Client
chayan = Client('http://fpcy.sdaisino.com:8085/CheckCodeService/CXF/GetInvoiceService?wsdl')
print(chayan.service.getInvoice('<?xml version="1.0" encoding="UTF-8"?>\
<CheckData>\
<InvData>\
<TaxCode>91321204063278931X</TaxCode>\
<Password>c4ca4238a0b923820dcc509a6f75849b</Password>\
<InvCode>3100193130</InvCode>\
<InvNo>51792388</InvNo>\
<InvTime>2020-03-04</InvTime>\
<InvOther>1131.59</InvOther>\
</InvData>\
</CheckData>\
'))