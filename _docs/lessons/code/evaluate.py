# ---------------------------------------
# CSCI 127, Joy and Beauty of Data
# John Paxton
# Last Modified: ??
# ---------------------------------------
# A simple course evaluation system.
# ---------------------------------------

# The missing function goes here.

# ---------------------------------------

def main():
    print("Course Evaluation Program")
    print("-------------------------")
    ratings = ["topic interest", "difficulty estimation", "instructor assessment"]
    course = input("Enter course to evaluate (e.g. CSCI 127): ")
    course_rating = rate_course(ratings)
    print(course, "rating: ", course_rating)
    
    if course_rating >= 70:
        print("Highly recommended!")
    elif course_rating >= 30:
        print("Neutral recommendation")
    else:
        print("Not recommended!")
    
# ---------------------------------------

main()