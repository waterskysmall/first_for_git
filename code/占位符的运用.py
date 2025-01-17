name = "野兽先辈"
stock_price = 19.99
stock_code = 115414
growth_factor = 1.2
days = 7
print(f"公司：{name}，股票代码：{stock_code}，当前股价：{stock_price}")
print("每日增长系数是：%.1f，经过%d天的增长后，股价达到了：%.2f" % (growth_factor, days, 19.99 * (1.2 ** 7)))