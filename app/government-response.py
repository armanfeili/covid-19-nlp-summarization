import pandas as pd
import math

df_oxford_goverment_response = pd.read_csv("./oxford-government-response.csv", sep=',', on_bad_lines='skip', index_col=False, dtype='unicode')

class GovernmentResponse():
    
    row = None
    findLatest = False
    last_index_based_on_location_key = 0
    dataExist = True
    
    school_closing = None
    workplace_closing = None
    cancel_public_events = None
    restrictions_on_gatherings = None
    public_transport_closing = None
    stay_at_home_requirements = None
    restrictions_on_internal_movement = None
    international_travel_controls = None
    income_support = None
    debt_relief = None
    fiscal_measures = None
    international_support = None
    public_information_campaigns = None
    testing_policy = None
    contact_tracing = None
    emergency_investment_in_healthcare = None
    investment_in_vaccines = None
    facial_coverings = None
    vaccination_policy = None
    stringency_index = None
    
    
    
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
            self.last_index_based_on_location_key = df_oxford_goverment_response.query(f'location_key == "{self.location_key}"').index.max()
    
            if not(math.isnan(self.last_index_based_on_location_key)):
                self.row = df_oxford_goverment_response.iloc[self.last_index_based_on_location_key] 
            else:
                print("Sorry... There is no data based on government response by this location key.")
                self.dataExist = False
                return
            
            self.date = self.row['date']
            self.location_key = self.row['location_key']
            
            if (type(self.row['school_closing']) == str): self.school_closing = int(self.row['school_closing'])
            if (type(self.row['workplace_closing']) == str): self.workplace_closing = int(self.row['workplace_closing'])
            if (type(self.row['cancel_public_events']) == str): self.cancel_public_events = int(self.row['cancel_public_events'])
            if (type(self.row['restrictions_on_gatherings']) == str): self.restrictions_on_gatherings = int(self.row['restrictions_on_gatherings'])
            if (type(self.row['public_transport_closing']) == str): self.public_transport_closing = int(self.row['public_transport_closing'])
            if (type(self.row['stay_at_home_requirements']) == str): self.stay_at_home_requirements = int(self.row['stay_at_home_requirements'])
            if (type(self.row['restrictions_on_internal_movement']) == str): self.restrictions_on_internal_movement = int(self.row['restrictions_on_internal_movement'])
            if (type(self.row['international_travel_controls']) == str): self.international_travel_controls = int(self.row['international_travel_controls'])
            if (type(self.row['income_support']) == str): self.income_support = int(self.row['income_support'])
            if (type(self.row['debt_relief']) == str): self.debt_relief = int(self.row['debt_relief'])
            if (type(self.row['fiscal_measures']) == str): self.fiscal_measures = int(self.row['fiscal_measures'])
            if (type(self.row['international_support']) == str): self.international_support = int(self.row['international_support'])
            if (type(self.row['public_information_campaigns']) == str): self.public_information_campaigns = int(self.row['public_information_campaigns'])
            if (type(self.row['testing_policy']) == str): self.testing_policy = int(self.row['testing_policy'])
            if (type(self.row['contact_tracing']) == str): self.contact_tracing = int(self.row['contact_tracing'])
            if (type(self.row['emergency_investment_in_healthcare']) == str): self.emergency_investment_in_healthcare = int(self.row['emergency_investment_in_healthcare'])
            if (type(self.row['investment_in_vaccines']) == str): self.investment_in_vaccines = int(self.row['investment_in_vaccines'])
            if (type(self.row['facial_coverings']) == str): self.facial_coverings = int(self.row['facial_coverings'])
            if (type(self.row['vaccination_policy']) == str): self.vaccination_policy = int(self.row['vaccination_policy'])
            if (type(self.row['stringency_index']) == str): self.stringency_index = float(self.row['stringency_index'])
           
        else:
            self.row = df_oxford_goverment_response.query(f'location_key == "{self.location_key}" & date == "{self.date}"')

            if self.row.empty: 
                print("Sorry... There is no data based on government response by this location key.")
                self.dataExist = False
                return


            self.date = self.row['date'].item()
            self.location_key = self.row['location_key'].item()                   
            
            if (type(self.row['school_closing'].item()) == str): self.school_closing = int(self.row['school_closing'].item())
            if (type(self.row['workplace_closing'].item()) == str): self.workplace_closing = int(self.row['workplace_closing'].item())
            if (type(self.row['cancel_public_events'].item()) == str): self.cancel_public_events = int(self.row['cancel_public_events'].item())
            if (type(self.row['restrictions_on_gatherings'].item()) == str): self.restrictions_on_gatherings = int(self.row['restrictions_on_gatherings'].item())
            if (type(self.row['public_transport_closing'].item()) == str): self.public_transport_closing = int(self.row['public_transport_closing'].item())
            if (type(self.row['stay_at_home_requirements'].item()) == str): self.stay_at_home_requirements = int(self.row['stay_at_home_requirements'].item())
            if (type(self.row['restrictions_on_internal_movement'].item()) == str): self.restrictions_on_internal_movement = int(self.row['restrictions_on_internal_movement'].item())
            if (type(self.row['international_travel_controls'].item()) == str): self.international_travel_controls = int(self.row['international_travel_controls'].item())
            if (type(self.row['income_support'].item()) == str): self.income_support = int(self.row['income_support'].item())
            if (type(self.row['debt_relief'].item()) == str): self.debt_relief = int(self.row['debt_relief'].item())
            if (type(self.row['fiscal_measures'].item()) == str): self.fiscal_measures = int(self.row['fiscal_measures'].item())
            if (type(self.row['international_support'].item()) == str): self.international_support = int(self.row['international_support'].item())
            if (type(self.row['public_information_campaigns'].item()) == str): self.public_information_campaigns = int(self.row['public_information_campaigns'].item())
            if (type(self.row['testing_policy'].item()) == str): self.testing_policy = int(self.row['testing_policy'].item())
            if (type(self.row['contact_tracing'].item()) == str): self.contact_tracing = int(self.row['contact_tracing'].item())
            if (type(self.row['emergency_investment_in_healthcare'].item()) == str): self.emergency_investment_in_healthcare = int(self.row['emergency_investment_in_healthcare'].item())
            if (type(self.row['investment_in_vaccines'].item()) == str): self.investment_in_vaccines = int(self.row['investment_in_vaccines'].item())
            if (type(self.row['facial_coverings'].item()) == str): self.facial_coverings = int(self.row['facial_coverings'].item())
            if (type(self.row['vaccination_policy'].item()) == str): self.vaccination_policy = int(self.row['vaccination_policy'].item())
            if (type(self.row['stringency_index'].item()) == str): self.stringency_index = float(self.row['stringency_index'].item())

    def generateReport(self):
        file_path = r'./generated-report.txt'
        
        if not (self.dataExist): return
        
        with open(file_path, 'a+') as fp:
            fp.write(f'\n\n')
            fp.write(f'Covid data based on government response for location - {self.location_key}: \n')
                        
            fp.write('There is no date. \n') if self.date == None else fp.write(f'date is {self.date}\n')
            fp.write('There is no location_key. \n') if self.location_key == None else fp.write(f'location_key is {self.location_key}\n')
                    
            if (self.school_closing == None) :fp.write('There is no school_closing reported.\n')
            elif(self.school_closing == 0): fp.write(f'No restriction reported for school_closing on this date.\n')
            elif(self.school_closing == 1): fp.write(f'school_closing is recommended.\n')
            elif(self.school_closing == 2): fp.write(f'school_closing is required at some levels.\n')
            elif(self.school_closing == 3): fp.write(f'school_closing is required at all levels.\n')

            if (self.workplace_closing == None) :fp.write('There is no workplace_closing reported.\n')
            elif(self.workplace_closing == 0): fp.write(f'No restriction reported for workplace_closing on this date.\n')
            elif(self.workplace_closing == 1): fp.write(f'workplace_closing is recommended.\n')
            elif(self.workplace_closing == 2): fp.write(f'workplace_closing is required at some levels.\n')
            elif(self.workplace_closing == 3): fp.write(f'workplace_closing is required at all levels.\n')

            if (self.cancel_public_events == None) :fp.write('There is no cancel_public_events reported.\n')
            elif(self.cancel_public_events == 0): fp.write(f'No restriction reported for cancel_public_events on this date.\n')
            elif(self.cancel_public_events == 1): fp.write(f'cancel_public_events is recommended.\n')
            elif(self.cancel_public_events == 2): fp.write(f'cancel_public_events is required at some levels.\n')
            elif(self.cancel_public_events == 3): fp.write(f'cancel_public_events is required at all levels.\n')

            if (self.restrictions_on_gatherings == None) :fp.write('There is no restrictions_on_gatherings reported.\n')
            elif(self.restrictions_on_gatherings == 0): fp.write(f'No restriction reported for restrictions_on_gatherings on this date.\n')
            elif(self.restrictions_on_gatherings == 1): fp.write(f'restrictions_on_gatherings is recommended.\n')
            elif(self.restrictions_on_gatherings == 2): fp.write(f'restrictions_on_gatherings is required at some levels.\n')
            elif(self.restrictions_on_gatherings == 3): fp.write(f'restrictions_on_gatherings is required at all levels.\n')

            if (self.public_transport_closing == None) :fp.write('There is no public_transport_closing reported.\n')
            elif(self.public_transport_closing == 0): fp.write(f'No restriction reported for public_transport_closing on this date.\n')
            elif(self.public_transport_closing == 1): fp.write(f'public_transport_closing is recommended.\n')
            elif(self.public_transport_closing == 2): fp.write(f'public_transport_closing is required at some levels.\n')
            elif(self.public_transport_closing == 3): fp.write(f'public_transport_closing is required at all levels.\n')

            if (self.stay_at_home_requirements == None) :fp.write('There is no stay_at_home_requirements reported.\n')
            elif(self.stay_at_home_requirements == 0): fp.write(f'No restriction reported for stay_at_home_requirements on this date.\n')
            elif(self.stay_at_home_requirements == 1): fp.write(f'stay_at_home_requirements is recommended.\n')
            elif(self.stay_at_home_requirements == 2): fp.write(f'stay_at_home_requirements is required at some levels.\n')
            elif(self.stay_at_home_requirements == 3): fp.write(f'stay_at_home_requirements is required at all levels.\n')

            if (self.restrictions_on_internal_movement == None) :fp.write('There is no restrictions_on_internal_movement reported.\n')
            elif(self.restrictions_on_internal_movement == 0): fp.write(f'No restriction reported for restrictions_on_internal_movement on this date.\n')
            elif(self.restrictions_on_internal_movement == 1): fp.write(f'restrictions_on_internal_movement is recommended.\n')
            elif(self.restrictions_on_internal_movement == 2): fp.write(f'restrictions_on_internal_movement is required at some levels.\n')
            elif(self.restrictions_on_internal_movement == 3): fp.write(f'restrictions_on_internal_movement is required at all levels.\n')

            if (self.international_travel_controls == None) :fp.write('There is no international_travel_controls reported.\n')
            elif(self.international_travel_controls == 0): fp.write(f'No restriction reported for international_travel_controls on this date.\n')
            elif(self.international_travel_controls == 1): fp.write(f'international_travel_controls is recommended.\n')
            elif(self.international_travel_controls == 2): fp.write(f'international_travel_controls is required at some levels.\n')
            elif(self.international_travel_controls == 3): fp.write(f'international_travel_controls is required at all levels.\n')

            #######################
            ## Check differently ##
            #######################
            
            # what is income_support ?
            if (self.income_support == None) :fp.write('There is no income_support reported.\n')
            elif(self.income_support == 0): fp.write(f'No restriction reported for income_support on this date.\n')
            elif(self.income_support == 1): fp.write(f'income_support is recommended.\n')
            elif(self.income_support == 2): fp.write(f'income_support is required at some levels.\n')
            elif(self.income_support == 3): fp.write(f'income_support is required at all levels.\n')

            # what is income_support ?
            if (self.debt_relief == None) :fp.write('There is no debt_relief reported.\n')
            elif(self.debt_relief == 0): fp.write(f'No restriction reported for debt_relief on this date.\n')
            elif(self.debt_relief == 1): fp.write(f'debt_relief is recommended.\n')
            elif(self.debt_relief == 2): fp.write(f'debt_relief is required at some levels.\n')
            elif(self.debt_relief == 3): fp.write(f'debt_relief is required at all levels.\n')

            if (self.fiscal_measures == None) :fp.write('There is no fiscal_measures reported.\n')
            elif(self.fiscal_measures == 0): fp.write(f'There is no fiscal_measures reported.\n')
            else: fp.write(f'The fiscal_measures is :{self.fiscal_measures}.\n')

            if (self.international_support == None) :fp.write('There is no international_support reported.\n')
            elif(self.international_support == 0): fp.write(f'There is no international_support reported.\n')
            else: fp.write(f'The international_support is :{self.international_support}.\n')


            if (self.public_information_campaigns == None) :fp.write('There is no public_information_campaigns reported.\n')
            elif(self.public_information_campaigns == 0): fp.write(f'There is no public_information_campaigns reported.\n')
            else: fp.write(f'The number of public_information_campaigns is : {self.public_information_campaigns}.\n')
                
            if (self.testing_policy == None) :fp.write('There is no testing_policy reported.\n')
            elif(self.testing_policy == 0): fp.write(f'There is no testing_policy reported.\n')
            else: fp.write(f'The number of testing_policy is : {self.testing_policy}.\n')

            if (self.contact_tracing == None) :fp.write('There is no contact_tracing reported.\n')
            elif(self.contact_tracing == 0): fp.write(f'There is no contact_tracing reported.\n')
            else: fp.write(f'The number of contact_tracing is : {self.contact_tracing}.\n')

            if (self.emergency_investment_in_healthcare == None) :fp.write('There is no emergency_investment_in_healthcare reported.\n')
            elif(self.emergency_investment_in_healthcare == 0): fp.write(f'There is no emergency_investment_in_healthcare reported.\n')
            else: fp.write(f'The amount of emergency_investment_in_healthcare is : {self.emergency_investment_in_healthcare}.\n')
            
            if (self.investment_in_vaccines == None) :fp.write('There is no investment_in_vaccines reported.\n')
            elif(self.investment_in_vaccines == 0): fp.write(f'There is no investment_in_vaccines reported.\n')
            else: fp.write(f'The amount of investment_in_vaccines is : {self.investment_in_vaccines}.\n')

            if (self.facial_coverings == None) :fp.write('There is no facial_coverings reported.\n')
            elif(self.facial_coverings == 0): fp.write(f'There is no facial_coverings reported.\n')
            else: fp.write(f'The number of facial_coverings is : {self.facial_coverings}.\n')

            if (self.vaccination_policy == None) :fp.write('There is no vaccination_policy reported.\n')
            elif(self.vaccination_policy == 0): fp.write(f'There is no vaccination_policy reported.\n')
            else: fp.write(f'The number of vaccination_policy is : {self.vaccination_policy}.\n')

            if (self.stringency_index == None) :fp.write('There is no stringency_index reported.\n')
            elif(self.stringency_index == 0): fp.write(f'There is no stringency_index reported.\n')
            else: fp.write(f'The percentage of stringency_index is : {self.stringency_index}.\n')


governmentResponse = GovernmentResponse('US')
# governmentResponse = GovernmentResponse('US', '2022-07-07')

governmentResponse.setData()
governmentResponse.generateReport()
governmentResponse.row