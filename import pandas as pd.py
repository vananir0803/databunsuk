import pandas as pd
import matplotlib.pyplot as pit

csv_data = pd.read_csv(r'C:\databun\data_company', encoding='cp949')
print(csv_data.head())

csv_data.set_index('Un: 0', inplace=True)

for colume in csv_data.columes:
    plt.plot(csv_data.index, csv_data.loc[:, column], marker='o', label=column)

plt.xlabel('M')
plt.ylabel('V')
plt.title('Data')
plt.legend()
plt.show()
