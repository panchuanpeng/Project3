#coding=utf-8
#import libs 
import sys
import Use_List_cmd
import Use_List_sty
import Fun
import EXUIControl
import os
import tkinter
from   tkinter import *
import tkinter.ttk
import tkinter.font
#Add your Varial Here: (Keep This Line of comments)
#Define UI Class
class  Use_List:
    def __init__(self,root,isTKroot = True):
        uiName = self.__class__.__name__
        Fun.Register(uiName,'UIClass',self)
        self.root = root
        Fun.Register(uiName,'root',root)
        style = Use_List_sty.SetupStyle()
        if isTKroot == True:
            root.title("Form1")
            Fun.CenterDlg(uiName,root,1400,800)
            root['background'] = '#efefef'
        Form_1= tkinter.Canvas(root,width = 10,height = 4)
        Form_1.place(x = 0,y = 0,width = 1400,height = 800)
        Form_1.configure(bg = "#efefef")
        Form_1.configure(highlightthickness = 0)
        Fun.Register(uiName,'Form_1',Form_1)
        #Create the elements of root 
        Label_3 = tkinter.Label(Form_1,text="针卡编号")
        Fun.Register(uiName,'Label_3',Label_3,'针卡编号')
        Fun.SetControlPlace(uiName,'Label_3',60,40,80,20)
        Label_3.configure(relief = "flat")
        Entry_4_Variable = Fun.AddTKVariable(uiName,'Entry_4','')
        Entry_4 = tkinter.Entry(Form_1,textvariable=Entry_4_Variable)
        Fun.Register(uiName,'Entry_4',Entry_4)
        Fun.SetControlPlace(uiName,'Entry_4',130,40,130,20)
        Entry_4.configure(relief = "sunken")
        Label_6 = tkinter.Label(Form_1,text="Operator")
        Fun.Register(uiName,'Label_6',Label_6)
        Fun.SetControlPlace(uiName,'Label_6',360,40,90,20)
        Label_6.configure(relief = "flat")
        Entry_7_Variable = Fun.AddTKVariable(uiName,'Entry_7','')
        Entry_7 = tkinter.Entry(Form_1,textvariable=Entry_7_Variable)
        Fun.Register(uiName,'Entry_7',Entry_7)
        Fun.SetControlPlace(uiName,'Entry_7',450,40,130,20)
        Entry_7.configure(relief = "sunken")
        Label_10 = tkinter.Label(Form_1,text="Td使用量")
        Fun.Register(uiName,'Label_10',Label_10)
        Fun.SetControlPlace(uiName,'Label_10',680,40,90,20)
        Label_10.configure(relief = "flat")
        ComboBox_11_Variable = Fun.AddTKVariable(uiName,'ComboBox_11')
        ComboBox_11 = tkinter.ttk.Combobox(Form_1,textvariable=ComboBox_11_Variable, state="readonly")
        Fun.Register(uiName,'ComboBox_11',ComboBox_11)
        Fun.SetControlPlace(uiName,'ComboBox_11',770,40,50,20)
        ComboBox_11.configure(state = "readonly")
        ComboBox_11["values"] = [' ', '>', '<', '=']
        ComboBox_11.current(0)
        Entry_12_Variable = Fun.AddTKVariable(uiName,'Entry_12','')
        Entry_12 = tkinter.Entry(Form_1,textvariable=Entry_12_Variable)
        Fun.Register(uiName,'Entry_12',Entry_12)
        Fun.SetControlPlace(uiName,'Entry_12',820,40,120,20)
        Entry_12.configure(relief = "sunken")
        Label_13 = tkinter.Label(Form_1,text="至")
        Fun.Register(uiName,'Label_13',Label_13)
        Fun.SetControlPlace(uiName,'Label_13',1160,70,30,20)
        Label_13.configure(relief = "flat")
        Button_16 = tkinter.Button(Form_1,text="导出当前界面")
        Fun.Register(uiName,'Button_16',Button_16)
        Fun.SetControlPlace(uiName,'Button_16',480,110,100,28)
        Button_16.configure(bg = "#00ffff")
        Button_16.configure(command=lambda:Use_List_cmd.Button_16_onCommand(uiName,"Button_16"))
        ListView_2 = tkinter.ttk.Treeview(Form_1,show="headings")
        Fun.Register(uiName,'ListView_2',ListView_2)
        Fun.SetControlPlace(uiName,'ListView_2',0,200,1400,600)
        ListView_2.configure(selectmode = "extended")
        ListView_2.configure(columns = ["Id","针卡编号","日期","操作人","变更前验证状态","变更后验证状态","变更前使用状态","变更后使用状态","Td 数"])
        ListView_2.column("Id",anchor="center",width=10)
        ListView_2.heading("Id",anchor="center",text="Id")
        ListView_2.column("针卡编号",anchor="center",width=100)
        ListView_2.heading("针卡编号",anchor="center",text="针卡编号")
        ListView_2.column("日期",anchor="center",width=150)
        ListView_2.heading("日期",anchor="center",text="日期")
        ListView_2.column("操作人",anchor="center",width=150)
        ListView_2.heading("操作人",anchor="center",text="操作人")
        ListView_2.column("变更前验证状态",anchor="center",width=150)
        ListView_2.heading("变更前验证状态",anchor="center",text="变更前验证状态")
        ListView_2.column("变更后验证状态",anchor="center",width=150)
        ListView_2.heading("变更后验证状态",anchor="center",text="变更后验证状态")
        ListView_2.column("变更前使用状态",anchor="center",width=150)
        ListView_2.heading("变更前使用状态",anchor="center",text="变更前使用状态")
        ListView_2.column("变更后使用状态",anchor="center",width=150)
        ListView_2.heading("变更后使用状态",anchor="center",text="变更后使用状态")
        ListView_2.column("Td 数", anchor="center", width=150)
        ListView_2.heading("Td 数", anchor="center", text="Td 数")
        Button_15 = tkinter.Button(Form_1,text="查询")
        Fun.Register(uiName,'Button_15',Button_15)
        Fun.SetControlPlace(uiName,'Button_15',50,110,100,28)
        Button_15.configure(bg = "#00ffff")
        Button_15.configure(command=lambda:Use_List_cmd.Button_15_onCommand(uiName,"Button_15"))
        Frame_21 = tkinter.Frame(Form_1)
        Fun.Register(uiName,'Frame_21',Frame_21)
        Fun.SetControlPlace(uiName,'Frame_21',980,0,180,180)
        Frame_21.configure(bg = "#888888")
        Frame_21.configure(relief = "flat")
        Calendar_21= EXUIControl.Calendar(Frame_21)
        Calendar_21.setDatebarBgColor("#000000")
        Calendar_21.setDatebarFgColor("#ffffff")
        Calendar_21.setSelectedBgColor("#ecffc4")
        Calendar_21.setSelectedFgColor("#05640e")
        Fun.Register(uiName, 'Calendar_21', Calendar_21)
        Frame_22 = tkinter.Frame(Form_1)
        Fun.Register(uiName, 'Frame_22', Frame_22)
        Fun.SetControlPlace(uiName,'Frame_22',1190,0,180,180)
        Frame_22.configure(bg = "#888888")
        Frame_22.configure(relief = "flat")
        Calendar_22= EXUIControl.Calendar(Frame_22)
        Calendar_22.setDatebarBgColor("#000000")
        Calendar_22.setDatebarFgColor("#ffffff")
        Calendar_22.setSelectedBgColor("#ecffc4")
        Calendar_22.setSelectedFgColor("#05640e")
        Fun.Register(uiName, 'Calendar_22', Calendar_22)
        #Inital all element's Data 
        Fun.InitElementData(uiName)
        #Add Some Logic Code Here: (Keep This Line of comments)


#Create the root of Kinter 
if  __name__ == '__main__':
    root = tkinter.Tk()
    MyDlg = Use_List(root)
    root.mainloop()