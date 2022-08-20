import pandas as pd
import math

df_byAge = pd.read_csv("../sources/by-age.csv")

class ByAge():
    
    row = None
    findLatest = False
    last_index_based_on_location_key = 0
    dataExist = True
    
    new_confirmed_age_0 = None
    new_confirmed_age_1 = None
    new_confirmed_age_2 = None
    new_confirmed_age_3 = None
    new_confirmed_age_4 = None
    new_confirmed_age_5 = None
    new_confirmed_age_6 = None
    new_confirmed_age_7 = None
    cumulative_confirmed_age_0 = None
    cumulative_confirmed_age_1 = None
    cumulative_confirmed_age_2 = None
    cumulative_confirmed_age_3 = None
    cumulative_confirmed_age_4 = None
    cumulative_confirmed_age_5 = None
    cumulative_confirmed_age_6 = None
    cumulative_confirmed_age_7 = None
    
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
            self.last_index_based_on_location_key = df_byAge.query(f'location_key == "{self.location_key}"').index.max()
    
            if not(math.isnan(self.last_index_based_on_location_key)):
                self.row = df_byAge.iloc[self.last_index_based_on_location_key] 
            else:
                print("Sorry... There is no data based on ages by this location key.")
                self.dataExist = False
                return
            
            self.date = self.row['date']
            self.location_key = self.row['location_key']
            
            if (type(self.row['new_confirmed_age_0']) == str): self.new_confirmed_age_0 = int(self.row['new_confirmed_age_0'])
            if (type(self.row['new_confirmed_age_1']) == str): self.new_confirmed_age_1 = int(self.row['new_confirmed_age_1'])
            if (type(self.row['new_confirmed_age_2']) == str): self.new_confirmed_age_2 = int(self.row['new_confirmed_age_2'])
            if (type(self.row['new_confirmed_age_3']) == str): self.new_confirmed_age_3 = int(self.row['new_confirmed_age_3'])
            if (type(self.row['new_confirmed_age_4']) == str): self.new_confirmed_age_4 = int(self.row['new_confirmed_age_4'])
            if (type(self.row['new_confirmed_age_5']) == str): self.new_confirmed_age_5 = int(self.row['new_confirmed_age_5'])
            if (type(self.row['new_confirmed_age_6']) == str): self.new_confirmed_age_6 = int(self.row['new_confirmed_age_6'])
            if (type(self.row['new_confirmed_age_7']) == str): self.new_confirmed_age_7 = int(self.row['new_confirmed_age_7'])
            if (type(self.row['cumulative_confirmed_age_0']) == str): self.cumulative_confirmed_age_0 = int(self.row['cumulative_confirmed_age_0'])
            if (type(self.row['cumulative_confirmed_age_1']) == str): self.cumulative_confirmed_age_1 = int(self.row['cumulative_confirmed_age_1'])
            if (type(self.row['cumulative_confirmed_age_2']) == str): self.cumulative_confirmed_age_2 = int(self.row['cumulative_confirmed_age_2'])
            if (type(self.row['cumulative_confirmed_age_3']) == str): self.cumulative_confirmed_age_3 = int(self.row['cumulative_confirmed_age_3'])
            if (type(self.row['cumulative_confirmed_age_4']) == str): self.cumulative_confirmed_age_4 = int(self.row['cumulative_confirmed_age_4'])
            if (type(self.row['cumulative_confirmed_age_5']) == str): self.cumulative_confirmed_age_5 = int(self.row['cumulative_confirmed_age_5'])
            if (type(self.row['cumulative_confirmed_age_6']) == str): self.cumulative_confirmed_age_6 = int(self.row['cumulative_confirmed_age_6'])
            if (type(self.row['cumulative_confirmed_age_7']) == str): self.cumulative_confirmed_age_7 = int(self.row['cumulative_confirmed_age_7'])

        else:
            self.row = df_byAge.query(f'location_key == "{self.location_key}" & date == "{self.date}"')

            if self.row.empty: 
                print("Sorry... There is no data based on ages by this location key.")
                self.dataExist = False
                return


            self.date = self.row['date'].item()
            self.location_key = self.row['location_key'].item()                   
            
            if (type(self.row['new_confirmed_age_0'].item()) == str): self.new_confirmed_age_0 = int(self.row['new_confirmed_age_0'].item())
            if (type(self.row['new_confirmed_age_1'].item()) == str): self.new_confirmed_age_1 = int(self.row['new_confirmed_age_1'].item())
            if (type(self.row['new_confirmed_age_2'].item()) == str): self.new_confirmed_age_2 = int(self.row['new_confirmed_age_2'].item())
            if (type(self.row['new_confirmed_age_3'].item()) == str): self.new_confirmed_age_3 = int(self.row['new_confirmed_age_3'].item())
            if (type(self.row['new_confirmed_age_4'].item()) == str): self.new_confirmed_age_4 = int(self.row['new_confirmed_age_4'].item())
            if (type(self.row['new_confirmed_age_5'].item()) == str): self.new_confirmed_age_5 = int(self.row['new_confirmed_age_5'].item())
            if (type(self.row['new_confirmed_age_6'].item()) == str): self.new_confirmed_age_6 = int(self.row['new_confirmed_age_6'].item())
            if (type(self.row['new_confirmed_age_7'].item()) == str): self.new_confirmed_age_7 = int(self.row['new_confirmed_age_7'].item())
            if (type(self.row['cumulative_confirmed_age_0'].item()) == str): self.cumulative_confirmed_age_0 = int(self.row['cumulative_confirmed_age_0'].item())
            if (type(self.row['cumulative_confirmed_age_1'].item()) == str): self.cumulative_confirmed_age_1 = int(self.row['cumulative_confirmed_age_1'].item())
            if (type(self.row['cumulative_confirmed_age_2'].item()) == str): self.cumulative_confirmed_age_2 = int(self.row['cumulative_confirmed_age_2'].item())
            if (type(self.row['cumulative_confirmed_age_3'].item()) == str): self.cumulative_confirmed_age_3 = int(self.row['cumulative_confirmed_age_3'].item())
            if (type(self.row['cumulative_confirmed_age_4'].item()) == str): self.cumulative_confirmed_age_4 = int(self.row['cumulative_confirmed_age_4'].item())
            if (type(self.row['cumulative_confirmed_age_5'].item()) == str): self.cumulative_confirmed_age_5 = int(self.row['cumulative_confirmed_age_5'].item())
            if (type(self.row['cumulative_confirmed_age_6'].item()) == str): self.cumulative_confirmed_age_6 = int(self.row['cumulative_confirmed_age_6'].item())
            if (type(self.row['cumulative_confirmed_age_7'].item()) == str): self.cumulative_confirmed_age_7 = int(self.row['cumulative_confirmed_age_7'].item())

    def generateReport(self):
        file_path = r'./generated-report.txt'
        
        if not (self.dataExist): return
        
        with open(file_path, 'a+') as fp:
            fp.write(f'\n\n')
            fp.write(f'Covid data by Age for location - {self.location_key}: \n')
                        
            fp.write('There is no date. \n') if self.date == None else fp.write(f'date is {self.date}\n')
            fp.write('There is no location_key. \n') if self.location_key == None else fp.write(f'location_key is {self.location_key}\n')
            
            fp.write('There is no new_confirmed_age_0. \n') if self.new_confirmed_age_0 == None or self.new_confirmed_age_0 == 0 else fp.write(f'new_confirmed_age_0 is {math.ceil(self.new_confirmed_age_0)}\n')
            fp.write('There is no new_confirmed_age_1. \n') if self.new_confirmed_age_1 == None or self.new_confirmed_age_1 == 0 else fp.write(f'new_confirmed_age_1 is {math.ceil(self.new_confirmed_age_1)}\n')
            fp.write('There is no new_confirmed_age_2. \n') if self.new_confirmed_age_2 == None or self.new_confirmed_age_2 == 0 else fp.write(f'new_confirmed_age_2 is {math.ceil(self.new_confirmed_age_2)}\n')
            fp.write('There is no new_confirmed_age_3. \n') if self.new_confirmed_age_3 == None or self.new_confirmed_age_3 == 0 else fp.write(f'new_confirmed_age_3 is {math.ceil(self.new_confirmed_age_3)}\n')
            fp.write('There is no new_confirmed_age_4. \n') if self.new_confirmed_age_4 == None or self.new_confirmed_age_4 == 0 else fp.write(f'new_confirmed_age_4 is {math.ceil(self.new_confirmed_age_4)}\n')
            fp.write('There is no new_confirmed_age_5. \n') if self.new_confirmed_age_5 == None or self.new_confirmed_age_5 == 0 else fp.write(f'new_confirmed_age_5 is {math.ceil(self.new_confirmed_age_5)}\n')
            fp.write('There is no new_confirmed_age_6. \n') if self.new_confirmed_age_6 == None or self.new_confirmed_age_6 == 0 else fp.write(f'new_confirmed_age_6 is {math.ceil(self.new_confirmed_age_6)}\n')
            fp.write('There is no new_confirmed_age_7. \n') if self.new_confirmed_age_7 == None or self.new_confirmed_age_7 == 0 else fp.write(f'new_confirmed_age_7 is {math.ceil(self.new_confirmed_age_7)}\n')
            fp.write('There is no cumulative_confirmed_age_0. \n') if self.cumulative_confirmed_age_0 == None or self.cumulative_confirmed_age_0 == 0 else fp.write(f'cumulative_confirmed_age_0 is {math.ceil(self.cumulative_confirmed_age_0)}\n')
            fp.write('There is no cumulative_confirmed_age_1. \n') if self.cumulative_confirmed_age_1 == None or self.cumulative_confirmed_age_1 == 0 else fp.write(f'cumulative_confirmed_age_1 is {math.ceil(self.cumulative_confirmed_age_1)}\n')
            fp.write('There is no cumulative_confirmed_age_2. \n') if self.cumulative_confirmed_age_2 == None or self.cumulative_confirmed_age_2 == 0 else fp.write(f'cumulative_confirmed_age_2 is {math.ceil(self.cumulative_confirmed_age_2)}\n')
            fp.write('There is no cumulative_confirmed_age_3. \n') if self.cumulative_confirmed_age_3 == None or self.cumulative_confirmed_age_3 == 0 else fp.write(f'cumulative_confirmed_age_3 is {math.ceil(self.cumulative_confirmed_age_3)}\n')
            fp.write('There is no cumulative_confirmed_age_4. \n') if self.cumulative_confirmed_age_4 == None or self.cumulative_confirmed_age_4 == 0 else fp.write(f'cumulative_confirmed_age_4 is {math.ceil(self.cumulative_confirmed_age_4)}\n')
            fp.write('There is no cumulative_confirmed_age_5. \n') if self.cumulative_confirmed_age_5 == None or self.cumulative_confirmed_age_5 == 0 else fp.write(f'cumulative_confirmed_age_5 is {math.ceil(self.cumulative_confirmed_age_5)}\n')
            fp.write('There is no cumulative_confirmed_age_6. \n') if self.cumulative_confirmed_age_6 == None or self.cumulative_confirmed_age_6 == 0 else fp.write(f'cumulative_confirmed_age_6 is {math.ceil(self.cumulative_confirmed_age_6)}\n')
            fp.write('There is no cumulative_confirmed_age_7. \n') if self.cumulative_confirmed_age_7 == None or self.cumulative_confirmed_age_7 == 0 else fp.write(f'cumulative_confirmed_age_7 is {math.ceil(self.cumulative_confirmed_age_7)}\n')            


byAge = ByAge('IN')
# byAge = ByAge('US', '2022-08-01')

byAge.setData()
byAge.generateReport()
byAge.row