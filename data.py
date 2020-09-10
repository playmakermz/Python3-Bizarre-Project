import json

data_list = {
'name':'budi',
'password':'123',
'tabungan':1234,

        }
data_list = json.dumps(data_list)

data = json.loads(data_list)
