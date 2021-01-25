import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt
from io import BytesIO
from PIL import Image

data = pd.Series(np.random.rand(10).cumsum(),index=np.arange(1,100,10))
print(data)

data.plot()

buffer = BytesIO()
plt.savefig(buffer)
print(buffer)
plot_data = buffer.getvalue()
print(type(plot_data))
buffer.seek(0)
im = Image.open(buffer)
im.show()