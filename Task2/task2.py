# Movies Budget Analysis

def analysis_movies(movies):

    total = 0
    for title, budget in movies:
        total += budget
    average = total / len(movies)
    print(f"Average Budget = ${average:,.0f}")

    above = []
    below = [] 

    for title, budget in movies:
        difference = budget - average
        if difference > 0:
            above.append((title, difference))
        else:
            below.append((title,difference))

    print("Movies ABOVE average:")
    for title, diff in above:
        print(f"  {title} (+${diff:,.0f})")

    print("Movies BELOW average:")
    for title, diff in below:
        print(f"  {title} (-${diff:,.0f})")


movies = [
    ("Hera Pheri", 20000000),
    ("Bhool Bhulaiya", 9000000),
    ("Dhol", 4500000),
    ("Khatta Meetha", 7900000),
    ("Chup Chup Ke", 3650000),]
  

analysis_movies(movies)
