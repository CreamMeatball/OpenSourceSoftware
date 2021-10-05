import os

def read_data(filename):
    # currentPath = os.getcwd()
    # print("주소 : ", currentPath)
    data = []
    with open(filename, 'r') as f:
        for line in f:
            values = []
            if line.startswith('#'):
                continue
            for word in line.split(','):
                values.append(int(word))
            data.append(values)
    return data

def add_weighted_average(data, weight):
    for row in data:
        average = weight[0] * row[0] * weight[1] * row[1]
        row.append(average)

def analyze_data(data):
    mean = sum(data) / len(data)
    var_tmp = 0
    for i in range(len(data)):
        var_tmp += (data[i] - mean)**2
    var = var_tmp / len(data)
    data_tmp = data
    data_tmp.sort()
    median = data_tmp[int(len(data_tmp)/2)]
    return mean, var, median, min(data), max(data)

if __name__ == '__main__':
    data = read_data('data/class_score_en.csv')
    if data and len(data[0]) == 2:
        add_weighted_average(data, [40/125, 60/100])
        if len(data[0]) == 3:
            print('### Individual Score')
            print()
            print('| Midterm | Final | Total |')
            print('| ------- | ----- | ----- |')
            for row in data:
                print(f'| {row[0]} | {row[1]} | {row[2]:.3f} |')
            print()

            print('### Examination Analysis')
            col_n = len(data[0])
            col_name = ['Midterm', 'Final', 'Total']
            colwise_data = [ [row[c] for row in data] for c in range(col_n) ]
            for c, score in enumerate(colwise_data):
                mean, var, median, min_, max_ = analyze_data(score)
                print(f'* {col_name[c]}')
                print(f'  * Mean: **{mean:.3f}**')
                print(f'  * Variance: {var:.3f}')
                print(f'  * Median: **{median:.3f}**')
                print(f'  * Min/Max: ({min_:.3f}, {max_:.3f})')