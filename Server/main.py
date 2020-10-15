#-*- coding: utf-8 -*-
from Server import app
from flask import Flask, render_template, request, jsonify, session, redirect, url_for
from database import Engine, Base, Session, member, tabledb

from datetime import datetime
import time
import sys
import json
import hashlib
import string
import threading

reload(sys)
sys.setdefaultencoding('utf-8')

app.config.update(dict(
	SECRET_KEY = hashlib.md5(str(datetime.today())).hexdigest()
))

@app.route('/',methods=['POST',"GET"])
def index():
	
	return render_template('index.html')


@app.route('/login', methods=["POST","GET"])
def login():
	############ problem 2 - (1) ############
	inputID = request.form['loginID']
	inputPW = request.form['loginPW']
	
	loginUser = Session.query(member).filter(member.id == inputID).all()
	
	if not loginUser :
		temp = 'ID가 존재하지 않습니다.'
		error = temp.encode('utf-8')
	elif loginUser[0].password != inputPW :
		temp = '비밀번호가 틀렸습니다.'
		error = temp.encode('utf-8')        
	else :
		session['logged_in'] = True
		session['loginID'] = loginUser[0].id
		session['loginName'] = loginUser[0].name
		session['loginNick'] = loginUser[0].nickname
		session['loginnum'] = loginUser[0].num
		session['maxf']=loginUser[0].maxf
		return jsonify(result=1, url=url_for('main'))
	
	print error
	return jsonify(result=2 ,error = error)
	#########################################

@app.route('/signup', methods=['POST',"GET"])
def signup():
	############ problem 2 - (2) ############
	#if session.get('logged_in'):
	#    return url_for('index')
	
	subquery = Session.query(member).filter(member.id==request.form['inputID']).first()
	if subquery:
		return jsonify(result=0, error='ID가 존재합니다.')
	
	newmember = member(id=request.form['inputID'], password=request.form['inputPW'], name = request.form['inputName'], nickname = request.form['inputNick'],maxf=3)
	
	
	Session.add(newmember)
	Session.flush()
	
	return jsonify(result=1, url=url_for('index'))
	######################################### save table

@app.route('/seat', methods=['POST',"GET"])
def seat():
	
	Session.query(tabledb).filter(tabledb.floor==request.form['floor']).delete(synchronize_session=False)
	xx=request.form['maxf']
	
	Session.query(member).filter(member.id==request.form['id']).update({'maxf':xx})
	Session.flush()
	
	id=request.form['id']
	floor=request.form['floor']
	maxf=request.form['maxf']
	
	numx= request.form.getlist('numx[]')
	info= request.form.getlist('info[]')
	seatx= request.form.getlist('seatx[]')
	seaty= request.form.getlist('seaty[]')
	color = request.form.getlist('color[]')
	

	for x in xrange(0,int(numx[-1])):
	    newtable = tabledb(id=id,floor=floor,numx=numx[x],info=info[x],seatx=seatx[x],seaty=seaty[x],color=color[x])
	    Session.add(newtable)
	    Session.flush()
	
		
	return url_for('main')
   

	
	#########################################
@app.route('/main')
def main():
	data=Session.query(tabledb).filter(tabledb.id==session['loginID']).all()
	count=Session.query(tabledb).filter(tabledb.id==session['loginID']).count()
	floor=[]
	seatx=[]
	info=[]
	seaty=[]
	color=[]
	table=[]
	for x in xrange(0, count):
	    floor.append(data[x].floor)
	    seatx.append(data[x].seatx)
	    seaty.append(data[x].seaty)
	    color.append(data[x].color)
	    info.append(data[x].info)
	    table.append([data[x].floor,data[x].info,data[x].seatx,data[x].seaty,data[x].color] )
	nickname=session['loginNick']	
	id=session['loginID']
	sub=Session.query(member).filter(member.id==id).first()
	
	return render_template('tables.html',floor=floor,info=info,seatx=seatx,seaty=seaty,color=color,count=count,table=table,id=id,maxf=sub.maxf,nickname=nickname)
	
