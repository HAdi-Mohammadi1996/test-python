#%%
import numpy as np
import pandas as pd
import plotly.express as px

x = np.linspace(0, 10, 100)
y = np.sin(x)

df = pd.DataFrame({'x': x, 'y': y})

fig = px.line(df, x='x', y='y')
fig.show()
