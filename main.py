from fastapi import  FastAPI
import pandas as pd
import mysql.connector
import mysql
app=FastAPI()

conn =mysql.connector.connect(host='10.60.1.143',user='devteam',password="Boss@8055",database='degree_exam_anlysis')        
cursor=conn.cursor()
print("database connection is successfull")

@app.get('/<string:pcode>')
def paper(pcode):
    cursor.execute('SELECT * FROM ' +pcode)
    data=cursor.fetchall()
    return {"data":data}

@app.get('/level/<string:pcode>/<string:level>')
def paperlevel(pcode,level):
    if(level=='branch'):
        qry="SELECT branch,subject,count(distinct questionid) as qnos,sum(case when result ='r' then 1 else 0 end) as r, sum(case when result ='w' then 1 else 0 end) as w, sum(case when result ='l' then 1 else 0 end) as l,ifnull ((sum(case when result ='r' then 1 else 0 end) /(sum(case when result ='r' then 1 else 0 end) + sum(case when result ='w' then 1 else 0 end) +sum(case when result ='l' then 1 else 0 end) )) *100,0) as strike FROM "+pcode+" group by subject,branch  order by subject,branch,strike;"
    elif(level=='topic'):
        qry="SELECT branch,subject,topicid, topicname,count(distinct questionid) as qnos,sum(case when result ='r' then 1 else 0 end) as r, sum(case when result ='w' then 1 else 0 end) as w, sum(case when result ='l' then 1 else 0 end) as l,ifnull ((sum(case when result ='r' then 1 else 0 end) /(sum(case when result ='r' then 1 else 0 end) + sum(case when result ='w' then 1 else 0 end) +sum(case when result ='l' then 1 else 0 end) )) *100,0) as strike FROM "+pcode+" group by topicname,subject,branch  order by topicname,subject,branch,strike;"
    else:
        return 'Invalid level!'
    res=cursor.execute(qry)
    return res.to_json(orient="records")

def studentResult(dataframe,papercode):
    subject_names=dataframe.subject.unique()
    subjectWiseMarks=pd.pivot_table(dataframe,index=['suc','branch','program','studentname','examtype'], values=['studentmarks','timespent','questionmarks'], columns=["subject","result"], fill_value=0,aggfunc={'result':'count', 'studentmarks':'sum','timespent':'sum','questionmarks':'sum'})
    print(subjectWiseMarks)
    subjectWiseMarks['total']=0
    for x in subject_names:
        subjectWiseMarks[x+'_marks']=subjectWiseMarks[('studentmarks',   x, 'r')]+subjectWiseMarks[('studentmarks',   x, 'w')]+subjectWiseMarks[('studentmarks',   x, 'l')]
        subjectWiseMarks[x+'_maxmarks']=subjectWiseMarks[('questionmarks',   x, 'r')]+subjectWiseMarks[('questionmarks',   x, 'w')]+subjectWiseMarks[('questionmarks',   x, 'l')]
        subjectWiseMarks[x+'_rank']=subjectWiseMarks[x+'_marks'].rank(ascending=0,method='min')
        subjectWiseMarks['total'] = subjectWiseMarks['total']+subjectWiseMarks[x+'_marks']
    subjectWiseMarks['percentile']=subjectWiseMarks.total.rank(pct=True)*100
    subjectWiseMarks = subjectWiseMarks.sort_values(['total'], ascending=False)
    subjectWiseMarks['rank']=subjectWiseMarks['total'].rank(ascending=0,method='min')
    subjectWiseMarks.reset_index(inplace=True)
    subjectWiseMarks.columns = [''.join(col).strip() for col in subjectWiseMarks.columns.values]
    print(subjectWiseMarks.columns)
    print(subjectWiseMarks)
    subjectWiseMarks.to_csv(papercode+"_result.csv")
    return subjectWiseMarks.to_json(orient="records")
