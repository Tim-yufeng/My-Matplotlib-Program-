import matplotlib.pyplot as plt

def on_close(event):
    print('Figure closed!')

fig, ax = plt.subplots()
fig.canvas.mpl_connect('close_event', on_close)
plt.show()
