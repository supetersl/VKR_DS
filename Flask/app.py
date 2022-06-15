import flask
from flask import render_template
import pickle
import sklearn
from sklearn.linear_model import LinearRegression
import pandas as pd

app = flask.Flask(__name__, template_folder = 'templates')
@app.route('/', methods = ['POST', 'GET'])
def main():
    
    if flask.request.method =='GET':
       return render_template('main.html')
       
    
    if flask.request.method =='POST':
       loaded_model=pickle.load(open('M11.pkl','rb'))
       
       s1 = float(flask.request.form['Угол нашивки, град'])  
       s2 = float(flask.request.form['Шаг нашивки'])
       s3 = float(flask.request.form['Плотность нашивки']) 
       s4 = float(flask.request.form['Соотношение матрица-наполнитель'])
       s5 = float(flask.request.form['Плотность, кг/м3'])
       s6 = float(flask.request.form['модуль упругости, ГПа'])
       s7 = float(flask.request.form['Количество отвердителя, м.%'])
       s8 = float(flask.request.form['Содержание эпоксидных групп,%_2'])
       s9 = float(flask.request.form['Температура вспышки, С_2'])
       s10 = float(flask.request.form['Поверхностная плотность, г/м2'])
       s11 = float(flask.request.form['Прочность при растяжении, МПа'])
       s12 = float(flask.request.form['Потребление смолы, г/м2']) 
       data = {'Угол нашивки, град':s1,
                     'Шаг нашивки': s2,
                     'Плотность нашивки': s3,
                     'Соотношение матрица-наполнитель': s4,
                     'Плотность, кг/м3': s5,
                     'модуль упругости, ГПа': s6,
                     'Количество отвердителя, м.%': s7,
                     'Содержание эпоксидных групп,%_2': s8,
                     'Температура вспышки, С_2': s9,
                     'Поверхностная плотность, г/м2': s10,
                     'Прочность при растяжении, МПа': s11,
                     'Потребление смолы, г/м2': s12}
       X = pd.DataFrame(data, index=[0])
       y_pred = loaded_model.predict(X)  
       list1 = y_pred.tolist()
       s=float(list1[0])
       return render_template('main.html', result=s)
       

if __name__ =='__main__':
   app.run() 
