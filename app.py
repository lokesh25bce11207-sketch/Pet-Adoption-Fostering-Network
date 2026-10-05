from flask import Flask,render_template,request,redirect,url_for,flash
import mysql.connector
from config import DB_CONFIG,SECRET_KEY
app=Flask(__name__); app.secret_key=SECRET_KEY
def db(): return mysql.connector.connect(**DB_CONFIG)
def q(sql,p=()):
 c=db(); cur=c.cursor(dictionary=True); cur.execute(sql,p); rows=cur.fetchall(); cur.close(); c.close(); return rows
@app.route('/')
def home():
 c={"animals":q('SELECT COUNT(*) c FROM animals')[0]['c'],"available":q("SELECT COUNT(*) c FROM animals WHERE current_status='Available'")[0]['c'],"fostered":q("SELECT COUNT(*) c FROM animals WHERE current_status='Fostered'")[0]['c'],"adopted":q("SELECT COUNT(*) c FROM animals WHERE current_status='Adopted'")[0]['c'],"shelters":q('SELECT COUNT(*) c FROM shelters')[0]['c'],"pending_apps":q("SELECT COUNT(*) c FROM adoption_applications WHERE application_status IN ('Pending','Under Review')")[0]['c'],"overdue":q("SELECT COUNT(*) c FROM medical_records WHERE follow_up_status='Pending' AND next_checkup_date<CURRENT_DATE")[0]['c']}
 return render_template('dashboard.html',cards=c)
@app.route('/animals',methods=['GET','POST'])
def animals():
 if request.method=='POST':
  c=db(); cur=c.cursor(); data=[request.form.get(x) or None for x in ['name','species','breed','age','gender','size','health_status','vaccination_status','shelter_id','special_needs']]; cur.execute('INSERT INTO animals(name,species,breed,age,gender,size,health_status,vaccination_status,shelter_id,special_needs) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)',data); c.commit(); cur.close(); c.close(); flash('Animal added','success'); return redirect(url_for('animals'))
 return render_template('animals.html',animals=q('SELECT a.*,s.shelter_name FROM animals a LEFT JOIN shelters s ON s.shelter_id=a.shelter_id ORDER BY a.animal_id DESC'),shelters=q('SELECT shelter_id,shelter_name FROM shelters ORDER BY shelter_name'))
@app.route('/shelters')
def shelters(): return render_template('table.html',title='Shelters',headers=['ID','Shelter','City','Capacity','Animals'],rows=q('SELECT s.shelter_id,s.shelter_name,s.city,s.capacity,COUNT(a.animal_id) FROM shelters s LEFT JOIN animals a ON a.shelter_id=s.shelter_id GROUP BY s.shelter_id'))
@app.route('/adopters')
def adopters(): return render_template('table.html',title='Adopters',headers=['ID','Name','Age','Preferred Species','Size'],rows=q('SELECT adopter_id,full_name,age,preferred_species,preferred_size FROM adopters'))
@app.route('/medical')
def medical(): return render_template('table.html',title='Medical Follow-up',headers=['Animal','Next Checkup','Status','State'],rows=q('SELECT animal_name,next_checkup_date,follow_up_status,followup_state FROM Medical_Followup_View ORDER BY next_checkup_date'))
@app.route('/applications')
def applications(): return render_template('table.html',title='Applications',headers=['ID','Animal','Adopter','Status','Visit','Recommendation'],rows=q('SELECT application_id,animal_name,adopter_name,application_status,visit_status,approval_recommendation FROM Adoption_Application_Summary_View'))
@app.route('/adoptions')
def adoptions(): return render_template('table.html',title='Adoptions',headers=['ID','Animal','Adopter','Date','Status'],rows=q('SELECT ar.adoption_id,a.name,ad.full_name,ar.adoption_date,ar.adoption_status FROM adoption_records ar JOIN animals a ON a.animal_id=ar.animal_id JOIN adopters ad ON ad.adopter_id=ar.adopter_id'))
@app.route('/matching')
def matching():
 aid=request.args.get('adopter_id',type=int); adop=q('SELECT adopter_id,full_name FROM adopters'); rows=[]
 if aid: rows=q("SELECT a.name,a.species,a.size,a.health_status,s.shelter_name FROM adopters ad JOIN animals a ON a.current_status='Available' AND (ad.preferred_species IS NULL OR ad.preferred_species=a.species) AND (ad.preferred_size='Any' OR ad.preferred_size=a.size) LEFT JOIN shelters s ON s.shelter_id=a.shelter_id WHERE ad.adopter_id=%s",(aid,))
 return render_template('matching.html',adopters=adop,matches=rows,selected=aid)
if __name__=='__main__': app.run(debug=True)
