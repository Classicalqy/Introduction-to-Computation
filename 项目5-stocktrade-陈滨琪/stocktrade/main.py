import argparse
import pandas as pd
from src.trade import buy_stock
from src.strategy import turtle, movingaverage, abcd, diy
from src.visualize import visualize

parser = argparse.ArgumentParser()
parser.add_argument('--strategy', help='Trade strategy', choices=['turtle', 'movingaverage', 'abcd', 'diy'], default=None)
parser.add_argument('--market_type', help='Market type',
                    choices=['poor', 'normal', 'rich', 'inexhaustible'], default=None)
parser.add_argument('--verbose', help='Verbose', type=int, choices=[0, 1], default=0)
parser.add_argument('--arg1', help='Argument 1', default=None)
parser.add_argument('--arg2', help='Argument 2', default=None)
parser.add_argument('--arg3', help='Argument 3', default=None)
parser.add_argument('--arg4', help='Argument 4', default=None)
# 如果diy函数需要更多的参数可以在这里继续添加

# 读取参数
args = parser.parse_args()
strategy = args.strategy
market_type = args.market_type
verbose = args.verbose
arg1 = args.arg1
arg2 = args.arg2
arg3 = args.arg3
arg4 = args.arg4

# 读取数据
price = pd.read_csv('data/dataset.csv')['Price'].values


if strategy == 'turtle':
    if arg1 == None:
        raise ValueError('Please input the value of w')
    signal = turtle(price, int(arg1))

elif strategy == 'movingaverage':
    if arg1 == None:
        raise ValueError('Please input the value of sw')
    if arg2 == None:
        raise ValueError('Please input the value of lw')
    signal = movingaverage(price, int(arg1), int(arg2))
    
elif strategy == 'abcd':
    if arg1 == None:
        raise ValueError('Please input the value of w')
    if arg2 == None:
        raise ValueError('Please input the value of skip_loop')
    signal = abcd(price, int(arg1), int(arg2))
    
elif strategy == 'diy':
    signal = diy(price)
    
else:
    raise NotImplementedError('Strategy not implemented, please check your strategy name')

# 检查signal是否合法
if len(signal) != len(price):
    raise ValueError('The length of signal is not equal to the length of trade days')
for i in signal:
    if i not in [-1,0,1]:
        raise ValueError('The value of signal should be -1, 0 or 1')
    
# 交易
if market_type == 'poor':
    initial_money = 1000
elif market_type == 'normal':
    initial_money = 5000
elif market_type == 'rich':
    initial_money = 10000
elif market_type == 'inexhaustible':
    initial_money = 1000000000000
else:
    raise NotImplementedError('Market type not implemented, please check your market type name')
print('Stratepy: %s, Market type: %s' % (strategy, market_type))
states_buy, states_sell, total_gains, invest = buy_stock(price, signal, initial_money, verbose)

# 绘图
path = 'img/' + strategy + '_' + market_type + '.png'
visualize(price, states_buy, states_sell, total_gains, invest, path)

# 打印结果
print('Total gains %f, total investment %f%%' % (total_gains, invest))
