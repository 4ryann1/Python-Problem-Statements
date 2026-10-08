# Problem 19: Create a Movie class with title, director, and rating. 
# Create display_details(), update_rating(), and is_hit(). 
# A rating of 8 or above is a hit.

# Goal: Combine state changes and decisions using object data.

class Movie:
    def __init__(self, title, director, rating):
        self.title = title
        self.director = director
        self.rating = rating

    def display_details():
        print(f"Movie Name: {self.title}")
        print(f"Director: {self.director}")
        print(f"Rating: {self.rating}")

    def update_rating(rating):
        # self.rating = rating
        print("Rating",rating)

    def is_hit(rating):
        if rating>=8 and rating<=10:
            print(f"The movie is a hit with the rating of: {rating}.")
        else:
            print("The movie was a flop.")

jawan = Movie("Jawan","Atlee","8.5")
jawan.display_details()
jawan.is_hit(8.5)
jawan.update_rating(9.0)