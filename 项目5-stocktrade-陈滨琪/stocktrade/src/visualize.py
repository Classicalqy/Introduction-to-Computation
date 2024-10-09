import matplotlib.pyplot as plt
import seaborn as sns

def visualize(price, states_buy, states_sell, total_gains, invest, path):
    sns.set()
    fig = plt.figure(figsize=(15, 5))
    plt.plot(price, color='r', lw=2.)
    plt.plot(price, '^', markersize=10, color='m',
            label='buying signal', markevery=states_buy)
    plt.plot(price, 'v', markersize=10, color='k',
            label='selling signal', markevery=states_sell)
    plt.title('total gains %f, total investment %f%%' % (total_gains, invest))
    plt.legend()
    plt.savefig(path)
