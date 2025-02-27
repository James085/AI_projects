text to sql
import google.generativeai as genai
import sqlite3

import os 
os.environ["GOOGLE_API_KEY"]="AIzaSyB82BMvWIPevitjjH6ro2oW9VZVephHvPg"
genai.configure(api_key = os.environ["GOOGLE_API_KEY"])


model = genai.GenerativeModel(model_name = "gemini-pro")


def read_sql_query(sql, db):
    conn = sqlite3.connect(db)
    cur = conn.cursor()
    cur.execute(sql)
    rows = cur.fetchall()
    for row in rows:
        print(row)
    conn.close()





prompt_parts_1=[
    """
    You are an expert in converting English questions to SQL query!
    The SQL database has the name STUDENT and has the following columns - NAME, CLASS, 
    SECTION \n\nFor example,\nExample 1 - How many entries of records are present?, 
    the SQL command will be something like this SELECT COUNT(*) FROM STUDENT ;
    \nExample 2 - Tell me all the students studying in Data Science class?, 
    the SQL command will be something like this SELECT * FROM STUDENT 
    where CLASS="Data Science"; 
    also the sql code should not have ``` in beginning or end and sql word in output

    """


]


def generate_gemini_response(question, input_prompt):
    
    response = model.generate_content([input_prompt, question])
    # print(response.text)
    output = read_sql_query(response.text, "student_db")
    return output


generate_gemini_response("Tell me number of students in DEVOPS",
                    prompt_parts_1[0])