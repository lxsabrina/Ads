# 合约广告（GD）播放控制算法实现
# 任务描述：给定广告列表的播放概率（也叫做T时刻的流量分配概率），给出任意时刻的广告候选列表。
# 算法描述：  随机概率>drop_rate，广告展现；否则丢弃。（注：概率阈值是drop_rate， drop_rate = 1-播放rate）

from collections import defaultdict
import random

class PlayController:
    def __init__(self):
        self.play_rate = dict()
        #广告AD在第一天，第二天，第三天的播放概率矩阵。X代表控制不同天的预算比例（第一天0.5，第二天0.3， 第三天0.2），Y代表控制不同位置的预算分配比例。
        #两个子问题：T时刻花多少钱，T时刻的每个位置花多少钱。
        #第一个问题：T时刻花多少（pacing)，通过参竟率来控制展现速度，实现匀速播放（匀速播放指的是 广告消耗曲线和大盘消耗曲线一致）。算法描述：当 广告的累计消耗 > 大盘消耗比 * 广告当日预算，播放速度加少，否则播放速度加亏爱
      
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
