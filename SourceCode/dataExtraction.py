import openpyxl as xl
import pandas as pd




class DataExtraction:
        def __init__(self, filename):
                self.__file = filename
        
        def getFilename(self):
                return str(self.__file)

        def getDataFrame(self) -> pd.core.frame.DataFrame:
                return pd.read_excel(self.getFilename(), sheet_name="First Semester", engine="openpyxl")

        def splitCourse(self) ->dict:
                # method to extract combined courses with high carry over rate
                
                result = {
                        "Combined HCO": list(),  # combined courses with high carry over rate
                        "Combined LCO": list(), # combined courses with low carry over rate
                        "Departmental": list(), # non Departmental course
                }

                df = self.getDataFrame()

                course_df=df["Courses"] 
                unit_df = df["Credit Unit"]
                combined_df = df["Combined"]
                co_rate =  df["HCOR"]

                for i in range(len(course_df)):
                        # Extract high combined courses with high carry over rate
                        if combined_df[i] and co_rate[i]:
                                result["Combined HCO"].append((course_df[i], unit_df[i]))

                        # Extract combined courses with low carry over rate
                        if combined_df[i] and not co_rate[i]:
                                result['Combined LCO'].append((course_df[i], unit_df[i]))

                        # Extract Departmental Courses 
                        if not combined_df[i]: 
                                result["Departmental"].append((course_df[i], unit_df[i]))

                print(result)
                return result
               




test = DataExtraction('sample.xlsx')
# print(test.getDataFrame())
test.splitCourse()

