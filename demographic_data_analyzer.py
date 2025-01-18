import pandas as pd
import numpy as np

def calculate_demographic_data(print_data=True):
    df = pd.read_csv('adult.data.csv')

    
    races = pd.unique(df['race'])
    racecount = {r:0 for r in races}
    for i in range(len(df['race'])):
        if df.iloc[i,8] in races:
            racecount[df.iloc[i,8]]+=1
    race_count=pd.Series(data = racecount, index = races)

    sexes = pd.unique(df['sex'])
    sexcount = 0
    agesum = 0
    for i in range(len(df['sex'])):
        if df.iloc[i,9] =='Male':
            sexcount+=1
            agesum+=df.iloc[i,0]
    average_age_men = np.round(agesum/sexcount,1)

    
    eds = pd.unique(df['education'])
    edscount = {e:0 for e in eds}
    adved = ['Bachelors','Masters','Doctorate']
    payclassadved = {
        'with':0,
        'without':0
    }
    for i in range(len(df['sex'])):
        edscount[df.iloc[i,3]]+=1
        if df.iloc[i,3] in adved and df.iloc[i,14] == '>50K':
            payclassadved['with']+=1
        elif df.iloc[i,3] not in adved and df.iloc[i,14] == '>50K':
            payclassadved['without']+=1

    pplwadved = edscount['Bachelors']+edscount['Masters']+edscount['Doctorate']
    pplwoadved = len(df['sex']) - pplwadved

    
    percentage_bachelors = np.round(edscount['Bachelors']/len(df['sex'])*100,1)
    higher_education_rich = np.round(payclassadved['with']/pplwadved*100,1)
    lower_education_rich = np.round(payclassadved['without']/pplwoadved*100,1)

    
    min_hours = 100000000
    for i in range(len(df['hours-per-week'])):
        if int(df.iloc[i,12])<min_hours:
            min_hours = int(df.iloc[i,12])
    num_min_workers = 0
    rich_min =0
    for i in range(len(df['sex'])):
        if df.iloc[i,12] == min_hours:
            num_min_workers += 1
            if df.iloc[i,14] == '>50K':
                rich_min+=1
    
    
    rich_percentage = rich_min/num_min_workers*100

   
    nations = pd.unique(df['native-country'])
    countrycount = {r:0 for r in nations}
    richincountry = {r:0 for r in nations}
    richpercent_country = {r:0 for r in nations}
    for i in range(len(df['race'])):
        if df.iloc[i,13] in nations:
            countrycount[df.iloc[i,13]]+=1
            if df.iloc[i,14] == '>50K':
                richincountry[df.iloc[i,13]]+=1
    
    for r in nations:
        richpercent_country[r] = np.round(richincountry[r]/countrycount[r]*100,1)
    
    maxpercent = 0
    rich_country = ''
    for r in nations:
        if richpercent_country[r]>maxpercent:
            rich_country = r
            maxpercent = richpercent_country[r]
    highest_earning_country = rich_country

    highest_earning_country_percentage = maxpercent

    
    occupations = pd.unique(df['occupation'])
    occ_count = {r:0 for r in occupations}
    for i in range(len(df['race'])):
        if df.iloc[i,13] == 'India':
            occ_count[df.iloc[i,6]]+=1
    
    pplinjob = 0
    job = ''
    for r in occupations:
        if occ_count[r]>pplinjob:
            job = r
            pplinjob = occ_count[r]
    top_IN_occupation = job

    
if print_data:
        print("Number of each race:\n", race_count) 
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupations in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage':
        highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }
