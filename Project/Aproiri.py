import itertools as it 
data = {
    1:['L1','L2','L5'],
    2:['L2','L4'],
    3:['L2','L3'],
    4:['L1','L2','L4'],
    5:['L1','L3'],
    6:['L2','L3'],
    7:['L1','L3'],
    8:['L1','L2','L5','L3'],
    9:['L1','L2','L3'],
    }

class Rule:
    def __init__(self,A=None, B = None):
        self.A = A 
        self.B = B 
        self.cofidence = None
class Aprori:
    def __init__(self, min_support, min_cofidence):
        self.min_cofidence = min_cofidence
        self.min_support = min_support
        self.rules = []
     
    def fit(self,data):
        self.data = data 
        elements = set()

        for k ,v in self.data.items():
            for elment in v: 
                elements.add(elment)
        assert len(elements) <= len(self.data.keys()), "invalid data"
        elements = [[x,] for x in elements]
        self.old_item_set  = []
        self.old_sup_count = []

        self.new_item_set =  []
        self.new_sup_count = []
        for elm in elements:
            elm_cnt = self.counter(elm)
            self.old_item_set.append(elm) 
            self.old_sup_count.append(elm_cnt)
        
        i =0
        while i <len(self.old_item_set):
            if self.old_sup_count[i] < self.min_support:
                self.old_sup_count.pop(i)
                self.old_item_set.pop(i)
            else : 
                i+=1

    def counter(self,items:list):
        cnt = 0 
        for k , v in self.data.items():
            c = [i in v for i in items] 
            if False in c :
                continue 
            else: 
                cnt+=1 
        return cnt 
    def update_item_set(self): 

        new_item_set = self.generate_new_combinations(self.old_item_set)
        new_sup_count = []
        for item in new_item_set:
            cnt = self.counter(item)
            new_sup_count.append(cnt)
        i =0
        while i <len(new_item_set):
            if new_sup_count[i] < self.min_support:
                new_sup_count.pop(i)
                new_item_set.pop(i)
            else : 
                i+=1
        return new_item_set, new_sup_count
    
    def generate_new_combinations(self,item_set:list):
        new_combinations = []
        for idx, item in enumerate(item_set):
            
            for x in item_set[idx+1:]:
                new_combine = item.copy()
                for element in x:
                    new_combine.append(element)
                if list(set(new_combine)) in new_combinations :
                    continue
                new_combinations.append(list(set(new_combine)))
        return new_combinations
    
    def run(self):
        while True: 
            new_item_set, new_sup_count = self.update_item_set()
            if len(new_sup_count) == 0:
                break 
            self.old_item_set  = new_item_set 
            self.old_sup_count = new_sup_count 
        for item,cnt in zip(self.old_item_set, self.old_sup_count):
            rules  = self.compute_rules(item, cnt)
            self.rules.append(rules)

    def compute_conf(self,rule,cnt):
        cnt_A = self.counter(rule.A) 
        confidence = 10 *cnt / cnt_A 
        return confidence
    def compute_rules(self,pattern,cnt): 
        all_rules = []
        for i in range(1,len(pattern)):
            comb = list(it.combinations(pattern,i))
            comb = [list(x) for x in comb]
            for f in comb:
                rule = Rule()
                rule.A  = f 
                rule.B = [x for x in pattern if x not in f] 
                all_rules.append(rule)
        temp = all_rules.copy()
        for rule in temp[:-len(pattern)]:
            new_rule = Rule()
            new_rule.A = rule.B
            new_rule.B = rule.A

            all_rules.append(new_rule)
        del temp
        i = 0
        while i <len(all_rules):
            conf = self.compute_conf(all_rules[i], cnt)
            if self.min_cofidence < self.min_cofidence :
                del all_rules[i] 
            else : 
                all_rules[i].confidence = conf 
                i+=1  
        return all_rules

# model = Aprori(2,6)
# model.fit(data)
# model.run()
# print(model.old_item_set)
# for st in model.rules :
#     for r in st :
#         print(r.A,'|',r.B, '|', r.confidence*10) 
