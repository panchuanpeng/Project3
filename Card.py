#coding=utf-8
#import libs 
import sys
import Card_cmd
import Card_sty
import Fun
import os
import tkinter
from   tkinter import *
import tkinter.ttk
import tkinter.font
#Add your Varial Here: (Keep This Line of comments)
#Define UI Class
class  Card:
    def __init__(self,root,isTKroot = True):
        uiName = self.__class__.__name__
        Fun.Register(uiName,'UIClass',self)
        self.root = root
        Fun.Register(uiName,'root',root)
        style = Card_sty.SetupStyle()
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
        Button_4 = tkinter.Button(Form_1,text="修改")
        Fun.Register(uiName,'Button_4',Button_4)
        Fun.SetControlPlace(uiName,'Button_4',430,110,100,28)
        Button_4.configure(bg = "#00ffff")
        Button_4.configure(command=lambda:Card_cmd.Button_4_onCommand(uiName,"Button_4"))
        Button_5 = tkinter.Button(Form_1,text="删除")
        Fun.Register(uiName,'Button_5',Button_5)
        Fun.SetControlPlace(uiName,'Button_5',620,110,100,28)
        Button_5.configure(bg = "#00ffff")
        Button_5.configure(command=lambda:Card_cmd.Button_5_onCommand(uiName,"Button_5"))
        Button_6 = tkinter.Button(Form_1,text="加载全部")
        Fun.Register(uiName,'Button_6',Button_6)
        Fun.SetControlPlace(uiName,'Button_6',810,110,100,28)
        Button_6.configure(bg = "#00ffff")
        Button_6.configure(activebackground = "#808080")
        Button_6.configure(command=lambda:Card_cmd.Button_6_onCommand(uiName,"Button_6"))
        Button_3 = tkinter.Button(Form_1,text="增加")
        Fun.Register(uiName,'Button_3',Button_3)
        Fun.SetControlPlace(uiName,'Button_3',240,110,100,28)
        Button_3.configure(bg = "#00ffff")
        Button_3.configure(command=lambda:Card_cmd.Button_3_onCommand(uiName,"Button_3"))
        Button_2 = tkinter.Button(Form_1,text="查询")
        Fun.Register(uiName,'Button_2',Button_2)
        Fun.SetControlPlace(uiName,'Button_2',50,110,100,28)
        Button_2.configure(bg = "#00ffff")
        Button_2.configure(fg = "#000000")
        Button_2.configure(command=lambda:Card_cmd.Button_2_onCommand(uiName,"Button_2"))
        ListView_8 = tkinter.ttk.Treeview(Form_1,show="headings")
        Fun.Register(uiName,'ListView_8',ListView_8)
        Fun.SetControlPlace(uiName,'ListView_8',0,200,1400,600)
        ListView_8.configure(selectmode = "extended")
        ListView_8.configure(columns = ["Id","针卡编号","S/N","NSI编号","Vendor","验证状态","使用状态","适用产品","Td 预警量","Td 使用量","位置","备注"])
        ListView_8.column("Id",anchor="center",width=10)
        ListView_8.heading("Id",anchor="center",text="Id")
        ListView_8.column("针卡编号",anchor="center",width=80)
        ListView_8.heading("针卡编号",anchor="center",text="针卡编号")
        ListView_8.column("S/N",anchor="center",width=80)
        ListView_8.heading("S/N",anchor="center",text="S/N")
        ListView_8.column("NSI编号",anchor="center",width=80)
        ListView_8.heading("NSI编号",anchor="center",text="NSI编号")
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
        Fun.SetControlPlace(uiName,'Label_10',280,40,80,20)
        Label_10.configure(relief = "flat")
        Label_11 = tkinter.Label(Form_1,text="验证状态")
        Fun.Register(uiName,'Label_11',Label_11)
        Fun.SetControlPlace(uiName,'Label_11',520,40,80,20)
        Label_11.configure(relief = "flat")
        Label_12 = tkinter.Label(Form_1,text="适用产品")
        Fun.Register(uiName,'Label_12',Label_12)
        Fun.SetControlPlace(uiName,'Label_12',750,40,80,20)
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
        Fun.SetControlPlace(uiName,'Entry_16',360,40,140,20)
        Entry_16.configure(relief = "sunken")
        ComboBox_17_Variable = Fun.AddTKVariable(uiName,'ComboBox_17')
        ComboBox_17 = tkinter.ttk.Combobox(Form_1,textvariable=ComboBox_17_Variable, state="readonly")
        Fun.Register(uiName,'ComboBox_17',ComboBox_17)
        Fun.SetControlPlace(uiName,'ComboBox_17',600,40,130,20)
        ComboBox_17.configure(state = "readonly")
        ComboBox_17["values"] = [""] + Card_cmd.config.ComboBox["zt"]
        ComboBox_17.current(0)
        Entry_18_Variable = Fun.AddTKVariable(uiName,'Entry_18','')
        Entry_18 = tkinter.Entry(Form_1,textvariable=Entry_18_Variable)
        Fun.Register(uiName,'Entry_18',Entry_18)
        Fun.SetControlPlace(uiName,'Entry_18',830,40,140,20)
        Entry_18.configure(relief = "sunken")
        Entry_19_Variable = Fun.AddTKVariable(uiName,'Entry_19','')
        Entry_19 = tkinter.Entry(Form_1,textvariable=Entry_19_Variable)
        Fun.Register(uiName,'Entry_19',Entry_19)
        Fun.SetControlPlace(uiName,'Entry_19',1150,40,140,20)
        Entry_19.configure(relief = "sunken")
        Button_20 = tkinter.Button(Form_1,text="导出当前界面")
        Fun.Register(uiName,'Button_20',Button_20)
        Fun.SetControlPlace(uiName,'Button_20',1000,110,100,28)
        Button_20.configure(bg = "#00ffff")
        Button_20.configure(command=lambda:Card_cmd.Button_20_onCommand(uiName,"Button_20"))
        Button_21 = tkinter.Button(Form_1,text="导出使用记录")
        Fun.Register(uiName,'Button_21',Button_21)
        Fun.SetControlPlace(uiName,'Button_21',1190,110,100,28)
        Button_21.configure(bg = "#00ffff")
        Button_21.configure(command=lambda:Card_cmd.Button_21_onCommand(uiName,"Button_21"))
        #Inital all element's Data 
        Fun.InitElementData(uiName)
        #Add Some Logic Code Here: (Keep This Line of comments)


#Create the root of Kinter 
if  __name__ == '__main__':
    root = tkinter.Tk()
    MyDlg = Card(root)
    root.mainloop()
