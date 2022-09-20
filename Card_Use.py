#coding=utf-8
#import libs 
import sys
import Card_Use_cmd
import Card_Use_sty
import Fun
import os
import tkinter
from   tkinter import *
import tkinter.ttk
import tkinter.font
#Add your Varial Here: (Keep This Line of comments)
#Define UI Class
class  Card_Use:
    def __init__(self,root,isTKroot = True):
        uiName = self.__class__.__name__
        self.uiName = uiName
        Fun.Register(uiName,'UIClass',self)
        self.root = root
        self.isTKroot = isTKroot
        Fun.Register(uiName,'root',root)
        style = Card_Use_sty.SetupStyle()
        if isTKroot == True:
            root.title("Form1")
            Fun.CenterDlg(uiName,root,1400,800)
            root['background'] = '#efefef'
            root.bind('<Configure>',self.Configure)
        Form_1= tkinter.Canvas(root,width = 10,height = 4)
        Form_1.pack(fill=BOTH,expand=True)
        Form_1.configure(bg = "#efefef")
        Form_1.configure(highlightthickness = 0)
        Fun.Register(uiName,'Form_1',Form_1)
        #Create the elements of root 
        Button_4 = tkinter.Button(Form_1,text="归还")
        Fun.Register(uiName,'Button_4',Button_4)
        Fun.SetControlPlace(uiName,'Button_4',820,110,100,28)
        Button_4.configure(bg = "#00ffff")
        Button_4.configure(command=lambda:Card_Use_cmd.Button_4_onCommand(uiName,"Button_4"))
        Button_3 = tkinter.Button(Form_1,text="领用")
        Fun.Register(uiName,'Button_3',Button_3)
        Fun.SetControlPlace(uiName,'Button_3',430,110,100,28)
        Button_3.configure(bg = "#00ffff")
        Button_3.configure(command=lambda:Card_Use_cmd.Button_3_onCommand(uiName,"Button_3"))
        Button_2 = tkinter.Button(Form_1,text="查询")
        Fun.Register(uiName,'Button_2',Button_2)
        Fun.SetControlPlace(uiName,'Button_2',50,110,100,28)
        Button_2.configure(bg = "#00ffff")
        Button_2.configure(fg = "#000000")
        Button_2.configure(command=lambda:Card_Use_cmd.Button_2_onCommand(uiName,"Button_2"))
        ListView_8 = tkinter.ttk.Treeview(Form_1,show="headings")
        Fun.Register(uiName,'ListView_8',ListView_8)
        Fun.SetControlPlace(uiName,'ListView_8',0,200,1400,600)
        ListView_8.configure(selectmode = "extended")
        ListView_8.configure(columns = ["Id","针卡编号","S/N","Tip Length","Vendor","验证状态","使用状态","适用产品","Td 预警量","Td 使用量","位置","备注"])
        ListView_8.column("Id",anchor="center",width=10)
        ListView_8.heading("Id",anchor="center",text="Id")
        ListView_8.column("针卡编号",anchor="center",width=80)
        ListView_8.heading("针卡编号",anchor="center",text="针卡编号")
        ListView_8.column("S/N",anchor="center",width=80)
        ListView_8.heading("S/N",anchor="center",text="S/N")
        ListView_8.column("Tip Length",anchor="center",width=80)
        ListView_8.heading("Tip Length",anchor="center",text="Tip Length")
        ListView_8.column("Vendor",anchor="center",width=80)
        ListView_8.heading("Vendor",anchor="center",text="Vendor")
        ListView_8.column("验证状态",anchor="center",width=20)
        ListView_8.heading("验证状态",anchor="center",text="验证状态")
        ListView_8.column("使用状态",anchor="center",width=20)
        ListView_8.heading("使用状态",anchor="center",text="使用状态")
        ListView_8.column("适用产品",anchor="center",width=80)
        ListView_8.heading("适用产品",anchor="center",text="适用产品")
        ListView_8.column("Td 预警量",anchor="center",width=40)
        ListView_8.heading("Td 预警量",anchor="center",text="Td 预警量")
        ListView_8.column("Td 使用量",anchor="center",width=40)
        ListView_8.heading("Td 使用量",anchor="center",text="Td 使用量")
        ListView_8.column("位置",anchor="center",width=80)
        ListView_8.heading("位置",anchor="center",text="位置")
        ListView_8.column("备注",anchor="center",width=80)
        ListView_8.heading("备注",anchor="center",text="备注")
        ListView_8_Scrollbar = tkinter.Scrollbar(ListView_8,orient=tkinter.VERTICAL)
        ListView_8_Scrollbar.place(x = 1380,y = 0,width = 20,height = 600)
        ListView_8_Scrollbar.config(command = ListView_8.yview)
        ListView_8.config(yscrollcommand = ListView_8_Scrollbar.set)
        Label_9 = tkinter.Label(Form_1,text="针卡编号")
        Fun.Register(uiName,'Label_9',Label_9)
        Fun.SetControlPlace(uiName,'Label_9',50,40,80,20)
        Label_9.configure(relief = "flat")
        Label_10 = tkinter.Label(Form_1,text="Vendor")
        Fun.Register(uiName,'Label_10',Label_10)
        Fun.SetControlPlace(uiName,'Label_10',270,40,80,20)
        Label_10.configure(relief = "flat")
        Label_12 = tkinter.Label(Form_1,text="适用产品")
        Fun.Register(uiName,'Label_12',Label_12)
        Fun.SetControlPlace(uiName,'Label_12',510,40,80,20)
        Label_12.configure(relief = "flat")
        Label_13 = tkinter.Label(Form_1,text="Td 使用量")
        Fun.Register(uiName,'Label_13',Label_13)
        Fun.SetControlPlace(uiName,'Label_13',990,40,100,20)
        Label_13.configure(relief = "flat")
        ComboBox_14_Variable = Fun.AddTKVariable(uiName,'ComboBox_14')
        ComboBox_14 = tkinter.ttk.Combobox(Form_1,textvariable=ComboBox_14_Variable, state="readonly")
        Fun.Register(uiName,'ComboBox_14',ComboBox_14)
        Fun.SetControlPlace(uiName,'ComboBox_14',1090,40,60,20)
        ComboBox_14.configure(state = "readonly")
        ComboBox_14["values"]=[' ','>','<','=']
        ComboBox_14.current(0)
        Entry_15_Variable = Fun.AddTKVariable(uiName,'Entry_15','')
        Entry_15 = tkinter.Entry(Form_1,textvariable=Entry_15_Variable)
        Fun.Register(uiName,'Entry_15',Entry_15)
        Fun.SetControlPlace(uiName,'Entry_15',130,40,130,20)
        Entry_15.configure(relief = "sunken")
        Entry_16_Variable = Fun.AddTKVariable(uiName,'Entry_16','')
        Entry_16 = tkinter.Entry(Form_1,textvariable=Entry_16_Variable)
        Fun.Register(uiName,'Entry_16',Entry_16)
        Fun.SetControlPlace(uiName,'Entry_16',350,40,140,20)
        Entry_16.configure(relief = "sunken")
        Entry_18_Variable = Fun.AddTKVariable(uiName,'Entry_18','')
        Entry_18 = tkinter.Entry(Form_1,textvariable=Entry_18_Variable)
        Fun.Register(uiName,'Entry_18',Entry_18)
        Fun.SetControlPlace(uiName,'Entry_18',590,40,140,20)
        Entry_18.configure(relief = "sunken")
        Entry_19_Variable = Fun.AddTKVariable(uiName,'Entry_19','')
        Entry_19 = tkinter.Entry(Form_1,textvariable=Entry_19_Variable)
        Fun.Register(uiName,'Entry_19',Entry_19)
        Fun.SetControlPlace(uiName,'Entry_19',1150,40,140,20)
        Entry_19.configure(relief = "sunken")
        Label_20 = tkinter.Label(Form_1,text="针卡位置")
        Fun.Register(uiName,'Label_20',Label_20)
        Fun.SetControlPlace(uiName,'Label_20',740,40,80,20)
        Label_20.configure(relief = "flat")
        Entry_21_Variable = Fun.AddTKVariable(uiName,'Entry_21','')
        Entry_21 = tkinter.Entry(Form_1,textvariable=Entry_21_Variable)
        Fun.Register(uiName,'Entry_21',Entry_21)
        Fun.SetControlPlace(uiName,'Entry_21',820,40,140,20)
        Entry_21.configure(relief = "sunken")
        Button_22 = tkinter.Button(Form_1,text="NI计数")
        Fun.Register(uiName,'Button_22',Button_22)
        Fun.SetControlPlace(uiName,'Button_22',1190,110,100,28)
        Button_22.configure(bg = "#00ffff")
        Button_22.configure(command=lambda:Card_Use_cmd.Button_22_onCommand(uiName,"Button_22"))
        #Inital all element's Data 
        Fun.InitElementData(uiName)
        #Add Some Logic Code Here: (Keep This Line of comments)



        #Exit Application: (Keep This Line of comments)
        if self.isTKroot == True:
            self.root.protocol('WM_DELETE_WINDOW', self.Exit)
    def Exit(self):
        if self.isTKroot == True:
            self.root.destroy()

    def Configure(self,event):
        if self.root == event.widget:
            pass
#Create the root of Kinter 
if  __name__ == '__main__':
    root = tkinter.Tk()
    MyDlg = Card_Use(root)
    root.mainloop()
