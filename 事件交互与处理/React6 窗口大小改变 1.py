import matplotlib.pyplot as plt

def on_resize(event):
    print(f'New width: {event.width}, New height: {event.height}')

fig, ax = plt.subplots()
fig.canvas.mpl_connect('resize_event', on_resize)
plt.show()
