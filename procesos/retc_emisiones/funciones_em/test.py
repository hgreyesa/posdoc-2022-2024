#from bson.decimal128 import Decimal128, create_decimal128_context
#import decimal
#
#D128_CTX = create_decimal128_context()
##with decimal.localcontext(D128_CTX):
#d1 = Decimal128('1.23')
#d2 = Decimal128('3.21')
#d3 = Decimal128(d1.to_decimal() + d2.to_decimal())
#print(d3, type(d3))
#print(d3.to_decimal(), type(d3.to_decimal()))
#decimal.Decimal(d3)

import pandas as pd
from numpy.random import randint
df = pd.DataFrame(columns=['cve_ent', 'qty1', 'qty2'])
for i in range(0, 32):
    df.loc[i] = ['name' + str(i+1).zfill(2)] + list(randint(10, size=2))
print(df)
