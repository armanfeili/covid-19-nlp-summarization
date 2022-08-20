import pandas as pd
import math

df_hospitalization = pd.read_csv("./hospitalizations.csv", sep=',', on_bad_lines='skip', index_col=False, dtype='unicode')

class Hospitalization():
    
    row = None
    findLatest = False
    last_index_based_on_location_key = 0
    dataExist = True
    
    new_hospitalized_patients = None
    cumulative_hospitalized_patients = None
    current_hospitalized_patients = None
    current_intensive_care_patients = None
    
    def __init__(self, location_key, date = None):
        self.location_key = location_key      
        
        if (date != None):
            self.date = date
        else:
            self.date = None
            self.findLatest = True
            
        pass
        
    def setData(self):        
        if (self.findLatest):
            self.last_index_based_on_location_key = df_hospitalization.query(f'location_key == "{self.location_key}"').index.max()
    
            if not(math.isnan(self.last_index_based_on_location_key)):
                self.row = df_hospitalization.iloc[self.last_index_based_on_location_key] 
            else:
                print("Sorry... There is no data based on hospitalization by this location key.")
                self.dataExist = False
                return
            
            self.date = self.row['date']
            self.location_key = self.row['location_key']
            
            if (type(self.row['new_hospitalized_patients']) == str): self.new_hospitalized_patients = int(self.row['new_hospitalized_patients'])
            if (type(self.row['cumulative_hospitalized_patients']) == str): self.cumulative_hospitalized_patients = int(self.row['cumulative_hospitalized_patients'])
            if (type(self.row['current_hospitalized_patients']) == str): self.current_hospitalized_patients = int(self.row['current_hospitalized_patients'])
            if (type(self.row['current_intensive_care_patients']) == str): self.current_intensive_care_patients = int(self.row['current_intensive_care_patients'])

        else:
            self.row = df_hospitalization.query(f'location_key == "{self.location_key}" & date == "{self.date}"')

            if self.row.empty: 
                print("Sorry... There is no data based on hospitalization by this location key.")
                self.dataExist = False
                return


            self.date = self.row['date'].item()
            self.location_key = self.row['location_key'].item()                   
            
            if (type(self.row['new_hospitalized_patients'].item()) == str): self.new_hospitalized_patients = int(self.row['new_hospitalized_patients'].item())
            if (type(self.row['cumulative_hospitalized_patients'].item()) == str): self.cumulative_hospitalized_patients = int(self.row['cumulative_hospitalized_patients'].item())
            if (type(self.row['current_hospitalized_patients'].item()) == str): self.current_hospitalized_patients = int(self.row['current_hospitalized_patients'].item())
            if (type(self.row['current_intensive_care_patients'].item()) == str): self.current_intensive_care_patients = int(self.row['current_intensive_care_patients'].item())

    def generateReport(self):
        file_path = r'./generated-report.txt'
        
        if not (self.dataExist): return
        
        with open(file_path, 'a+') as fp:
            fp.write(f'\n\n')
            fp.write(f'Covid data based on hospitalization for location - {self.location_key}: \n')
                        
            fp.write('There is no date. \n') if self.date == None else fp.write(f'date is {self.date}\n')
            fp.write('There is no location_key. \n') if self.location_key == None else fp.write(f'location_key is {self.location_key}\n')
            
            fp.write('There is no new_hospitalized_patients. \n') if self.new_hospitalized_patients == None or self.new_hospitalized_patients == 0 else fp.write(f'new_hospitalized_patients is {math.ceil(self.new_hospitalized_patients)}\n')
            fp.write('There is no cumulative_hospitalized_patients. \n') if self.cumulative_hospitalized_patients == None or self.cumulative_hospitalized_patients == 0 else fp.write(f'cumulative_hospitalized_patients is {math.ceil(self.cumulative_hospitalized_patients)}\n')
            fp.write('There is no current_hospitalized_patients. \n') if self.current_hospitalized_patients == None or self.current_hospitalized_patients == 0 else fp.write(f'current_hospitalized_patients is {math.ceil(self.current_hospitalized_patients)}\n')
            fp.write('There is no current_intensive_care_patients. \n') if self.current_intensive_care_patients == None or self.current_intensive_care_patients == 0 else fp.write(f'current_intensive_care_patients is {math.ceil(self.current_intensive_care_patients)}\n')

# hospitalization = Hospitalization('US')
hospitalization = Hospitalization('US', '2022-08-01')

hospitalization.setData()
hospitalization.generateReport()
hospitalization.row