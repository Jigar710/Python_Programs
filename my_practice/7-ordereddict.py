from collections import OrderedDict

d = OrderedDict()
d['a'] = 1
d['b'] = 5
d['d'] = 4
d['c'] = 6

print(d)
print(OrderedDict.__doc__)

import json
print(json.dumps(d))