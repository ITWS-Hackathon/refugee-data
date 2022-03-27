import pandas as pd
import sys



def main():
    if (len(sys.argv) <= 1):
        print("Not enough arguments, need the input file name and then te the output file name")
        return
    

    test = pd.read_csv(f'./{sys.argv[1]}')

    test_trimmed = pd.DataFrame();

    test_trimmed['location'] = test['Indicator']
    test_trimmed['TIME'] = test['TIME']
    test_trimmed['Time'] = test['Time']
    test_trimmed['Value'] = test['Value']


    locations, values_2015, values_2016, values_2017, values_2018, values_2019, values_2020 = [], [], [], [], [], [], []

    for i in range(0, len(test_trimmed), 6):
        locations.append(test_trimmed.iloc[i]['location'])
        values_2015.append(test_trimmed.iloc[i]['Value'])
        values_2016.append(test_trimmed.iloc[i]['Value'])
        values_2017.append(test_trimmed.iloc[i]['Value'])
        values_2018.append(test_trimmed.iloc[i]['Value'])
        values_2019.append(test_trimmed.iloc[i]['Value'])
        values_2020.append(test_trimmed.iloc[i]['Value'])

    test2 = pd.DataFrame();
    test2['Inbound Country'] = locations
    test2['2015'] = values_2015
    test2['2016'] = values_2016
    test2['2017'] = values_2017
    test2['2018'] = values_2018
    test2['2019'] = values_2019
    test2['2020'] = values_2020

    # print(test2)
    # print(test2.head())

    test2.to_csv(f'{sys.argv[2]}', sep='\t')



if (__name__ == '__main__'):
    main();
    # print(sys.argv)
        
        