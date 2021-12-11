import openpyxl as op
import pandas as pd
import random as rd



class GenerateData:
        __DAYS = {
                1:"Monday", 2:"Tuesday", 3:"Wednesday", 
                4:"Thursday", 5:"Friday"
        }
        def __init__(self):
                self.days = [2,1,5,3,4]

        def generateHCO(self, list):
                days = self.days
                result = []

                for i in range(len(list)):
                        choice = rd.choice(days)
                        days.remove(choice)
                        day = self.__DAYS[choice]
                        result.append( (list[i], day) )            
                return result


test = GenerateData()
test.generateHCO([('MAT 111', 3), ('MAT 112', 3)])
# test.generateLCO([('PHY 113', 3), ('GST 110', 3), ('CPT 111 ', 3), ('CHM 111', 3), ('STA 117 ', 4)])
