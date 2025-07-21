#Exercise 1

#1
class Statistics:
    def __init__(self,data):
        self.data = sorted(data)
    
    def count(self):
        return len(self.data)

    def mean(self):
        return sum(self.data) / len(self.data)
    
    def median(self):
        middle = len(self.data) // 2
        if len(self.data) % 2 != 0:
            return self.data[middle]
        else:
            median = (self.data[middle] + self.data[middle - 1]) / 2
            return median
    
    def sum_tot(self):
        total = 0
        for num in self.data:
            total += num
        return total
    
    def minimum(self):
        return self.data[0]
    
    def maximum(self):
        return self.data[-1]
    
    def range_of_list(self):
        return self.data[-1] - self.data[0]
    
    def frequency(self):
        from collections import Counter
        sorted_data = Counter(self.data)
        return sorted_data

    def mode(self):
        from collections import Counter
        sorted_data = Counter(self.data)
        value, count = sorted_data.most_common(1)[0]
        return f'Mode: {value} Count: {count}'

    def std(self):
        total = 0
        for num in self.data:
            total += (num - self.mean()) ** 2
        dev = (total / self.count()) ** 0.5
        return dev
    
    def var(self):
        return self.std() ** 2

#Example Usage:
ages = [31, 26, 34, 37, 27, 26, 32, 32, 26, 27, 27, 24, 32, 33, 27, 25, 26, 38, 37, 31, 34, 24, 33, 29, 26]

stats = Statistics(ages)
print('Count:', stats.count()) # 25
print('Sum: ', stats.sum_tot()) # 744
print('Min: ', stats.minimum()) # 24
print('Max: ', stats.maximum()) # 38
print('Range: ', stats.range_of_list()) # 14
print('Mean: ', stats.mean()) # 30
print('Median:', stats.median()) # 29
print('Mode:', stats.mode()) # {'mode': 26, 'count': 5}
print('Standard Deviation: ', stats.std()) # 4.2
print('Variance: ', stats.var()) # 17.5
print('Frequency Distribution: ', stats.frequency()) # [(20.0, 26), (16.0, 27), (12.0, 32), (8.0, 37), (8.0, 34), (8.0, 33), (8.0, 31), (8.0, 24), (4.0, 38), (4.0, 29), (4.0, 25)]