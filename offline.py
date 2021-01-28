import json

class Offline:

    def __init__(self, pm_two_five_file, pm_ten_file):
        self.pm_two_five_file = pm_two_five_file
        self.pm_ten_file = pm_ten_file

    def print_pm_two_five(self, pm_two_five):
        print(str.format("PM 2.5 {0}", pm_two_five))

    def print_pm_ten(self, pm_ten):
        print(str.format("PM 10 {0}", pm_ten))

    def write_pm_two_five(self, pm_two_five):
        with open(self.pm_two_five_file, 'a') as file:
            json.dump(pm_two_five, file)

    def write_pm_ten(self, pm_ten):
        with open(self.pm_ten_file, 'a') as file:
            json.dump(pm_ten, file)
