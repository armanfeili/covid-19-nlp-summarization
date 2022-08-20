import pandas as pd
import math

df_bySex = pd.read_csv("../sources/by-sex.csv")

class BySex():
    
    row = None
    findLatest = False
    last_index_based_on_location_key = 0
    dataExist = True
    
    new_confirmed_male = None
    new_confirmed_female = None
    cumulative_confirmed_male = None
    cumulative_confirmed_female = None
    new_deceased_male = None
    new_deceased_female = None
    cumulative_deceased_male = None
    cumulative_deceased_female = None
    new_hospitalized_patients_male = None
    new_hospitalized_patients_female = None
    cumulative_hospitalized_patients_male = None
    cumulative_hospitalized_patients_female = None
    
    def __init__(self, location_key, date = None):
        self.location_key = location_key        

        if (date != None):
            self.date = date
        else:
            self.date = None
            self.findLatest = True
    
    def setData(self):        
        if (self.findLatest):
            self.last_index_based_on_location_key = df_bySex.query(f'location_key == "{self.location_key}"').index.max()
            
            if not(math.isnan(self.last_index_based_on_location_key)):
                self.row = df_bySex.iloc[self.last_index_based_on_location_key]
            else:
                print("Sorry... There is no data based on sex by this location key.")
                self.dataExist = False
                return
            
            self.date = self.row['date']
            self.location_key = self.row['location_key']
            if not (math.isnan(self.row['new_confirmed_male'])): self.new_confirmed_male = math.ceil(self.row['new_confirmed_male'])
            if not (math.isnan(self.row['new_confirmed_female'])): self.new_confirmed_female = math.ceil(self.row['new_confirmed_female'])
            if not (math.isnan(self.row['cumulative_confirmed_male'])): self.cumulative_confirmed_male = math.ceil(self.row['cumulative_confirmed_male'])
            if not (math.isnan(self.row['cumulative_confirmed_female'])): self.cumulative_confirmed_female = math.ceil(self.row['cumulative_confirmed_female'])
            if not (math.isnan(self.row['new_deceased_male'])): self.new_deceased_male = math.ceil(self.row['new_deceased_male'])
            if not (math.isnan(self.row['new_deceased_female'])): self.new_deceased_female = math.ceil(self.row['new_deceased_female'])
            if not (math.isnan(self.row['cumulative_deceased_male'])): self.cumulative_deceased_male = math.ceil(self.row['cumulative_deceased_male'])
            if not (math.isnan(self.row['cumulative_deceased_female'])): self.cumulative_deceased_female = math.ceil(self.row['cumulative_deceased_female'])
            if not (math.isnan(self.row['new_hospitalized_patients_male'])): self.new_hospitalized_patients_male = math.ceil(self.row['new_hospitalized_patients_male'])
            if not (math.isnan(self.row['new_hospitalized_patients_female'])): self.new_hospitalized_patients_female = math.ceil(self.row['new_hospitalized_patients_female'])
            if not (math.isnan(self.row['cumulative_hospitalized_patients_male'])): self.cumulative_hospitalized_patients_male = math.ceil(self.row['cumulative_hospitalized_patients_male'])
            if not (math.isnan(self.row['cumulative_hospitalized_patients_female'])): self.cumulative_hospitalized_patients_female = math.ceil(self.row['cumulative_hospitalized_patients_female']) 
                                                                     
        else:
            self.row = df_bySex.query(f'location_key == "{self.location_key}" & date == "{self.date}"')
            
            if self.row.empty: 
                print("Sorry... There is no data based on sex by this location key.")
                self.dataExist = False
                return
            
            
            self.date = self.row['date'].item()
            self.location_key = self.row['location_key'].item()
            if not (math.isnan(self.row['new_confirmed_male'].item())): self.new_confirmed_male = self.row['new_confirmed_male'].item()
            if not (math.isnan(self.row['new_confirmed_female'].item())): self.new_confirmed_female = self.row['new_confirmed_female'].item()
            if not (math.isnan(self.row['cumulative_confirmed_male'].item())): self.cumulative_confirmed_male = self.row['cumulative_confirmed_male'].item()
            if not (math.isnan(self.row['cumulative_confirmed_female'].item())): self.cumulative_confirmed_female = self.row['cumulative_confirmed_female'].item()
            if not (math.isnan(self.row['new_deceased_male'].item())): self.new_deceased_male = self.row['new_deceased_male'].item()
            if not (math.isnan(self.row['new_deceased_female'].item())): self.new_deceased_female = self.row['new_deceased_female'].item()
            if not (math.isnan(self.row['cumulative_deceased_male'].item())): self.cumulative_deceased = self.row['cumulative_deceased_male'].item()
            if not (math.isnan(self.row['cumulative_deceased_female'].item())): self.cumulative_deceased_female = self.row['cumulative_deceased_female'].item()
            if not (math.isnan(self.row['new_hospitalized_patients_male'].item())): self.new_hospitalized_patients_male = self.row['new_hospitalized_patients_male'].item()
            if not (math.isnan(self.row['new_hospitalized_patients_female'].item())): self.new_hospitalized_patients_female = self.row['new_hospitalized_patients_female'].item()
            if not (math.isnan(self.row['cumulative_hospitalized_patients_male'].item())): self.cumulative_hospitalized_patients_male = self.row['cumulative_hospitalized_patients_male'].item()
            if not (math.isnan(self.row['cumulative_hospitalized_patients_female'].item())): self.cumulative_hospitalized_patients_female = self.row['cumulative_hospitalized_patients_female'].item()

    def generateReport(self):
        file_path = r'./generated-report.txt'
        
        if not (self.dataExist): return
        
        with open(file_path, 'a+') as fp:
            fp.write(f'\n\n')
            fp.write(f'Covid data by sex for location - {self.location_key}: \n')
                        
            fp.write('There is no date. \n') if self.date == None else fp.write(f'date is {self.date}\n')
            fp.write('There is no location_key. \n') if self.location_key == None else fp.write(f'location_key is {self.location_key}\n')
            fp.write('There is no new_confirmed_male. \n') if self.new_confirmed_male == None or self.new_confirmed_male == 0 else fp.write(f'new_confirmed_male is {math.ceil(self.new_confirmed_male)}\n')
            fp.write('There is no new_confirmed_female. \n') if self.new_confirmed_female == None or self.new_confirmed_female == 0 else fp.write(f'new_confirmed_female is {math.ceil(self.new_confirmed_female)}\n')
            fp.write('There is no cumulative_confirmed_male. \n') if self.cumulative_confirmed_male == None or self.cumulative_confirmed_male == 0 else fp.write(f'cumulative_confirmed_male is {math.ceil(self.cumulative_confirmed_male)}\n')
            fp.write('There is no cumulative_confirmed_female. \n') if self.cumulative_confirmed_female == None or self.cumulative_confirmed_female == 0 else fp.write(f'cumulative_confirmed_female is {math.ceil(self.cumulative_confirmed_female)}\n')
            fp.write('There is no new_deceased_male. \n') if self.new_deceased_male == None or self.new_deceased_male == 0 else fp.write(f'new_deceased_male is {math.ceil(self.new_deceased_male)}\n')
            fp.write('There is no new_deceased_female. \n') if self.new_deceased_female == None or self.new_deceased_female == 0 else fp.write(f'new_deceased_female is {math.ceil(self.new_deceased_female)}\n')
            fp.write('There is no cumulative_deceased_male. \n') if self.cumulative_deceased_male == None or self.cumulative_deceased_male == 0 else fp.write(f'cumulative_deceased_male is {math.ceil(self.cumulative_deceased_male)}\n')
            fp.write('There is no cumulative_deceased_female. \n') if self.cumulative_deceased_female == None or self.cumulative_deceased_female == 0 else fp.write(f'cumulative_deceased_female is {math.ceil(self.cumulative_deceased_female)}\n')
            fp.write('There is no new_hospitalized_patients_male. \n') if self.new_hospitalized_patients_male == None or self.new_hospitalized_patients_male == 0 else fp.write(f'new_hospitalized_patients_male is {math.ceil(self.new_hospitalized_patients_male)}\n')
            fp.write('There is no new_hospitalized_patients_female. \n') if self.new_hospitalized_patients_female == None or self.new_hospitalized_patients_female == 0 else fp.write(f'new_hospitalized_patients_female is {math.ceil(self.new_hospitalized_patients_female)}\n')
            fp.write('There is no cumulative_hospitalized_patients_male. \n') if self.cumulative_hospitalized_patients_male == None or self.cumulative_hospitalized_patients_male == 0 else fp.write(f'cumulative_hospitalized_patients_male is {math.ceil(self.cumulative_hospitalized_patients_male)}\n')
            fp.write('There is no cumulative_hospitalized_patients_female. \n') if self.cumulative_hospitalized_patients_female == None or self.cumulative_hospitalized_patients_female == 0 else fp.write(f'cumulative_hospitalized_patients_female is {math.ceil(self.cumulative_hospitalized_patients_female)}\n')
                        

# bySex = BySex('US','2021-10-31')
bySex = BySex('MX')

bySex.setData()
bySex.generateReport()
bySex.row