import csv

def baseball_Strikeouts(csv):

    count = 0
    with open(csv, "r") as file:
        for line in file:
            if "strikeout" in line: 
                count = count + 1

    print(count)





    
baseball_Strikeouts(r"C:\Users\mbien\OneDrive\Desktop\programming\savant_data.csv")






