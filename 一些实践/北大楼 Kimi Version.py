# # # import matplotlib.pyplot as plt
# # # import matplotlib.patches as patches
# # #
# # #
# # # def draw_building(ax):
# # #     # 绘制底部建筑
# # #     ax.add_patch(patches.Rectangle((0.2, 0), 0.6, 0.4, fill=True, color='lightblue'))
# # #
# # #     # 绘制左侧建筑
# # #     ax.add_patch(patches.Rectangle((0.3, 0.4), 0.1, 0.2, fill=True, color='lightblue'))
# # #
# # #     # 绘制右侧建筑
# # #     ax.add_patch(patches.Rectangle((0.6, 0.4), 0.1, 0.2, fill=True, color='lightblue'))
# # #
# # #     # 绘制塔楼
# # #     ax.add_patch(patches.Rectangle((0.45, 0.6), 0.1, 0.3, fill=True, color='lightblue'))
# # #     ax.add_patch(patches.Rectangle((0.45, 0.9), 0.1, 0.1, fill=True, color='red'))
# # #
# # #     # 绘制屋顶
# # #     ax.add_patch(patches.Polygon([[0.2, 0.4], [0.3, 0.6], [0.4, 0.6], [0.45, 0.9], [0.55, 0.9], [06., 0.6], [0.7, 0.6]],
# # #                                  fill=True, color='lightblue'))
# # #
# # #     # 绘制窗户
# # #     for i in range(3):
# # #         for j in range(4):
# # #             ax.add_patch(patches.Rectangle((0.22 + 0.1 * i, 0.02 + 0.1 * j), 0.06, 0.06, fill=True, color='white'))
# # #             ax.add_patch(patches.Rectangle((0.52 + 0.1 * i, 0.02 + 0.1 * j), 0.06, 0.06, fill=True, color='white'))
# # #
# # #     # 设置坐标轴
# # #     ax.set_xlim(0, 1)
# # #     ax.set_ylim(0, 1)
# # #     ax.axis('off')
# # #
# # #
# # # # 创建图形和轴
# # # fig, ax = plt.subplots()
# # # draw_building(ax)
# # # plt.show()
# # import matplotlib.pyplot as plt
# # import matplotlib.patches as patches
# #
# #
# # def draw_building(ax):
# #     # 绘制底部建筑
# #     ax.add_patch(patches.Rectangle((0.2, 0), 0.6, 0.4, fill=True, color='lightblue'))
# #
# #     # 绘制左侧建筑
# #     ax.add_patch(patches.Rectangle((0.3, 0.4), 0.1, 0.2, fill=True, color='lightblue'))
# #
# #     # 绘制右侧建筑
# #     ax.add_patch(patches.Rectangle((0.6, 0.4), 0.1, 0.2, fill=True, color='lightblue'))
# #
# #     # 绘制塔楼
# #     ax.add_patch(patches.Rectangle((0.45, 0.6), 0.1, 0.3, fill=True, color='lightblue'))
# #     ax.add_patch(patches.Rectangle((0.45, 0.9), 0.1, 0.05, fill=True, color='red'))
# #
# #     # 绘制屋顶
# #     ax.add_patch(patches.Polygon([[0.2, 0.4], [0.3, 0.6], [0.4, 0.6], [0.45, 0.9], [0.55, 0.9], [0.6, 0.6], [0.7, 0.6]],
# #                                  fill=True, color='lightblue'))
# #
# #     # 绘制窗户
# #     for i in range(5):
# #         for j in range(5):
# #             ax.add_patch(patches.Rectangle((0.25 + 0.1 * i, 0.05 + 0.1 * j), 0.08, 0.08, fill=True, color='white'))
# #
# #     # 设置坐标轴
# #     ax.set_xlim(0, 1)
# #     ax.set_ylim(0, 1)
# #     ax.axis('off')
# #
# #
# # # 创建图形和轴
# # fig, ax = plt.subplots()
# # draw_building(ax)
# # plt.show()
# import matplotlib.pyplot as plt
# import matplotlib.patches as patches
#
#
# def draw_building(ax):
#     # 绘制底部建筑
#     ax.add_patch(patches.Rectangle((0.2, 0), 0.6, 0.8, fill=True, color='lightblue'))
#
#     # 绘制左侧建筑
#     ax.add_patch(patches.Rectangle((0.3, 0.8), 0.1, 0.2, fill=True, color='lightblue'))
#
#     # 绘制右侧建筑
#     ax.add_patch(patches.Rectangle((0.6, 0.8), 0.1, 0.2, fill=True, color='lightblue'))
#
#     # 绘制塔楼
#     ax.add_patch(patches.Rectangle((0.45, 0.6), 0.1, 0.4, fill=True, color='lightblue'))
#     ax.add_patch(patches.Rectangle((0.45, 1.0), 0.1, 0.05, fill=True, color='red'))
#
#     # 绘制屋顶
#     ax.add_patch(
#         patches.Polygon([[0.2, 0.8], [0.3, 1.0], [0.4, 1.0], [0.45, 1.05], [0.55, 1.05], [0.6, 1.0], [0.7, 1.0]],
#                         fill=True, color='lightblue'))
#
#     # 绘制窗户
#     for i in range(5):
#         for j in range(5):
#             ax.add_patch(patches.Rectangle((0.25 + 0.1 * i, 0.05 + 0.1 * j), 0.08, 0.08, fill=True, color='white'))
#
#     # 设置坐标轴
#     ax.set_xlim(0, 1)
#     ax.set_ylim(0, 1.2)
#     ax.axis('off')
#
#
# # 创建图形和轴
# fig, ax = plt.subplots()
# draw_building(ax)
# plt.show()
import matplotlib.pyplot as plt
import matplotlib.patches as patches


def draw_building(ax):
    # 绘制主体建筑
    ax.add_patch(patches.Rectangle((0.2, 0.1), 0.6, 0.8, fill=True, color='lightblue'))

    # 绘制顶部建筑
    ax.add_patch(patches.Polygon([[0.2, 0.9], [0.4, 0.7], [0.6, 0.7], [0.8, 0.9]], fill=True, color='lightblue'))

    # 绘制窗户
    for i in range(4):
        for j in range(5):
            ax.add_patch(patches.Rectangle((0.25 + 0.15 * i, 0.15 + 0.15 * j), 0.1, 0.1, fill=True, color='white'))

    # 绘制顶部小窗户
    ax.add_patch(patches.Rectangle((0.45, 0.7), 0.1, 0.1, fill=True, color='white'))
    ax.add_patch(patches.Rectangle((0.55, 0.7), 0.1, 0.1, fill=True, color='white'))

    # 设置坐标轴
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis('off')


# 创建图形和轴
fig, ax = plt.subplots()
draw_building(ax)
plt.show()
