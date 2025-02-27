# import mysql.connector
import streamlit as st
import sqlite3

# conn = mysql.connector.connect(host='', user='root', password='12345',
# database = 'python')
#print(mydb)
#st.write(mydb)
conn = sqlite3.connect('s.db')
cur =conn.cursor()
cur.execute('create table if not exists emp(id text not null primary key , name text, age int)')
#st.write('create successfully')
#cur.execute('show tables')

#for i in cur:
    #print(i)
    #st.wri



with st.form('insert_deta'):
    id = st.text_input('id')
    name = st.text_input('Name')
    age = st.text_input('Age')
    submit_button = st.form_submit_button('Insert deta')
    display_button = st.form_submit_button('display deta')
    # update_deta = st.form_submit_button('update deta')



if submit_button:
    query = 'insert into emp (id, name, age) values(?, ?, ?)'
    cur.execute(query, (id, name, age))
    conn.commit()
    st.success('deta written successfully')
    st.balloons()


if display_button:
    cur.execute('select * from emp')
    for i in cur:
        st.write(i)

user_id = st.text_input('enter id')
new_name = st.text_input('enter name')
new_age = st.text_input('enter age')
if st.button('update'):
    query ='update emp set name = ?, age= ? where id = ?'
    cur.execute(query,(new_name, new_age, user_id))
    conn.commit()
    st.success('deta update successfully')
    st.balloons()


delete_user_id = st.text_input('enteruser id')
if st.button('delete'):
    query ='delete from emp wherw id = ?'
    cur.execute(query, (delete_user_id,))
    conn.commit()
    st.success('deta deleted successfully')
    st.balloons()