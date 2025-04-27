import matplotlib.pyplot as plt
ax=plt.subplot()

# 数据
sizes = [215, 130, 245, 210]
labels = ['Python', 'C++', 'Ruby', 'Java']
colors = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue']

# 绘制饼图
ax.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=140)
plt.title('Pie Chart')
plt.show()


