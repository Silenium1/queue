from datetime import datetime
from collections import OrderedDict
data = { "01-01-2015" : "some data","05-05-2015" : "some data", "03-04-2015" : "some data" }

ordered_data = OrderedDict(sorted(data.items(), key = lambda x:datetime.strptime(x[0], '%d-%m-%Y')))
print(ordered_data)