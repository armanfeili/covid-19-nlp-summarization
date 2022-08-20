import pandas as pd
import math

df_owid = pd.read_csv("./owid-covid-data.csv")

class OwidData():
        
    row = None
    worldRow = None
    prevRow = None
    last_index_based_on_iso_code = 0
    last_world_index = 0
    findLatest = False
    value = None
    
    world_total_cases = None
    world_new_cases = None
    world_total_deaths = None
    world_new_deaths = None
    world_total_vaccinations = None
    world_population = None
    
    world_total_cases_percentage = None
    world_new_cases_percentage = None
    world_total_deaths_percentage = None
    world_new_deaths_percentage = None
    world_total_vaccinations_percentage = None
    
    total_cases_percentage = None
    new_cases_percentage = None
    total_deaths_percentage = None
    new_deaths_percentage = None
    total_vaccinations_percentage = None
    

    iso_code = None
    continent = None
    location = None
    date = None
    total_cases = None
    new_cases = None
    new_cases_smoothed = None
    total_deaths = None
    new_deaths = None
    new_deaths_smoothed = None
    reproduction_rate = None
    icu_patients = None
    hosp_patients = None
    weekly_icu_admissions = None
    weekly_hosp_admissions = None
    total_tests = None
    new_tests = None
    new_tests_smoothed = None
    positive_rate = None
    tests_per_case = None
    tests_units = None
    total_vaccinations = None
    people_vaccinated = None
    people_fully_vaccinated = None
    total_boosters = None
    new_vaccinations = None
    new_vaccinations_smoothed = None
    new_people_vaccinated_smoothed = None
    stringency_index = None
    population = None
    hospital_beds_per_thousand = None
    life_expectancy = None
    human_development_index = None
    excess_mortality = None
    
    infection_risk = None
    case_fatality_rate = None
    test_percentage = None
    vaccination_percentage = None
    average_number_of_vaccination_per_person = None
    
    def __init__(self, iso_code, date = None):
        self.iso_code = iso_code
        self.date = date
        
        if not (self.date):
            self.findLatest = True
            print("Available Latest Report, Loading...")
        else:
            print("Report for the selected date : " + self.date)
        pass
             
    def isNull(self, value = None):
        if (type(value) == str):
            value = float(value)
            return math.isnan(value)
        
        elif (type(value) == float):
            return math.isnan(value)
        
    def convertNumber(self, value = None):
        if (type(value) == str):
            value = float(value)
            return value
        
        elif (type(value) == float):
            return value
        
    def getLastReportedValue(self, key):
        if (type(self.row[f'{key}']) == str): self.value = float(self.row[f'{key}'])
        elif (type(self.row[f'{key}']) == float): self.value = self.row[f'{key}']
        
        if (math.isnan(self.value)):
            k = 1
            
            while(True):                    
                self.prevRow = df_owid.iloc[df_owid.query(f'iso_code == "{self.iso_code}"').index.max() - k]
                k = k + 1
                
                if (type(self.prevRow[f'{key}']) == str): self.value = float(self.prevRow[f'{key}'])
                elif (type(self.prevRow[f'{key}']) == float): self.value = self.prevRow[f'{key}']
                
                if not (math.isnan(self.value)): 
                    break
                if(k == 100):
                    return None
            return self.value
        else:
            return self.value
        
    def additionalData(self):
        if(self.population):
            # INFECTION RISK:
            # Total Number of covid-19 cases divided by Total Population since the beginning of outbreak
            if (self.total_cases): self.infection_risk = round((self.total_cases / self.population) * 100 , 2)

            # CASE FATALITY RATE (CFR):
            # Total Number of Deaths due to Covid-19 divided by Total Number of confirmed cases since the beginning of outbreak (It shows that how lethal covid-19 is in any country)
            if (self.total_deaths): self.case_fatality_rate = round((self.total_deaths / self.total_cases) * 100, 2)

            # TEST PERCENTAGE:
            # Total number of tests divided by total population
            if (self.total_tests): self.test_percentage = round((self.total_tests / self.population) * 100, 2)

            # VACCINATION PERCENTAGE
            # Total number of vaccinated people divided by total population
            if (self.people_vaccinated): self.vaccination_percentage = round((self.people_vaccinated / self.population) * 100, 2)

            # AVERAGE NUMBER OF TIMES A PERSON GOT VACCINATED
            # Total number of vaccination divided by total population
            if (self.total_vaccinations): self.average_number_of_vaccination_per_person = round(self.total_vaccinations / self.population, 2)

            self.last_world_index = df_owid.query(f'iso_code == "OWID_WRL"').index.max()

            if(self.last_world_index != 0):
                self.worldRow = df_owid.iloc[self.last_world_index]

                self.world_total_cases = self.worldRow['total_cases']
                self.world_new_cases = self.worldRow['new_cases']
                self.world_total_deaths = self.worldRow['total_deaths']
                self.world_new_deaths = self.worldRow['new_deaths']
                self.world_total_vaccinations = self.worldRow['total_vaccinations']
                self.world_population = self.worldRow['population']
        
    def setData(self):        

        if (self.findLatest == False):
            self.row = df_owid.query(f'iso_code == "{self.iso_code}" & date == "{self.date}"')
            
            print(self.row['population'].item())
            print(type(self.row['population'].item()))
            
            self.continent = self.row['continent'].item()
            self.location = self.row['location'].item()
            if not (self.isNull(self.row['total_cases'].item())): self.total_cases = self.convertNumber(self.row['total_cases'].item())
            if not (self.isNull(self.row['new_cases'].item())): self.new_cases = self.convertNumber(self.row['new_cases'].item())
            if not (self.isNull(self.row['new_cases_smoothed'].item())): self.new_cases_smoothed = self.convertNumber(self.row['new_cases_smoothed'].item())
            if not (self.isNull(self.row['total_deaths'].item())): self.total_deaths = self.convertNumber(self.row['total_deaths'].item())
            if not (self.isNull(self.row['new_deaths'].item())): self.new_deaths = self.convertNumber(self.row['new_deaths'].item())
            if not (self.isNull(self.row['new_deaths_smoothed'].item())): self.new_deaths_smoothed = self.convertNumber(self.row['new_deaths_smoothed'].item())
            if not (self.isNull(self.row['reproduction_rate'].item())): self.reproduction_rate =self.convertNumber(self.row['reproduction_rate'].item())
            if not (self.isNull(self.row['icu_patients'].item())): self.icu_patients = self.convertNumber(self.row['icu_patients'].item())
            if not (self.isNull(self.row['hosp_patients'].item())): self.hosp_patients = self.convertNumber(self.row['hosp_patients'].item())
            if not (self.isNull(self.row['total_tests'].item())): self.total_tests = self.convertNumber(self.row['total_tests'].item())
            if not (self.isNull(self.row['new_tests'].item())): self.new_tests = self.convertNumber(self.row['new_tests'].item())
            if not (self.isNull(self.row['new_tests_smoothed'].item())): self.new_tests_smoothed = self.convertNumber(self.row['new_tests_smoothed'].item())
            if not (self.isNull(self.row['positive_rate'].item())): self.positive_rate = self.convertNumber(self.row['positive_rate'].item())
            if not (self.isNull(self.row['tests_per_case'].item())): self.tests_per_case = self.convertNumber(self.row['tests_per_case'].item())
            if not (self.isNull(self.row['total_vaccinations'].item())): self.total_vaccinations = self.convertNumber(self.row['total_vaccinations'].item())
            if not (self.isNull(self.row['people_vaccinated'].item())): self.people_vaccinated = self.convertNumber(self.row['people_vaccinated'].item())
            if not (self.isNull(self.row['people_fully_vaccinated'].item())): self.people_fully_vaccinated = self.convertNumber(self.row['people_fully_vaccinated'].item())
            if not (self.isNull(self.row['total_boosters'].item())): self.total_boosters = self.convertNumber(self.row['total_boosters'].item())
            if not (self.isNull(self.row['new_vaccinations'].item())): self.new_vaccinations = self.convertNumber(self.row['new_vaccinations'].item())
            if not (self.isNull(self.row['new_vaccinations_smoothed'].item())): self.new_vaccinations_smoothed = self.convertNumber(self.row['new_vaccinations_smoothed'].item())
            if not (self.isNull(self.row['new_people_vaccinated_smoothed'].item())): self.new_people_vaccinated_smoothed = self.convertNumber(self.row['new_people_vaccinated_smoothed'].item())
            if not (self.isNull(self.row['stringency_index'].item())): self.stringency_index = self.convertNumber(self.row['stringency_index'].item())
            if not (self.isNull(self.row['population'].item())): self.population = self.convertNumber(self.row['population'].item())
            if not (self.isNull(self.row['hospital_beds_per_thousand'].item())): self.hospital_beds_per_thousand = self.convertNumber(self.row['hospital_beds_per_thousand'].item())
            if not (self.isNull(self.row['life_expectancy'].item())): self.life_expectancy = self.convertNumber(self.row['life_expectancy'].item())
            if not (self.isNull(self.row['human_development_index'].item())): self.human_development_index = self.convertNumber(self.row['human_development_index'].item())
            if not (self.isNull(self.row['excess_mortality'].item())): self.excess_mortality = self.convertNumber(self.row['excess_mortality'].item())
            
            self.additionalData()

        elif (self.findLatest == True):
            self.last_index_based_on_iso_code = df_owid.query(f'iso_code == "{self.iso_code}"').index.max()
            
            if(self.last_index_based_on_iso_code != 0):
                self.row = df_owid.iloc[self.last_index_based_on_iso_code]
            else:
                print("Sorry... No index with this ISO code.")
                return

            self.continent = self.row['continent']
            self.location = self.row['location']
            self.date = self.row['date']
            
            self.total_cases = self.getLastReportedValue('total_cases')
            self.new_cases = self.getLastReportedValue('new_cases')
            self.new_cases_smoothed = self.getLastReportedValue('new_cases_smoothed')
            self.total_deaths = self.getLastReportedValue('total_deaths')
            self.new_deaths = self.getLastReportedValue('new_deaths')
            self.new_deaths_smoothed = self.getLastReportedValue('new_deaths_smoothed')
            self.reproduction_rate = self.getLastReportedValue('reproduction_rate')
            self.icu_patients = self.getLastReportedValue('icu_patients')
            self.hosp_patients = self.getLastReportedValue('hosp_patients')
            self.total_tests = self.getLastReportedValue('total_tests')
            self.new_tests = self.getLastReportedValue('new_tests')
            self.new_tests_smoothed = self.getLastReportedValue('new_tests_smoothed')
            self.positive_rate = self.getLastReportedValue('positive_rate')
            self.tests_per_case = self.getLastReportedValue('tests_per_case')
            self.total_vaccinations = self.getLastReportedValue('total_vaccinations')
            self.people_vaccinated = self.getLastReportedValue('people_vaccinated')
            self.people_fully_vaccinated = self.getLastReportedValue('people_fully_vaccinated')
            self.total_boosters = self.getLastReportedValue('total_boosters')
            self.new_vaccinations = self.getLastReportedValue('new_vaccinations')
            self.new_vaccinations_smoothed = self.getLastReportedValue('new_vaccinations_smoothed')
            self.new_people_vaccinated_smoothed = self.getLastReportedValue('new_people_vaccinated_smoothed')
            self.stringency_index = self.getLastReportedValue('stringency_index')
            self.population = self.getLastReportedValue('population')
            self.hospital_beds_per_thousand = self.getLastReportedValue('hospital_beds_per_thousand')
            self.life_expectancy = self.getLastReportedValue('life_expectancy')
            self.human_development_index = self.getLastReportedValue('human_development_index')
            self.excess_mortality = self.getLastReportedValue('excess_mortality')
            
            self.additionalData()
      
        print('All Owid data has been set!')
        
    def generateReport(self):
        file_path = r'../reports/generated-report.txt'
        open(file_path, 'w').close() # clear file first.
        
        if not(self.iso_code == 'OWID_WRL'):

            if (self.world_population and self.population):
                if not (self.world_total_cases == None): self.world_total_cases_percentage = round(math.ceil(float(self.world_total_cases)) / math.ceil(float(self.world_population)) * 100, 3)
                if not (self.world_new_cases == None): self.world_new_cases_percentage = round(math.ceil(float(self.world_new_cases)) / math.ceil(float(self.world_population)) * 100, 3)
                if not (self.world_total_deaths == None): self.world_total_deaths_percentage = round(math.ceil(float(self.world_total_deaths)) / math.ceil(float(self.world_population)) * 100, 3)
                if not (self.world_new_deaths == None): self.world_new_deaths_percentage = round(math.ceil(float(self.world_new_deaths)) / math.ceil(float(self.world_population)) * 100, 3)
                if not (self.world_total_vaccinations == None): self.world_total_vaccinations_percentage = round(math.ceil(float(self.world_total_vaccinations)) / math.ceil(float(self.world_population)), 3)
                
                if not (self.total_cases == None): self.total_cases_percentage = round(math.ceil(float(self.total_cases)) / math.ceil(float(self.population)) * 100, 3)
                if not (self.new_cases == None): self.new_cases_percentage = round(math.ceil(float(self.new_cases)) / math.ceil(float(self.population)) * 100, 3)
                if not (self.total_deaths == None): self.total_deaths_percentage = round(math.ceil(float(self.total_deaths)) / math.ceil(float(self.population)) * 100, 3)
                if not (self.new_deaths == None): self.new_deaths_percentage = round(math.ceil(float(self.new_deaths)) / math.ceil(float(self.population)) * 100, 3)
                if not (self.total_vaccinations == None): self.total_vaccinations_percentage = round(math.ceil(float(self.total_vaccinations)) / math.ceil(float(self.population)), 3)
            
        with open(file_path, 'a+') as fp:
            if (self.date):
                fp.write(f'Here is comprehensive covid-19 report in {self.location} on date: {self.date}: \n')
            else:
                fp.write(f'Here is the latest covid-19 report in {self.location}: \n')
            fp.write('\n')
            
            fp.write(f'Due to the difference in reporting times between states, territories and the federal government, it can be difficult to get a current picture of the pandemic in {self.location}. \n')
            fp.write(f'Here we have brought together data on cases, deaths, hospitalisations and vaccinations.\n')

            if self.total_cases == None : fp.write('')
            else: 
                fp.write(f'As the latest data suggests, {math.ceil(self.total_cases)} total cases are reported.')
                if (self.world_total_cases_percentage and self.total_cases_percentage):
                    if (self.world_total_cases_percentage > self.total_cases_percentage):
                        fp.write(f'Additionally, in comparison to the world data, {self.location} has less infection rate, which is a good news!')
                    elif (self.world_total_cases_percentage < self.total_cases_percentage):
                        fp.write(f'Additionally, in comparison to the world data, unfortunately {self.location} has more infection rate.')
                    elif (self.world_total_cases_percentage == self.total_cases_percentage):
                        fp.write(f'Additionally, in comparison to the world data, {self.location} has equal infection rate to the world.')
                
            if self.new_cases == None : fp.write('')
            else: 
                fp.write(f'Not to mention that the new cases that is reported is something around {math.ceil(self.new_cases)}')
                
                if (self.world_new_cases_percentage and self.new_cases_percentage):
                    if (self.world_new_cases_percentage > self.new_cases_percentage):
                        fp.write(f'In comparison to world data, {self.location} has less new case rate, which is the bright side.')
                    elif (self.world_new_cases_percentage < self.new_cases_percentage):
                        fp.write(f'In comparison to world data, {self.location} has more new case rate.')
                    elif (self.world_new_cases_percentage == self.new_cases_percentage):
                        fp.write(f'In comparison to world data, {self.location} has equal new case rate to the world.')
                    
            # if self.new_cases_smoothed == None : fp.write('There is no new_cases_smoothed. ')
            # else: fp.write(f'new_cases_smoothed is: {math.ceil(self.new_cases_smoothed)}')
            
            if self.total_deaths == None : fp.write('There is no total_deaths. ')
            else: 
                fp.write(f'The other most frequently data reported is the total deaths that up to this point the number is: {math.ceil(self.total_deaths)}')
                if (self.world_total_deaths_percentage and self.total_deaths_percentage):                
                    if (self.world_total_deaths_percentage > self.total_deaths_percentage):
                        fp.write(f'In comparison to world data, {self.location} has less death rate.')
                    elif (self.world_total_deaths_percentage < self.total_deaths_percentage):
                        fp.write(f'In comparison to world data, {self.location} has more death rate.')
                    elif (self.world_total_deaths_percentage == self.total_deaths_percentage):
                        fp.write(f'In comparison to world data, {self.location} has equal death rate to the world.')
                    
            if self.new_deaths == None : fp.write('There is no new_deaths. ')
            else: 
                fp.write(f'new_deaths is: {math.ceil(self.new_deaths)}')
                if (self.world_new_deaths_percentage and self.new_deaths_percentage):                
                    if (self.world_new_deaths_percentage > self.new_deaths_percentage):
                        fp.write(f'In comparison to world data, {self.location} has less new death rate.')
                    elif (self.world_new_deaths_percentage < self.new_deaths_percentage):
                        fp.write(f'In comparison to world data, {self.location} has more new death rate.')
                    elif (self.world_new_deaths_percentage == self.new_deaths_percentage):
                        fp.write(f'In comparison to world data, {self.location} has equal new death rate to the world.')
                    
            if self.new_deaths_smoothed == None : fp.write('There is no new_deaths_smoothed. ')
            else: fp.write(f'new_deaths_smoothed is: {math.ceil(self.new_deaths_smoothed)}')
            if self.reproduction_rate == None : fp.write('There is no reproduction_rate. ')
            else: fp.write(f'reproduction_rate is: {math.ceil(self.reproduction_rate)}')
            if self.icu_patients == None : fp.write('There is no icu_patients. ')
            else: fp.write(f'icu_patients is: {math.ceil(self.icu_patients)}')
            if self.hosp_patients == None : fp.write('There is no hosp_patients. ')
            else: fp.write(f'hosp_patients is: {math.ceil(self.hosp_patients)}')
            if self.total_tests == None : fp.write('There is no total_tests. ')
            else: fp.write(f'total_tests is: {math.ceil(self.total_tests)}')
            if self.new_tests == None : fp.write('There is no new_tests. ')
            else: fp.write(f'new_tests is: {math.ceil(self.new_tests)}')
            if self.new_tests_smoothed == None : fp.write('There is no new_tests_smoothed. ')
            else: fp.write(f'new_tests_smoothed is: {math.ceil(self.new_tests_smoothed)}')
            if self.positive_rate == None : fp.write('There is no positive_rate. ')
            else: fp.write(f'positive_rate is: {math.ceil(self.positive_rate)}')
            if self.tests_per_case == None : fp.write('There is no tests_per_case. ')
            else: fp.write(f'tests_per_case is: {math.ceil(self.tests_per_case)}')
            if self.total_vaccinations == None : fp.write('There is no total_vaccinations. ')
            else: 
                fp.write(f'total_vaccinations is: {math.ceil(self.total_vaccinations)}')
                if (self.world_total_vaccinations_percentage and self.total_vaccinations_percentage):                
                    if (self.world_total_vaccinations_percentage > self.total_vaccinations_percentage):
                        fp.write(f'In comparison to world data, {self.location} has less vaccination rate.')
                    elif (self.world_total_vaccinations_percentage < self.total_vaccinations_percentage):
                        fp.write(f'In comparison to world data, {self.location} has more vaccination rate.')
                    elif (self.world_total_vaccinations_percentage == self.total_vaccinations_percentage):
                        fp.write(f'In comparison to world data, {self.location} has equal vaccination rate to the world.')
                    
            if self.people_vaccinated == None : fp.write('There is no people_vaccinated. ')
            else: fp.write(f'people_vaccinated is: {math.ceil(self.people_vaccinated)}')
            if self.people_fully_vaccinated == None : fp.write('There is no people_fully_vaccinated. ')
            else: fp.write(f'people_fully_vaccinated is: {math.ceil(self.people_fully_vaccinated)}')
            if self.total_boosters == None : fp.write('There is no total_boosters. ')
            else: fp.write(f'total_boosters is: {math.ceil(self.total_boosters)}')
            if self.new_vaccinations == None : fp.write('There is no new_vaccinations. ')
            else: fp.write(f'new_vaccinations is: {math.ceil(self.new_vaccinations)}')
            if self.new_vaccinations_smoothed == None : fp.write('There is no new_vaccinations_smoothed. ')
            else: fp.write(f'new_vaccinations_smoothed is: {math.ceil(self.new_vaccinations_smoothed)}')
            if self.new_people_vaccinated_smoothed == None : fp.write('There is no new_people_vaccinated_smoothed. ')
            else: fp.write(f'new_people_vaccinated_smoothed is: {math.ceil(self.new_people_vaccinated_smoothed)}')
            if self.stringency_index == None : fp.write('There is no stringency_index. ')
            else: fp.write(f'stringency_index is: {self.stringency_index}')
            if self.population == None : fp.write('There is no population. ')
            else: fp.write(f'population is: {math.ceil(self.population)}')
            if self.hospital_beds_per_thousand == None : fp.write('There is no hospital_beds_per_thousand. ')
            else: fp.write(f'hospital_beds_per_thousand is: {math.ceil(self.hospital_beds_per_thousand)}')
            if self.life_expectancy == None : fp.write('There is no life_expectancy. ')
            else: fp.write(f'life_expectancy is: {self.life_expectancy}')
            if self.human_development_index == None : fp.write('There is no human_development_index. ')
            else: fp.write(f'human_development_index is: {self.human_development_index}')
            if self.excess_mortality == None : fp.write('There is no excess_mortality. ')
            else: fp.write(f'excess_mortality is: {self.excess_mortality}')

            fp.write('Some additioanl data is as follows: ')

            if self.infection_risk == None : fp.write('There is no self.infection_risk. ')
            else: fp.write(f'infection_risk is: {self.infection_risk}')

            if self.case_fatality_rate == None : fp.write('There is no self.case_fatality_rate. ')
            else: fp.write(f'case_fatality_rate is: {self.case_fatality_rate}')

            if self.test_percentage == None : fp.write('There is no self.test_percentage. ')
            else: fp.write(f'test_percentage is: {self.test_percentage}')

            if self.vaccination_percentage == None : fp.write('There is no self.vaccination_percentage. ')
            else: fp.write(f'vaccination_percentage is: {self.vaccination_percentage}')

            if self.average_number_of_vaccination_per_person == None : fp.write('There is no self.average_number_of_vaccination_per_person. ')
            else: fp.write(f'average_number_of_vaccination_per_person is: {self.average_number_of_vaccination_per_person}')
            
        
        print('All Owid reports have been written!')
            
# owid = OwidData('IRN')
owid = OwidData('OWID_WRL')
# owid = OwidData('IRN','2022-01-09')

owid.setData()
owid.generateReport()
