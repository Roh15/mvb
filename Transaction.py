from nacl.signing import VerifyKey
from nacl.encoding import HexEncoder
from txGenerator import generate_hash, generateSignature
import json


class Transaction:
    def __init__(self, tx):
        # print("creating tx from " + str(tx))
        self.input = tx['input']
        self.number = tx['number']
        self.output = tx['output']
        self.sig = tx['sig']
        self.tx_fee = 0
        self.validate()

    def netTx(self):
        net = {}
        for i in self.input:
            output = i['output']
            senderPk = output['pubkey']
            sendAmount = output['value']
            if senderPk not in net:
                net[senderPk] = 0
            net[senderPk] -= sendAmount
        for o in self.output:
            receiverPk = o['pubkey']
            receiveAmount = o['value']
            if receiverPk not in net:
                net[receiverPk] = 0
            net[receiverPk] += receiveAmount
        return net

    def validate(self):
        # if not valid, throw error
        if len(self.input) == 0:
            raise Exception
        elif len(self.output) == 0:
            raise Exception
        elif not self.sig:
            raise Exception
        elif not self.number:
            raise Exception
        hexHash = generate_hash(
            [json.dumps(self.input).encode('utf-8'), json.dumps(self.output).encode('utf-8'), self.sig.encode('utf-8')]
        )
        if self.number != hexHash:
            raise Exception
        totalInOut = 0
        res = self.netTx()
        for val in res.values():
            totalInOut += val

        # changes made in <Task 1>
        # original:
        # if totalInOut != 0:
        #     raise Exception
        if totalInOut > 0: # more received than sent
            raise Exception
        else:
            self.tx_fee = -totalInOut
        # end of changes

        vk = VerifyKey(self.input[0]['output']['pubkey'], encoder=HexEncoder)
        vk.verify(self.sig, encoder=HexEncoder)
