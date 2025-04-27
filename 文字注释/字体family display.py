import matplotlib.pyplot as plt

plt.plot([1, 2, 3], [4, 5, 6])
# Serif 字体
plt.text(1, 4, 'Serif Font', family='serif', fontsize=14, color='red')
# Sans-serif 字体
plt.text(1, 5, 'Sans-serif Font', family='sans-serif', fontsize=14, color='blue')
# Cursive 字体
plt.text(1, 6, 'Cursive Font', family='cursive', fontsize=14, color='green')
# Fantasy 字体
plt.text(2, 4, 'Fantasy Font', family='fantasy', fontsize=14, color='purple')
# Monospace 字体
plt.text(2, 5, 'Monospace Font', family='monospace', fontsize=14, color='orange')

plt.show()


