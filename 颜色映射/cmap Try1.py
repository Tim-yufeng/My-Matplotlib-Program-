import matplotlib.pyplot as plt
import numpy as np
data = np.random.rand(4,4,3)
fig2,ax2=plt.subplots()
ax2.imshow(data)
plt.show()
print(data)



# cmap=plt.get_cmap('viridis')
# # colormaps=plt.colormaps()  # 列出所有颜色映射
# #
# # print(colormaps)
# print(cmap)
# plt.show()
# fig1,ax1=plt.subplots()



# surf1=ax1.imshow([[0,1,2],[2,0,1],[1,2,0]], cmap='hot')
# plt.show()
# surf2=ax2.imshow([[0,1,2],[0,1,2],[0,1,2]], cmap='hot')
# fig1.colorbar(surf1,ax=ax1)
# fig2.colorbar(surf2,ax=ax2)
# ax2.imshow(np.array([
#     [[0.0, 0.0, 0.0], [1.0, 0.0, 0.5], [0.5, 1.0, 0.0]],
#     [[0.0, 0.5, 1.0], [0.0, 0.0, 0.0], [0.5, 1.0, 0.0]],
#     [[0.0, 1.0, 0.5], [1.0, 0.0, 0.5], [0.0, 0.0, 0.0]]
# ])
# )

# import matplotlib.pyplot as plt
# import numpy as np
#
# # 获取所有颜色映射名称
# colormaps = plt.colormaps()
#
# # 创建一个图形窗口
# fig, axes = plt.subplots(nrows=len(colormaps) // 4 + 1, ncols=4, figsize=(15, 30))
# axes = axes.flatten()
#
# # 遍历所有颜色映射并绘制示例
# for i, cmap_name in enumerate(colormaps):
#     ax = axes[i]
#     gradient = np.linspace(0, 1, 256)
#     gradient = np.vstack((gradient, gradient))
#     ax.imshow(gradient, aspect='auto', cmap=cmap_name)
#     ax.set_title(cmap_name, fontsize=10)
#     ax.axis('off')
#
# # 调整布局并显示
# plt.tight_layout()
# plt.show()
