import matplotlib.pyplot as plt

def on_enter_axes(event):
    event.inaxes.patch.set_facecolor('yellow')
    event.canvas.draw()

def on_leave_axes(event):
    event.inaxes.patch.set_facecolor('white')
    event.canvas.draw()

fig, ax = plt.subplots()
fig.canvas.mpl_connect('axes_enter_event', on_enter_axes)
fig.canvas.mpl_connect('axes_leave_event', on_leave_axes)
plt.show()
