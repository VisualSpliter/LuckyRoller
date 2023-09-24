import pandas as pd
import numpy as np
import random
from operator import itemgetter

# Todo: Use Static/Class Method Decorator
#*Done at 2023/9/24
# Todo: Randomize Student List
#*Done at 2023/9/24
# Todo: Add Class Weight Function
#!Suspended Due to Some Reason (Just Lazy)
# Todo: Add "Choose Only One Class" Function
#!Ditto
# Todo: Add Title Check Function
#*Done at 2021/9/24

class Excel:
    def __init__(self) -> None:
        pass
    
    class resolve:
        def __init__(self) -> None:
            pass
        
        @classmethod
        def file_resolve(self, excel_file_path = str, sheet_index = 0):

            # If File Path / File is Blank, Raise an Error and Exit
            if excel_file_path == None:
                raise RuntimeError("File Can't be Blank, You Must Choose a File")
            

            # Read The File in to Ram
            student_sheet = pd.read_excel(excel_file_path, sheet_name = sheet_index)

            return student_sheet
            
        @classmethod
        def student_list_resolve(self, excel_file_path = str, sheet_index = 0):
            student_sheet = self.file_resolve(excel_file_path , sheet_index)
            student_list = []


            # Append the Student Data in to Simplified List
            for i in range(0,len(student_sheet)-1):
                student_list.append([
                                    student_sheet.loc[ : , "班级"][i],
                                    student_sheet.loc[ : , "姓名"][i],
                                    student_sheet.loc[ : , "学号"][i]
                                    ])

            return student_list
        
        @classmethod
        def class_list(self, excel_file_path = str, sheet_index = 0):
            student_sheet = self.file_resolve(excel_file_path , sheet_index)
            class_list = []

            # Append the Student Data in to Simplified List
            for i in range(0,len(student_sheet)-1):
                class_list.append(student_sheet.loc[ : , "班级"][i])

            class_list = list(set(class_list))

            # ! Shit Code Here
            # class_list.sort(key=lambda x: x[-3:])

            class_list.sort()

            return class_list

    @staticmethod
    def list_shuffle(student_list):
        random.shuffle(student_list)
        return student_list
    
    @staticmethod
    def weighted_shuffle(class_number):
        pass



# Some Decent Examples
# excel_sheet = "2023级计算机系本科新生录取名单.xlsx"
# student_list = excel_resolve(excel_file_path = excel_sheet)
# print(student_list)

stu_lst = Excel.resolve.student_list_resolve(excel_file_path="2023级计算机系本科新生录取名单.xlsx")
class_lst = Excel.resolve.class_list(excel_file_path="2023级计算机系本科新生录取名单.xlsx")

print(stu_lst)
print(class_lst)

stu_lst = Excel().list_shuffle(stu_lst)
print(stu_lst)