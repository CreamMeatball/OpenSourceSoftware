import glob, csv

files = glob.glob('math01_lab/data/class_score_??.csv')
all_data = []
for file in files:
    with open(file, 'r') as f:
        csv_reader = csv.reader(f)
        data = []
        for line in csv_reader:
            if line and not line[0].strip().startswith('#'):
                data.append([int(val) for val in line])
        all_data = all_data + data

print(all_data)