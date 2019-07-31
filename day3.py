#6 variables
c1='Dark Chocolate'
c2='Milk Chocolate'
c3='White Chocolate'
dc=5
mc=6
wc=8
chocBox=dc+mc+wc
print(c1,'=',dc,'     ',c2,'=',mc,'     ',c3,'=',wc,'     Total=',chocBox)

#3 variables
choc1={'Dark Chocolate':5}
choc2={'Milk Chocolate':6}
choc3={'White Chocolate':8}
print(choc1, choc2, choc3)

#1 variable
chocBox={'Dark Chocolate':5,'Milk Chocolate':6,'White Chocolate':8}
print(chocBox)

#2 dictionaries
studentAge={'Steve':32,'Lia':28,'Vin':45,'Katie':38}
studentGender={'Steve':'Male','Lia':'Female','Vin':'Male','Katie':'Female'}
print(studentAge,studentGender)

#Lists within a list
student=[['Steve',32,'M'],['Lia',28,'F'],['Vin',45,'M'],['Katie',38,'F']]
print(student)

#dictionaries within a list
studentInfo=[studentAge,studentGender]
print(studentInfo)

#data analysis (students)
import pandas as pd
dir(pd)
studentdf=pd.DataFrame(student,columns=('name','age','gender'),index=['1','2','3','4'])
print(studentdf)

#data analysis (chocolates)
cadBox=[['Dark Chocolate',5],['Milk Chocolate',6],['White Chocolate',8]]
chocdf=pd.DataFrame(cadBox,columns=('type','amount'),index=['1','2','3'])
print(chocdf)

print(studentdf['name'])
print(studentdf['age'])
print(studentdf['gender'])
print(chocdf['type'])
print(chocdf['amount'])

#bar graphs
import plotly
dir(plotly)
from plotly.offline import plot
import plotly.graph_objs as go

title= go.Layout(title='ages of students')

studentBar= go.Bar(x=studentdf["name"],y=studentdf["age"])

fig= go.Figure(data=[studentBar],layout=title)
plot(fig)

title2= go.Layout(title='number of chocolates by type')

chocBar= go.Bar(x=chocdf['type'],y=chocdf['amount'])

fig2= go.Figure(data=[chocBar],layout=title2)
plot(fig2)