#%%
import plotly.express as px

# %%



# %%
fig = px.treemap(
    names = ["Ungulates", "Odd-toed Ungulates", "Even-Toed Ungulates", "Camelids", "Pigs", "Whippos", "Ruminants", "Bovids", '🦏', '🐴🐎', '🦓', '🐖🐷🐽', '🐗', ],
    parents = ["", "Ungulates", "Ungulates", "Even-Toed Ungulates", "Even-Toed Ungulates", "Even-Toed Ungulates", "Even-Toed Ungulates", "Even-Toed Ungulates", 'Odd-toed Ungulates', 'Odd-toed Ungulates', 'Odd-toed Ungulates', 'Pigs', 'Pigs', ]
)
fig.show()
# %%
fig = px.treemap(
    names = ["Ungulates", "Odd-toed Ungulates", "Even-Toed Ungulates", ],
    parents = [" ", "Ungulates", "Ungulates",]
)
fig.show()
# %%
