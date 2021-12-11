import sys

from SourceCode.dataExtraction import DataExtraction




if __name__ == "__main__":
        args = sys.argv
        filename = args[-1]

        # print(filename)
        test_object = DataExtraction(filename)
        test_object.splitCourse()
