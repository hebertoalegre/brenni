import os
import csv
import subprocess
from werkzeug.utils import secure_filename
from backend.config import app, db, ExportsDB, ImportsdDB, ALLOWED_EXTENSIONS
from flask import render_template, redirect, url_for, request, flash
from datetime import datetime


@app.route('/')
def home():
    return render_template("home.html")

@app.route('/imports', methods=['GET','POST'])
def fred():
    return render_template('imports.html')
    # fredskey = [(key[0], key[1], key[2]) for key in FredDB.query.order_by('id').with_entities(FredDB.fredkey, FredDB.fredname, FredDB.id).all()]

    # if request.method =='POST':
    #     if request.form.get('F15B')=='DESCARGAR':
    #         dir = request.form.get('F15D')
    #         fredpy = FredApi()
    #         fredpy.set_token(request.form.get('FREDKEY'))
    #         for i in request.form.getlist('CHECKIT'):                
    #             if i =='Todos':
    #                 file = os.path.join(dir,'todos')
    #                 df = pd.concat([pd.DataFrame(fredpy.get_series(j[0],"1992-01-01"))[['date', 'value']].set_index('date') for j in fredskey], axis=1)       
    #                 df.columns= [col[1] for col in fredskey]
    #                 df.to_csv(f'{file}.csv', encoding='utf-8', index=True, sep=',')
    #             else:
    #                 json_data = fredpy.get_series(i,"1992-01-01")
    #                 os.chdir(rf'{dir}')
    #                 file =os.path.join(dir,FredDB.query.filter(FredDB.fredkey==i).with_entities(FredDB.fredname)[0][0].replace(' ', '_'))
    #                 pd.DataFrame(json_data)[['date', 'value']].to_csv(f'{file}.csv', encoding='utf-8', index=False, sep=',')              
 
    #     if request.form.get('addregistro')=='modificar':
    #         return redirect(url_for('registros', fredskey=fredskey))
            
    # return render_template('fred.html', fredskey=fredskey)