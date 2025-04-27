import matplotlib.pyplot as plt

def on_enter(event):
    fig.patch.set_facecolor('yellow')
    fig.canvas.draw()

def on_leave(event):
    fig.patch.set_facecolor('green')
    fig.canvas.draw()

fig, ax = plt.subplots()
fig.canvas.mpl_connect('figure_enter_event', on_enter)
fig.canvas.mpl_connect('figure_leave_event', on_leave)
plt.show()
