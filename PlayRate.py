# 合约广告（GD）播放控制算法实现
# 任务描述：给定广告列表的播放概率（也叫做T时刻的流量分配概率），给出任意时刻的广告候选列表。
# 算法描述：  随机概率>drop_rate，广告展现；否则丢弃。（注：概率阈值是drop_rate， drop_rate = 1-播放rate）

from collections import defaultdict
import random

class PlayController:
    def __init__(self):
        self.play_rate = dict()
        #广告AD在第一天，第二天，第三天的播放概率矩阵。X代表控制不同天的预算比例（第一天0.5，第二天0.3， 第三天0.2），Y代表控制不同位置的预算分配比例。
        #两个子问题：每天花多少钱，每个位置花多少钱。
        #生效逻辑：播放系统通过展现控制 来实现广告每天花多少钱，每个位置花多少钱。（cost = requests * ecpm * bid， 对于GD广告， 请求量正比于消耗；对于效果广告，请求量 = 消耗/ecpm）
        self.play_rate['pos1'] = [0.4, 0.1, 0.05] 
        self.play_rate['pos2'] = [0.1, 0.1, 0.1]
        self.play_rate['pos3'] = [0.1, 0.1, 0.05]
    
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
