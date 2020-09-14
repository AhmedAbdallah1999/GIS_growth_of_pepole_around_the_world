from xlrd import open_workbook
work_book = open_workbook('growth.xls')
sheet =work_book.sheet_by_index(0)

list =[]
for row in range(sheet.nrows):
    for col in range(sheet.ncols):

        if sheet.cell(row,col).value == "Country Code" :
            for x in range(sheet.nrows-1):
                list.append(sheet.cell(x+ 1, col).value)


print(list)

list2 =[]
for row in range(sheet.nrows):
    for col in range(sheet.ncols):

        if sheet.cell(row,col).value == "Country Name" :
            for x in range(sheet.nrows-1):
                list2.append(sheet.cell(x+ 1, col).value)


print(list2)
y = input("enter year")
list3 =[]
for row in range(sheet.nrows):
    for col in range(sheet.ncols):

        if sheet.cell(row,col).value == y:
            for x in range(sheet.nrows-1):
                list3.append(sheet.cell(x+ 1, col).value)


print(list3)

import pygal
# importing World_map package
from pygal.maps.world import World
# creating object
worldmap_chart = pygal.maps.world.World()
# adding title
worldmap_chart.title = 'Growth of pepole'
# add data
list4 =[]
list5 =[]
list6 =[]
list7 =[]
list8 =[]
for y in range(sheet.nrows-1):
    if list3[y] <-3.55:
        list4.append(list[y])
    elif list3[y] >-3.55 and list3[y] <-0.44  :
        list5.append(list[y])
    elif list3[y] >-0.44  and list3[y] < 1.6:
        list6.append(list[y])
    elif list3[y] >1.6 and list3[y] < 2.25 :
        list7.append(list[y])
    elif list3[y] >2.25 :
        list8.append(list[y])

worldmap_chart.add("< -3.5", list4)
worldmap_chart.add("-3.55-0.44", list5)
worldmap_chart.add("-0.44-1.6", list6)
worldmap_chart.add("1.6-2.25", list7)
worldmap_chart.add(">2.25", list8)

# rendering the svg to file
worldmap_chart.render_to_file('growth_of_pepole.svg')
