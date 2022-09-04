import openpyxl as o
from openpyxl import Workbook


class exl():
    #def __init__(self):

    def user_create_workbook(self):
        self.wb=Workbook()
        self.sheet=self.wb.active
        self.sheet["A1"]=" User Name "
        self.sheet["B2"]=" Password "
        self.sheet["C3"]=" email id "

    def add_data(self,username:str,password:str, mail:str):
        self.sheet["A"+str(self.sheet.max_row+1)]=username
        self.sheet["B"+str(self.sheet.max_row+1)]=password
        self.sheet["C"+str(self.sheet.max_row+1)]=mail

        self.wb.save('reg.xlsx')
