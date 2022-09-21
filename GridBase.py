import Fun
# TreeView作为表格使用时的相关操作
def addCard(uiName,TreeViewName,*item):
    treeview = Fun.GetElement(uiName,TreeViewName)
    treeview.insert('', 'end', values=item)

def editSelected(uiName,TreeViewName,*item):
    treeview = Fun.GetElement(uiName,TreeViewName)
    index = treeview.selection()
    if(len(index) == 0):
        return None
    item = (treeview.item(index)['values'][0],) + item
    treeview.item(index, values=item)
    return treeview.item(index)['values']

def takeoutcard(uiName,TreeViewName,item):
    treeview = Fun.GetElement(uiName,TreeViewName)
    index = treeview.selection()
    if(len(index) == 0):
        return None
    treeview.set(index, "使用状态", item)
    return treeview.item(index)['values']

def returncard(uiName,TreeViewName,*item):
    treeview = Fun.GetElement(uiName,TreeViewName)
    index = treeview.selection()
    if(len(index) == 0):
        return None
    treeview.set(index, "Tip Length", item[0])
    treeview.set(index, "使用状态", item[1])
    treeview.set(index, "位置", item[2])
    treeview.set(index, "备注", item[3])
    return treeview.item(index)['values']

def deleteSelected(uiName,TreeViewName):
    treeview = Fun.GetElement(uiName,TreeViewName)
    index = treeview.selection()
    if(len(index) == 0):
        return None
    item = treeview.item(index)
    treeview.delete(index)
    return item['values']

def getSelected(uiName,TreeViewName):
    treeview = Fun.GetElement(uiName,TreeViewName)
    index = treeview.selection()
    if(len(index) == 0):
        return None
    return treeview.item(index)['values']

def clearData(uiName,TreeViewName):
    treeview = Fun.GetElement(uiName,TreeViewName)
    obj = treeview.get_children()
    for i in obj:
        treeview.delete(i)
    return treeview

def getallData(uiName,TreeViewName):
    value_list = [["Id","针卡编号","S/N","Tip Length","Vendor","验证状态","使用状态","适用产品","Td 预警量","Td 使用量","位置","备注"]]
    treeview = Fun.GetElement(uiName,TreeViewName)
    obj = treeview.get_children()
    for i in obj:
        value_list.append(treeview.item(i)['values'])
    return value_list

def getuselist(uiName,TreeViewName):
    value_list = [["Id","针卡编号","日期","操作人","Tip Length","变更前验证状态","变更后验证状态","变更前使用状态","变更后使用状态","Td 数","位置","备注"]]
    treeview = Fun.GetElement(uiName,TreeViewName)
    obj = treeview.get_children()
    for i in obj:
        value_list.append(treeview.item(i)['values'])
    return value_list


def edituser(uiName,TreeViewName,*item):
    treeview = Fun.GetElement(uiName,TreeViewName)
    index = treeview.selection()
    if(len(index) == 0):
        return None
    treeview.set(index, "Admin", item[0])
    return treeview.item(index)['values']