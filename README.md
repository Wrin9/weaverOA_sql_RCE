# weaverOA_sql_RCE
## 泛微OA某版本的SQL代码执行漏洞
### 2022.04.20
经过测试，该漏洞属于泛微OA msssql远程代码执行漏洞。
测试如图：
![1650428637(1)](https://user-images.githubusercontent.com/54984589/164150112-b8ef1ee8-ff9a-4509-b75f-c73f199a5be9.png)

POC:
PS:url结尾不能有[/],例如：http://127.0.0.1:8080，不能为http://127.0.0.1:8080/

Url ending cannot have [/], for example, http://127.0.0.1:8080, not for http://127.0.0.1:8080/

pocsuite -r weaverOA_sql_injection_POC_EXP.py -u url --verify

![1648651245(1)](https://user-images.githubusercontent.com/54984589/160861695-53c75697-6b88-41fb-bcc7-c1a49c8e2dec.png)

EXP:pocsuite -r weaverOA_sql_injection_POC_EXP.py -u url --attack --command "[command]"

PS:url结尾不能有[/],例如：http://127.0.0.1:8080，不能为http://127.0.0.1:8080/

Url ending cannot have [/], for example, http://127.0.0.1:8080, not for http://127.0.0.1:8080/

![1648651381(1)](https://user-images.githubusercontent.com/54984589/160862217-45fe5a02-d6ab-4731-adb1-8b20ebcf2130.png)
# 免责声明
## 此工具仅用于学习、研究和自查。不应将其用于非法目的。使用本工具产生的一切风险与我无关！
# Disclaimer
## This tool is for study, research, and self-examination only. It should not be used for illegal purposes. All risks arising from the use of this tool have nothing to do with me!
