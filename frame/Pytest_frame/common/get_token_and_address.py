import requests
import pprint
import json

def get_address():
    """
    获取POS机的token，并获取帐号的充币地址
    :return:
    """
    url_getAddress = "https://api-test.fiiipos.com/api/Wallet/GetDepositAddress"
    url_getToken = "https://api-test.fiiipos.com/api/Account/Signon"

    POSSNs = [
        {"N3000TEST031":"PT031"},
        {"N3000TEST032": "PT032"}
    ]
    for POSSN in POSSNs:
        for sn, merchantid in POSSN.items():

            headers_token = {'content-type': "application/json"}
            data = {"POSSN": sn,
                    "MerchantId": merchantid,
                    "PIN": "HUFPORxIUjn19Dwry06AAY5cn5Z4ELRoLQg5/43HJgtwbK/ViJy8Qcx5j2eXRZl4"}
            response = requests.post(url_getToken, json=data, headers=headers_token)
            result_token = response.json()['Data']['AccessToken'] # 获取帐号登录token
            pprint.pprint("POS机SN码{0}，帐号{1}的充币地址为：".format(sn, merchantid))

            cryptoIds = [2, 3, 5, 6, 20, 22, 24, 25, 26, 28, 30, 31]
            for cryptoid in cryptoIds:
                id = cryptoid
                querystring_getAddress = {"cryptoId":id}
                headers_address = {
                    'content-type': "application/json",
                    'authorization': "bearer " + result_token
                    }
                response_address = requests.get(url_getAddress, headers=headers_address, params=querystring_getAddress)
                result = response_address.json()
                address = result['Data']['Address'] # 获取帐号的充币地址
                pprint.pprint("{0}地址为：{1}".format(id, address))


if __name__=='__main__':
    
    get_address()
