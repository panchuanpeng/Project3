#coding=utf-8
#import libs 
import sys
import Add_cmd
import Add_sty
import Fun
import os
import tkinter
from   tkinter import *
import tkinter.ttk
import tkinter.font
#Add your Varial Here: (Keep This Line of comments)
#Define UI Class
class  Add:
    def __init__(self,root,isTKroot = True):
        uiName = self.__class__.__name__
        Fun.Register(uiName,'UIClass',self)
        self.root = root
        Fun.Register(uiName,'root',root)
        style = Add_sty.SetupStyle()
        if isTKroot == True:
            root.title("Form1")
            Fun.CenterDlg(uiName,root,620,600)
            root['background'] = '#efefef'
        Form_1= tkinter.Canvas(root,width = 10,height = 4)
        Form_1.place(x = 0,y = 0,width = 620,height = 600)
        Form_1.configure(bg = "#efefef")
        Form_1.configure(highlightthickness = 0)
        Fun.Register(uiName,'Form_1',Form_1)
        #Create the elements of root 
        Label_2 = tkinter.Label(Form_1,text="针卡编号",anchor="w")
        Fun.Register(uiName,'Label_2',Label_2)
        Fun.SetControlPlace(uiName,'Label_2',40,40,100,20)
        Label_2.configure(relief = "flat")
        Label_4 = tkinter.Label(Form_1,text="Tip Length(必需)",anchor="w")
        Fun.Register(uiName,'Label_4',Label_4)
        Fun.SetControlPlace(uiName,'Label_4',40,120,100,20)
        Label_4.configure(relief = "flat")
        Label_5 = tkinter.Label(Form_1,text="使用状态",anchor="w")
        Fun.Register(uiName,'Label_5',Label_5)
        Fun.SetControlPlace(uiName,'Label_5',40,240,100,20)
        Label_5.configure(relief = "flat")
        Label_6 = tkinter.Label(Form_1,text="适用产品",anchor="w")
        Fun.Register(uiName,'Label_6',Label_6)
        Fun.SetControlPlace(uiName,'Label_6',40,280,100,20)
        Label_6.configure(relief = "flat")
        Label_7 = tkinter.Label(Form_1,text="备注",anchor="w")
        Fun.Register(uiName,'Label_7',Label_7)
        Fun.SetControlPlace(uiName,'Label_7',40,440,100,20)
        Label_7.configure(relief = "flat")
        Entry_8_Variable = Fun.AddTKVariable(uiName,'Entry_8','')
        Entry_8 = tkinter.Entry(Form_1,textvariable=Entry_8_Variable)
        Fun.Register(uiName,'Entry_8',Entry_8)
        Fun.SetControlPlace(uiName,'Entry_8',180,40,380,20)
        Entry_8.configure(relief = "sunken")
        Entry_9_Variable = Fun.AddTKVariable(uiName,'Entry_9','')
        Entry_9 = tkinter.Entry(Form_1,textvariable=Entry_9_Variable)
        Fun.Register(uiName,'Entry_9',Entry_9)
        Fun.SetControlPlace(uiName,'Entry_9',180,80,380,20)
        Entry_9.configure(relief = "sunken")
        Entry_10_Variable = Fun.AddTKVariable(uiName,'Entry_10','')
        Entry_10 = tkinter.Entry(Form_1,textvariable=Entry_10_Variable)
        Fun.Register(uiName,'Entry_10',Entry_10)
        Fun.SetControlPlace(uiName,'Entry_10',180,120,380,20)
        Entry_10.configure(relief = "sunken")
        Entry_10.bind("<KeyRelease>",Fun.EventFunction_Adaptor(Add_cmd.Entry_22_onKey, uiName=uiName, widgetName="Entry_10"))
        Entry_11_Variable = Fun.AddTKVariable(uiName, 'Entry_11')
        Entry_11 = tkinter.ttk.Combobox(Form_1, textvariable=Entry_11_Variable, state="readonly")
        Fun.Register(uiName, 'Entry_11', Entry_11)
        Fun.SetControlPlace(uiName, 'Entry_11', 180, 160, 380, 20)
        Entry_11.configure(state="readonly")
        Entry_11["values"] = Add_cmd.config.ComboBox["vd"]
        Entry_11.current(0)
        Label_3 = tkinter.Label(Form_1,text="S/N",anchor="w")
        Fun.Register(uiName,'Label_3',Label_3)
        Fun.SetControlPlace(uiName,'Label_3',40,80,100,20)
        Label_3.configure(relief = "flat")
        Button_14 = tkinter.Button(Form_1,text="增加",anchor="w")
        Fun.Register(uiName,'Button_14',Button_14)
        Fun.SetControlPlace(uiName,'Button_14',260,520,100,28)
        Button_14.configure(bg = "#00ffff")
        Button_14.configure(command=lambda:Add_cmd.Button_14_onCommand(uiName,"Button_14"))
        Label_16 = tkinter.Label(Form_1,text="Vendor",anchor="w")
        Fun.Register(uiName,'Label_16',Label_16)
        Fun.SetControlPlace(uiName,'Label_16',40,160,100,20)
        Label_16.configure(relief = "flat")
        Label_17 = tkinter.Label(Form_1,text="验证状态",anchor="w")
        Fun.Register(uiName,'Label_17',Label_17)
        Fun.SetControlPlace(uiName,'Label_17',40,200,100,20)
        Label_17.configure(relief = "flat")
        Label_18 = tkinter.Label(Form_1,text="Td 预警量",anchor="w")
        Fun.Register(uiName,'Label_18',Label_18)
        Fun.SetControlPlace(uiName,'Label_18',40,320,100,20)
        Label_18.configure(relief = "flat")
        Label_19 = tkinter.Label(Form_1,text="Td 使用量",anchor="w")
        Fun.Register(uiName,'Label_19',Label_19)
        Fun.SetControlPlace(uiName,'Label_19',40,360,100,20)
        Label_19.configure(relief = "flat")
        Label_20 = tkinter.Label(Form_1,text="位置",anchor="w")
        Fun.Register(uiName,'Label_20',Label_20)
        Fun.SetControlPlace(uiName,'Label_20',40,400,100,20)
        Label_20.configure(relief = "flat")
        Entry_14_Variable = Fun.AddTKVariable(uiName, 'Entry_14')
        Entry_14 = tkinter.ttk.Combobox(Form_1, textvariable=Entry_14_Variable, state="readonly")
        Fun.Register(uiName, 'Entry_14', Entry_14)
        Fun.SetControlPlace(uiName, 'Entry_14',180,280,380,20)
        Entry_14.configure(state="readonly")
        Entry_14["values"] = list(Add_cmd.config.product.values())
        Entry_14.current(0)
        Entry_22_Variable = Fun.AddTKVariable(uiName,'Entry_22','')
        Entry_22 = tkinter.Entry(Form_1,textvariable=Entry_22_Variable)
        Fun.Register(uiName,'Entry_22',Entry_22,'Entry_15')
        Fun.SetControlPlace(uiName,'Entry_22',180,320,380,20)
        Entry_22.configure(relief = "sunken")
        Entry_22.bind("<KeyRelease>",Fun.EventFunction_Adaptor(Add_cmd.Entry_22_onKey,uiName=uiName,widgetName="Entry_22"))
        Entry_23_Variable = Fun.AddTKVariable(uiName,'Entry_23','0')
        Entry_23 = tkinter.Entry(Form_1,textvariable=Entry_23_Variable)
        Fun.Register(uiName,'Entry_23',Entry_23,'Entry_16')
        Fun.SetControlPlace(uiName,'Entry_23',180,360,380,20)
        Entry_23.configure(relief = "sunken")
        Entry_23.bind("<KeyRelease>",Fun.EventFunction_Adaptor(Add_cmd.Entry_22_onKey, uiName=uiName, widgetName="Entry_23"))
        Entry_17_Variable = Fun.AddTKVariable(uiName, 'Entry_17')
        Entry_17 = tkinter.ttk.Combobox(Form_1, textvariable=Entry_17_Variable, state="readonly")
        Fun.Register(uiName, 'Entry_17', Entry_17)
        Fun.SetControlPlace(uiName, 'Entry_17',180,400,380,20)
        Entry_17.configure(state="readonly")
        Entry_17["values"] = Add_cmd.config.ComboBox["wz"]
        Entry_17.current(0)
        Entry_25_Variable = Fun.AddTKVariable(uiName,'Entry_25','')
        Entry_25 = tkinter.Entry(Form_1,textvariable=Entry_25_Variable)
        Fun.Register(uiName,'Entry_25',Entry_25,'Entry_18')
        Fun.SetControlPlace(uiName,'Entry_25',180,440,380,20)
        Entry_25.configure(relief = "sunken")
        ComboBox_26_Variable = Fun.AddTKVariable(uiName,'ComboBox_26')
        ComboBox_26 = tkinter.ttk.Combobox(Form_1,textvariable=ComboBox_26_Variable, state="readonly")
        Fun.Register(uiName,'ComboBox_26',ComboBox_26)
        Fun.SetControlPlace(uiName,'ComboBox_26',180,200,380,20)
        ComboBox_26.configure(state = "readonly")
        ComboBox_26["values"]=Add_cmd.config.ComboBox["zt"]
        ComboBox_26.current(0)
        ComboBox_27_Variable = Fun.AddTKVariable(uiName,'ComboBox_27')
        ComboBox_27 = tkinter.ttk.Combobox(Form_1,textvariable=ComboBox_27_Variable, state="readonly")
        Fun.Register(uiName,'ComboBox_27',ComboBox_27)
        Fun.SetControlPlace(uiName,'ComboBox_27',180,240,380,20)
        ComboBox_27.configure(state = "readonly")
        ComboBox_27["values"]=Add_cmd.config.ComboBox["sy"]
        ComboBox_27.current(0)
        #Inital all element's Data 
        Fun.InitElementData(uiName)
        #Add Some Logic Code Here: (Keep This Line of comments)


#Create the root of Kinter 
if  __name__ == '__main__':
    root = tkinter.Tk()
    MyDlg = Add(root)
    root.mainloop()
