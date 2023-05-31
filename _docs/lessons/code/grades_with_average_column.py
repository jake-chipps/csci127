grades_file = open("grades.csv", "r")
average_file = open("grades-average.csv", "w")

# Create empty list to store unclean strings from csv
uber_list = []

# Loop through each row of file and split string to list
for row in grades_file:
    uber_list.append( row.split(",") )

# Create empty list to store cleaned strings from csv
grades_list = []

# Strip each string and append to each row
# Append each row to cleaned strings list
for row in uber_list:
    row_list = []
    for item in row:
        row_list.append( item.strip() )
    grades_list.append( row_list )

# Append "Average" to first row
# Calculate average for other rows, append average to row
for i in range(len(grades_list)):
    if i == 0:
        grades_list[i].append("Average")
    else:
        sum = 0
        for j in range(len(grades_list[i])):
            if j > 0:
                sum += int(grades_list[i][j])
        grades_list[i].append( str(sum/2) )

# Join list to string, using "," as glue
# Write glued row to output file
for row in grades_list:
    glue = ","
    average_file.write(glue.join(row) + "\n")

grades_file.close()
average_file.close()
