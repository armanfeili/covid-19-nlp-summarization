import pandas as pd

df_health = pd.read_csv("./health.csv", sep=',', on_bad_lines='skip', index_col=False, dtype='unicode')

class Health():
    
    row = None
    findLatest = False
    last_index_based_on_location_key = 0
    dataExist = True
    
    life_expectancy = None
    smoking_prevalence = None
    diabetes_prevalence = None
    infant_mortality_rate = None
    adult_male_mortality_rate = None
    adult_female_mortality_rate = None
    pollution_mortality_rate = None
    comorbidity_mortality_rate = None
    hospital_beds_per_1000 = None
    nurses_per_1000 = None
    physicians_per_1000 = None
    health_expenditure_usd = None
    out_of_pocket_health_expenditure_usd = None

    def __init__(self, location_key, date = None):
        self.location_key = location_key      
        pass
        
    def setData(self):        
        self.row = df_health.query(f'location_key == "{self.location_key}"')

        if self.row.empty: 
            print("Sorry... There is no data based on health by this location key.")
            self.dataExist = False
            return

        self.location_key = self.row['location_key'].item()                   

        if (type(self.row['life_expectancy'].item()) == str): self.life_expectancy = float(self.row['life_expectancy'].item())
        if (type(self.row['smoking_prevalence'].item()) == str): self.smoking_prevalence = float(self.row['smoking_prevalence'].item())
        if (type(self.row['diabetes_prevalence'].item()) == str): self.diabetes_prevalence = float(self.row['diabetes_prevalence'].item())
        if (type(self.row['infant_mortality_rate'].item()) == str): self.infant_mortality_rate = float(self.row['infant_mortality_rate'].item())
        if (type(self.row['adult_male_mortality_rate'].item()) == str): self.adult_male_mortality_rate = float(self.row['adult_male_mortality_rate'].item())
        if (type(self.row['adult_female_mortality_rate'].item()) == str): self.adult_female_mortality_rate = float(self.row['adult_female_mortality_rate'].item())
        if (type(self.row['pollution_mortality_rate'].item()) == str): self.pollution_mortality_rate = float(self.row['pollution_mortality_rate'].item())
        if (type(self.row['comorbidity_mortality_rate'].item()) == str): self.comorbidity_mortality_rate = float(self.row['comorbidity_mortality_rate'].item())
        if (type(self.row['hospital_beds_per_1000'].item()) == str): self.hospital_beds_per_1000 = float(self.row['hospital_beds_per_1000'].item())
        if (type(self.row['nurses_per_1000'].item()) == str): self.nurses_per_1000 = float(self.row['nurses_per_1000'].item())
        if (type(self.row['physicians_per_1000'].item()) == str): self.physicians_per_1000 = float(self.row['physicians_per_1000'].item())
        if (type(self.row['health_expenditure_usd'].item()) == str): self.health_expenditure_usd = float(self.row['health_expenditure_usd'].item())
        if (type(self.row['out_of_pocket_health_expenditure_usd'].item()) == str): self.out_of_pocket_health_expenditure_usd = float(self.row['out_of_pocket_health_expenditure_usd'].item())

    def generateReport(self):
        file_path = r'./generated-report.txt'
        
        if not (self.dataExist): return
        
        with open(file_path, 'a+') as fp:
            fp.write(f'\n\n')
            fp.write(f'Covid data based on the state of health for location - {self.location_key}: \n')
                        
            fp.write('There is no location_key. \n') if self.location_key == None else fp.write(f'location_key is {self.location_key}\n')
            
            fp.write('There is no life_expectancy. \n') if self.life_expectancy == None or self.life_expectancy == 0 else fp.write(f'life_expectancy is {self.life_expectancy}\n')
            fp.write('There is no smoking_prevalence. \n') if self.smoking_prevalence == None or self.smoking_prevalence == 0 else fp.write(f'smoking_prevalence is {self.smoking_prevalence}\n')
            fp.write('There is no diabetes_prevalence. \n') if self.diabetes_prevalence == None or self.diabetes_prevalence == 0 else fp.write(f'diabetes_prevalence is {self.diabetes_prevalence}\n')
            fp.write('There is no infant_mortality_rate. \n') if self.infant_mortality_rate == None or self.infant_mortality_rate == 0 else fp.write(f'infant_mortality_rate is {self.infant_mortality_rate}\n')
            fp.write('There is no adult_male_mortality_rate. \n') if self.adult_male_mortality_rate == None or self.adult_male_mortality_rate == 0 else fp.write(f'adult_male_mortality_rate is {self.adult_male_mortality_rate}\n')
            fp.write('There is no adult_female_mortality_rate. \n') if self.adult_female_mortality_rate == None or self.adult_female_mortality_rate == 0 else fp.write(f'adult_female_mortality_rate is {self.adult_female_mortality_rate}\n')
            fp.write('There is no pollution_mortality_rate. \n') if self.pollution_mortality_rate == None or self.pollution_mortality_rate == 0 else fp.write(f'pollution_mortality_rate is {self.pollution_mortality_rate}\n')
            fp.write('There is no comorbidity_mortality_rate. \n') if self.comorbidity_mortality_rate == None or self.comorbidity_mortality_rate == 0 else fp.write(f'comorbidity_mortality_rate is {self.comorbidity_mortality_rate}\n')
            fp.write('There is no hospital_beds_per_1000. \n') if self.hospital_beds_per_1000 == None or self.hospital_beds_per_1000 == 0 else fp.write(f'hospital_beds_per_1000 is {self.hospital_beds_per_1000}\n')
            fp.write('There is no nurses_per_1000. \n') if self.nurses_per_1000 == None or self.nurses_per_1000 == 0 else fp.write(f'nurses_per_1000 is {self.nurses_per_1000}\n')
            fp.write('There is no physicians_per_1000. \n') if self.physicians_per_1000 == None or self.physicians_per_1000 == 0 else fp.write(f'physicians_per_1000 is {self.physicians_per_1000}\n')
            fp.write('There is no health_expenditure_usd. \n') if self.health_expenditure_usd == None or self.health_expenditure_usd == 0 else fp.write(f'health_expenditure_usd is {self.health_expenditure_usd}\n')
            fp.write('There is no out_of_pocket_health_expenditure_usd. \n') if self.out_of_pocket_health_expenditure_usd == None or self.out_of_pocket_health_expenditure_usd == 0 else fp.write(f'out_of_pocket_health_expenditure_usd is {self.out_of_pocket_health_expenditure_usd}\n')

health = Health('US')

health.setData()
health.generateReport()
health.row