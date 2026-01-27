import pandas as pd 
                                  
df = pd.read_csv("students.csv")             #Importing csv file raw student data for analysis of students 
print(df)

print(df.groupby("City")["Percentile"].mean())     #Checking City wise average marks of Student 

print(df.groupby("City").agg(
    Average_percentile = ("Percentile","mean"),          #Checking all Maximum and Minimum , Average marks of student for better
    Maximum_percentile = ("Percentile","max"),           #analyizing the performance city wise of student 
    Minimum_percentile = ("Percentile","min")
))

result = df.groupby(["City","Gender"]).agg(                #Checking all Average, Maximum and Minimum percentile City and Gender wise
    Average_Percentile = ("Percentile","mean"),           #to check which is making best performance Female or Male city wise 
    Maximum_Percentile = ("Percentile","max"),
    Minimum_Percentile = ("Percentile","min")
)

result = result.reset_index()                      
print(result)

Top_Student_index = result["Maximum_Percentile"].idxmax()           #checking top student percentile and which city he belong                
print(result.loc[Top_Student_index])

Lower_Student_index = result["Minimum_Percentile"].idxmin()        #checking lower percentile student and which city he belong 
print(result.loc[Lower_Student_index])


print("\nINSIGHTS SUMMARY:")
print("1. City-wise performance comparison completed.")
print("2. Gender-based performance analyzed across cities.")
print("3. Top and lowest performing student groups identified.")
print("4. This analysis can help institutions improve academic planning.")

