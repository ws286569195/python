# -- coding:UTF-8 --<code>
# 查验发票测试1
from suds.client import Client
chayan = Client('http://fpcy.sdaisino.com:8085/CheckCodeService/CXF/GetInvoiceService?wsdl')
print(chayan.service.getInvoice('<?xml version="1.0" encoding="UTF-8"?>\
<CheckData>\
<InvData>\
<TaxCode>9161000029419556XT</TaxCode>\
<Password>c4ca4238a0b923820dcc509a6f75849b</Password>\
<InvCode>033002000611</InvCode>\
<InvNo>91221903</InvNo>\
<InvTime>2021-01-08</InvTime>\
<InvOther>620192</InvOther>\
</InvData>\
</CheckData>\
'))