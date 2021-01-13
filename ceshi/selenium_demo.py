from selenium import webdriver



option=webdriver.IeOptions()
option.add_argument('disable-infobars')
browser = webdriver.Ie(executable_path="./drivers/IEDriverServer.exe", ie_options=option)
# browser = webdriver.Chrome(executable_path="./drivers/chromedriver.exe")

req_url = "https://www.baidu.com"

# 开始请求
browser.get(req_url)
#打印页面源代码
print(browser.page_source)
#关闭浏览器
browser.close()
#关闭chreomedriver进程
browser.quit()


