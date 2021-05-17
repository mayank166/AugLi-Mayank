import matplotlib.pyplot as plt

class student:
    def __init__(self, name, international_rank, national_rank, school_rank, marks):
        self.name = name
        self.international_rank = international_rank
        self.national_rank = national_rank
        self.school_rank = school_rank
        self.marks = marks
        self.percentage = marks/40

list = []
list.append(student ("Sachin", 2000, 1000, 500, 32))
list.append(student ("Mayank", 1000, 500, 250, 38))
list.append(student ("Kamal", 1500, 750, 450, 35))
list.append(student ("Anjali", 500, 200, 1, 39))
list.append(student ("Gayatri", 2500, 1500, 750, 28))
list.append(student ("Siddhant", 300, 100, 1, 40))

#Calculating National Average Score
total_marks = 0
count = 0
for s in list:
    count = count + 1
    total_marks += s.marks
national_avg_score = total_marks/count
national_avg_percentage = national_avg_score/40

#Search by name
val = input("Name: ")
i = 0
for s in list:
    if (val == s.name and i == 0):
        print("International Rank: ", s.international_rank)
        print("National Rank: ", s.national_rank)
        print("School Rank: ", s.school_rank)
        print("Marks: ", s.marks, "/40")
        left = [1, 2]
        height = [s.percentage, national_avg_percentage]
        tick_label = [s.name, "Average Participant"]
        plt.bar(left, height, tick_label = tick_label, width = 1, color = ['red', 'green'])
        plt.show()
        i = 1        
if (i == 0):
    print("Not found")
print("National Average Score: ", national_avg_score, "/40")

#Creating Bar Graphs

    
        
        
    
