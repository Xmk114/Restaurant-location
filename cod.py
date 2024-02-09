import matplotlib.pyplot as plt

def calculate_profit(income, cost):
    return income - cost

def get_regions_data(num_regions):
    incomes = []
    costs = []
    for i in range(num_regions):
        # 总收入
        while True:
            try:
                P = float(input(f"请输入第{i + 1}个区域人流量: "))
                break
            except ValueError:
                int("请输入一个有效的数值")
        while True:
            try:
                R = float(input(f"请输入第{i + 1}个区域进店i率(0-1): "))
                if 0 <= R <= 1:
                    break
                else:
                    print("请输入0-1之间的数")
            except ValueError:
                print("请输入一个有效的数值")
        while True:
            try:
                E = float(input(f"请输入第{i + 1}个区域环境卫生指数(0-1): "))
                if 0 <= E <= 1:
                    break
                else:
                    print("请输入0-1之间的数")
            except ValueError:
                print("请输入一个有效的数值")
        while True:
            try:
                N = float(input(f"请输入第{i + 1}个区域竞争对手数量: ")) + 1
                if N > 0:
                    break
                else:
                    print("请输入一个正数的数值")
            except ValueError:
                print("请输入一个有效的数值")
        while True:
            try:
                Cpp = float(input(f"请输入第{i + 1}个区域人均消费: "))
                break
            except ValueError:
                print("请输入一个有效的数值")

        Q = P * R * E * (1 / N)
        Total = Q * Cpp * 365
        incomes.append(Total)

        # 总支出
        while True:
            try:
                Rent = float(input(f"请输入第{i + 1}个区域的年租金: "))
                break
            except ValueError:
                print("请输入一个有效的数值")
        while True:
            try:
                L = float(input(f"请输入第{i + 1}个区域的年劳动成本(平均工资×人数): "))
                break
            except ValueError:
                print("请输入一个有效的数值")
        while True:
            try:
                W = float(input(f"请输入第{i + 1}个区域的水电费: "))
                break
            except ValueError:
                print("请输入一个有效的数值")
        while True:
            try:
                fp = float(input(f"请输入第{i + 1}个区域的餐品总进价: "))
                break
            except ValueError:
                print("请输入一个有效的数值")
        C = Rent + L + W + fp
        costs.append(C)

    return incomes, costs

# 获取所有区域的收入和成本
num_regions = int(input("请输入有几个区域："))
incomes, costs = get_regions_data(num_regions)
profits = [calculate_profit(income, cost) for income, cost in zip(incomes, costs)]

# 找出利润最大的区域
max_profit = max(profits)
max_profit_region = profits.index(max_profit)
print(f"最大利润为：{max_profit}，代表的区域是第{max_profit_region + 1}个区域。")

# 输出每个区域的毛利润率，并判断是否大于60%
for i, (income, cost) in enumerate(zip(incomes, costs)):
    gross_profit = income - cost
    gross_profit_rate = gross_profit / income
    print(f"第{i + 1}个区域的毛利润率为：{gross_profit_rate:.2%}")
    print(f"第{i + 1}个区域的毛利润为：{gross_profit:.2f}")
    if gross_profit_rate > 0.6:
        print(f"第{i + 1}个区域正在向好的方面发展")
    else:
        print(f"第{i + 1}个区域需要进一步努力")

# 计算盈亏平衡点客流量和营业额
Q_BEPs = [(cost / income) for income, cost in zip(incomes, costs)]
T_BEPs = [income * Q_BEP for income, Q_BEP in zip(incomes, Q_BEPs)]

# 输出各个区域的盈亏平衡点客流量和营业额
for i, (region_Q_BEP, region_T_BEP) in enumerate(zip(Q_BEPs, T_BEPs)):
    print(f"第{i + 1}个区域的盈亏平衡点客流量为：{region_Q_BEP:.2f}人")
    print(f"第{i + 1}个区域的盈亏平衡点营业额为：{region_T_BEP:.2f}元")

# 绘制利润柱状图
# 设置Matplotlib默认字体
plt.rcParams['font.sans-serif'] = ['SimSun']  # 指定默认字体为SimSun
plt.rcParams['axes.unicode_minus'] = False    # 解决保存图像时负号'-'显示为方块的问题
plt.figure(figsize=(10, 6))
plt.bar(range(1, len(profits) + 1), profits, color='skyblue', width=0.8)
plt.title("各区域利润比较")
plt.xlabel("区域编号")
plt.ylabel("利润")
plt.tick_params(axis='y', colors='skyblue')  # y轴刻度标签的颜色为天蓝色
plt.xticks(range(1, len(profits) + 1))
plt.locator_params(axis='y', nbins=8)

# 在柱子上显示数据
for x, y in zip(range(1, len(profits) + 1), profits):
    plt.text(x, y, f"{y:.2f}", ha="center", va="bottom")

# 绘制盈亏平衡点客流量和营业额折线图
plt.twinx()
plt.plot(range(1, len(T_BEPs) + 1), T_BEPs, color='green', linestyle='--', marker='s', label="营业额")
plt.ylabel("营业额")
plt.tick_params(axis='y', colors='green')  # y轴刻度标签的颜色为绿色
plt.xticks(range(1, len(Q_BEPs) + 1))
plt.locator_params(axis='y', nbins=8)
plt.legend(loc="upper left")

plt.show()
