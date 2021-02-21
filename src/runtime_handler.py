from templates.new_patient import NewPatientFrame
from templates.common_data import CommonDataFrame

class RuntimeHandler():
    def __init__(self):
        print('Initializing RuntimeHandler...')
        self.index = 0
        self.parts = {
            'patient' : self.new_patient,
            'common' : self.common_data
        }
        #self.order = [part for part in self.parts]
        self.order = [
            'patient',
            'common'
        ]
        print('Order:')
        for idx,i in enumerate(self.order):
            print('\t',idx,':', i)

    def get_part(self, part):
        return self.parts.get(part, None)

    def set_new(self, part):
        print('Trying to set part:', part)
        new_part = self.get_part(part)
        new_part()
        return True

    def process(self, error=0):

        try:
            self.set_new(self.order[self.index])
            self.index += 1
            print('Processed...')
            return True
        except IndexError as ie:
            print('IndexError: Starting process from start again.')
            self.index = 0
            error += 1
            if not error > 3:
                self.process(error)

        return False
    
    def new_patient(self):
        new_patient_frame = NewPatientFrame(self)

    def common_data(self):
        common_data_frame = CommonDataFrame(self)