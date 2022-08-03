# 合约广告（GD）播放控制算法实现
# 任务描述：给定广告列表的播放概率（也叫做T时刻的流量分配概率），给出任意时刻的广告候选列表。
# 算法描述：  随机概率>drop_rate，广告展现；否则丢弃。（注：概率阈值是drop_rate， drop_rate = 1-播放rate）

from collections import defaultdict
import random

class PlayController:
    def __init__(self):
        self.play_rate = dict()
        #T时刻是一个分配问题，时间序列是一个预估问题。怎么描述
        self.play_rate['ad1'] = [0.5, 0.1, 0.2] 
        self.play_rate['ad2'] = [0.2, 0.2, 0.2]
        self.play_rate['ad3'] = [0.2, 0.3, 0.4]
    
    def play_list(self, t): #返回T时刻的播放列表, t = 0, 1, 2 
        ans = []
        for ad, ad_rate_list in self.play_rate.items():
            rate = ad_rate_list[t]
            random_number = random.uniform(0,1)
            drop_rate = 1-rate
            if random_number >= drop_rate:
                ans.append(ad)
        return ans

if __name__ == '__main__':
    controller = PlayController()
    count = defaultdict(int)
    total = 10000
    for i in range(0, total):
        ans = controller.play_list(0)
        for ad in ans: count[ad] += 1
    for k,v in count.items():
        print(f'{k}: {v}, {v/total}')  
