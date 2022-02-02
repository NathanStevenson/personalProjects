# Nathan Stevenson

# Set up for finding classes dependent on entered time and department
filename = "CS1212Data.csv"
class_csv = open(filename)
class_dictionary = {}

for row in class_csv:
    classes = row.strip().split(",")
    class_name = classes[9]
    department = classes[1]
    class_number = classes[2]
    credit_number = classes[5]
    time_info = classes[7]
    class_id = classes[0]
    professor = classes[6]
    class_dictionary[class_id] = [class_name, department + " " + class_number, credit_number, time_info, professor]

# Questions for user
desired_start_time = input("What start time are you looking for (specify am or pm): ")
desired_end_time = input("What end time are you looking for (specify am or pm): ")
time_range = desired_start_time + " - " + desired_end_time
specified_department = input("Would you like to specify a department? If not hit Enter: ")

# Output
if specified_department != "":
    for classes in class_dictionary:
        if time_range in class_dictionary[classes][3] and specified_department.lower() in class_dictionary[classes][1].lower():
            print(class_dictionary[classes][0] + ": " + class_dictionary[classes][1] + "\n" + "Time: " +
                  class_dictionary[classes][3] + "\n" + "Credits: " + class_dictionary[classes][2] + "\n" +
                  "Professor: " + class_dictionary[classes][4])
            print("----------------------------------------------")

if specified_department == "":
    for classes in class_dictionary:
        if time_range in class_dictionary[classes][3]:
            print(class_dictionary[classes][0] + ": " + class_dictionary[classes][1] + "\n" + "Time: " +
                  class_dictionary[classes][3] + "\n" + "Credits: " + class_dictionary[classes][2] + "\n" +
                  "Professor: " + class_dictionary[classes][4])
            print("----------------------------------------------")

class_csv.close()
