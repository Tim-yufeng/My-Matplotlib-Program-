import matplotlib.pyplot as plt
import numpy as np
import matplotlib.colors as mcolors
fig,ax=plt.subplots()
def on_resize(event):
    a=event.width
    b=event.height
    norm=mcolors.Normalize(0,3,clip=True)
    y1=tuple(norm([np.exp((b)/625),np.exp((a)/1280),np.exp((a+b)/1905)]))
    y2=tuple(norm([np.exp((a)/1280),np.exp((b)/625),np.exp((a-b)/700)]))
    fig.patch.set_facecolor(color=y1)
    ax.patch.set_facecolor(color=y2)
    plt.draw()
    print(f'a={a},b={b}')
fig.canvas.mpl_connect('resize_event', on_resize)
plt.show()

