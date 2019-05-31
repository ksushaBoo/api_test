import configparser
import random
import string
import requests
import xml.dom.minidom
from requests import Response


def randomOrderId(count):
    orderId = ''
    if count == 0:
        rang = random.randint(10, 50)
        orderId += ''.join(random.choice(string.ascii_lowercase + string.digits) for _ in range(rang))
    else:
        try:
            rang = count
            orderId += ''.join(random.choice(string.ascii_lowercase + string.digits) for _ in range(rang))
        except TypeError:
            orderId = count

    return orderId


class Api:
    parser = configparser.ConfigParser()
    parser.read('test_params.ini')

    BASE_URL = parser.get('base', 'url_block')

    @staticmethod
    def requestBlock(task, differentOrderId=False, charOrder=0, CustomFields=False):
        url = Api.BASE_URL
        orderIdOperation = randomOrderId(count=charOrder)

        Key = Api.parser.get(task, 'Key')
        OrderId = orderIdOperation
        Amount = Api.parser.get(task, 'Amount')
        buyPAN = Api.parser.get(task, 'Pay_PAN')
        buyAmount = Api.parser.get(task, 'Pay_Amount')
        buyEMonth = Api.parser.get(task, 'Pay_EMonth')
        buyEYear = Api.parser.get(task, 'Pay_EYear')
        buyCardHolder = Api.parser.get(task, 'Pay_CardHolder')
        buySecureCode = Api.parser.get(task, 'Pay_SecureCode')

        if differentOrderId is False:
            buyOrderId = OrderId
        else:
            buyOrderId = randomOrderId(count=charOrder)

        user_pay_data = f"PAN={buyPAN};" \
            f"EMonth={buyEMonth};" \
            f"EYear={buyEYear};" \
            f"CardHolder={buyCardHolder};" \
            f"SecureCode={buySecureCode};" \
            f"OrderId={buyOrderId};" \
            f"Amount={buyAmount};"

        params = {
            'Key': Key,
            'Amount': Amount,
            'OrderId': OrderId,
            'PayInfo': user_pay_data,
        }

        if CustomFields:
            cusFieldFull = ''
            try:
                ip = Api.parser.get(task, 'IP')
                cusFieldFull += f"IP={ip};"
            except configparser.NoOptionError:
                pass
            try:
                description = Api.parser.get(task, 'Description')
                cusFieldFull += f"Description={description};"
            except configparser.NoOptionError:
                pass
            params['CustomFields'] = cusFieldFull

        try:
            paytureId = Api.parser.get(task, 'PaytureId')
            params['PaytureId'] = paytureId
        except configparser.NoOptionError:
            pass

        try:
            customerKey = Api.parser.get(task, 'CustomerKey')
            params['CustomerKey'] = customerKey
        except configparser.NoOptionError:
            pass

        try:
            cheque = Api.parser.get(task, 'Cheque')
            params['Cheque'] = cheque
        except configparser.NoOptionError:
            pass

        result: Response = requests.get(url, params=params)

#        with open('resp.txt', 'a') as f:
#            f.write(f"===>{task}\n{result.text}\n{params}\n")

        dom = xml.dom.minidom.parseString(result.text)
        dom.normalize()
        Block = dom.getElementsByTagName('Block')[0]
        success = Block.getAttribute('Success')
        acceptResult = success

        if success == 'False':
            acceptResult = Block.getAttribute('ErrCode')

        return acceptResult
