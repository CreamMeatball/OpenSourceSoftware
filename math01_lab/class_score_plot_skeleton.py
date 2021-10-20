#%%
import glob, csv
import matplotlib.pyplot as plt

def read_data(filename):
    files = glob.glob(filename)
    all_data = []
    for file in files:
        with open(file, 'r') as f:     # Construct a file object
            csv_reader = csv.reader(f) # Construct a CSV reader object
            data = []
            for line in csv_reader:
                if line and not line[0].strip().startswith('#'): # If 'line' is valid and not a header
                    data.append([int(val) for val in line])      # Append 'line' to 'data' as numbers
            all_data = all_data + data                           # Merge 'data' to 'all_data'
    return all_data

if __name__ == '__main__':
    # Load score data
    class_kr = read_data('data/class_score_kr.csv')
    class_en = read_data('data/class_score_en.csv')

    # Derive miterm, final, and total scores
    midtm_kr = [0]
    final_kr = [0]
    total_kr = [0]
    midtm_en = [0]
    final_en = [0]
    total_en = [0]

    # Plot midterm/final scores as points
    plt.plot(midtm_kr, final_kr)

    # Plot total scores as a histogram

# %%
