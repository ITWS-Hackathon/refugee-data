import pandas as pd
import sys



def main():
    if (len(sys.argv) <= 1):
        print("Not enough arguments, need the input file name and then te the output file name")
        return
    

    test = pd.read_csv(f'./{sys.argv[1]}')

    df = pd.DataFrame();
    locations, values, years = [], [], []


    for i in range(0, len(test), 6):
        if ('female' in test.iloc[i]['Indicator'] or 'male' in test.iloc[i]['Indicator']):
            continue
        temp1 = []
        temp2 = []
        for j in range(6):
            values.append(test.iloc[i+j]['Value'])
            years.append(str(2015 + j))
            locations.append(test.iloc[i]['Indicator'])

        # print(test.iloc[i]['Indicator'], "test")

        # values.append(temp1)
        # years.append(temp2)

    df['Location'] = locations
    df['Year'] = years
    df['Value'] = values

    # df['location'] = test['Indicator']
    # df['Year'] = test['TIME']
    # df['Value'] = test['Value']

    df.to_csv(f'{sys.argv[2]}', sep=',', index=False)
    df.to_json('data_continents.json')



    # df.drop(df.columns[df.apply(lambda col: "female" in col or "male" in col)])

    # df.to_csv(f'{sys.argv[2]}', sep=',', index=False)
    # locations, values_2015, values_2016, values_2017, values_2018, values_2019, values_2020 = [], [], [], [], [], [], []

    # for i in range(0, len(df), 6):
    #     locations.append(df.iloc[i]['location'])
    #     values_2015.append(df.iloc[i]['Value'])
    #     values_2016.append(df.iloc[i+1]['Value'])
    #     values_2017.append(df.iloc[i+2]['Value'])
    #     values_2018.append(df.iloc[i+3]['Value'])
    #     values_2019.append(df.iloc[i+4]['Value'])
    #     values_2020.append(df.iloc[i+5]['Value'])

    # test2 = pd.DataFrame();
    # test2['Inbound Location'] = locations
    # test2['2015'] = values_2015
    # test2['2016'] = values_2016
    # test2['2017'] = values_2017
    # test2['2018'] = values_2018
    # test2['2019'] = values_2019
    # test2['2020'] = values_2020

    # # print(test2)
    # # print(test2.head())

    # test2.to_csv(f'{sys.argv[2]}', sep=',', index=False)



if (__name__ == '__main__'):
    main();
    # print(sys.argv)
        
        