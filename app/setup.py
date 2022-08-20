class Start():
    
    country_code = None
    date = None
    
    alpha_2 = None
    alpha_3 = None
    country_name = None
    count_of_iteration = 0
        
    def __init__(self):
        
        self.country_code = (input("Please enter Alpha-2 Country Code OR press [Enter key] to see World Report:")).upper()
        
        if (self.country_code):
            if (len(self.country_code) == 2): self.alpha_2 = self.country_code
            elif (len(self.country_code) == 3): self.alpha_3 = self.country_code
            else: print('Country code should be 2 or 3 character. Please try again.')
            
            if(self.alpha_2):
                for dic in worldSymbols:
                    if(dic['alpha2'] == self.alpha_2.lower()):
                        self.count_of_iteration = self.count_of_iteration + 1
                        self.alpha_3 = dic['alpha3']
                        self.country_name = dic['name']

                if(self.count_of_iteration == 0): print('No such country code available! Please try again.')
                        
            elif(self.alpha_3):
                for dic in worldSymbols:
                    if(dic['alpha3'] == self.alpha_3.lower()):
                        self.count_of_iteration = self.count_of_iteration + 1
                        self.alpha_2 = dic['alpha2']
                        self.country_name = dic['name']

                if(self.count_of_iteration == 0): print('No such country code available! Please try again.')

        if not (self.country_code): self.country_code = 'OWID_WRL'
        if (self.country_code == 'OWID_WRL'):
            # just generate owid report 
            
        else:
            # generate full report

        print("country_codes is: " + country_codes)
        date = input("Please enter date OR press enter for the latest date:")
        print(f'Generating Report of Covid-19 for {self.country_name} ...')
        
        pass

start = Start()
start