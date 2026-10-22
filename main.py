import csv
# comma seperated value

with open("YA_Books.csv", mode="r", encoding="utf-8") as bookfile:
     # mode "r" means read
     # as bookfile means alias/nickname
     books = csv.reader(bookfile)
     # skip the header row
     #next is skip
     next(books)

    # author colomn is index 1
     min_year = 0
     worst_rating = 5
     pages = 0
     least_pages = 600
     best_rating = 0

     for row in books:
    # print out only authors that start with "M"
    #if row[1].startswith("M"):
    #print(row[1])


        # print out last names: (slice)
        # authorname = row[1]
        # lastindex = row[1].rfind(" ")
        # lastname = authorname[lastindex + 1]
        # if lastname.startswith("V"):
        # print(authorname[lastindex + 1:])
        

        # find most recent book (highest number)
        # : means then
        # year = int(row[2])
        # if min_year < year:
        #     min_year = year
        #     most_recent_book = row
        
        # get the book with the worst rating

        rating = float(row[6])
        if worst_rating > rating:
             worst_rating = rating
             worst_book = row

         # highest rating
        rating = float(row[6])
        if best_rating < rating:
              best_rating = rating
              most_rated = row


            
        most_pages = int(row[5])
        if pages < most_pages:
            pages = most_pages
            the_pages = row
            

        no_pages = int(row[5])
        if least_pages > no_pages:
             least_pages = no_pages
             notalot_pages = row
             


print( f" Highest rated book: \n {best_rating}")

print ( f" Lowest rated book: \n{worst_rating}")

print( f" Most pages: \n{pages}")

print ( f" Least amount of pages: \n{least_pages}")

print( f" The difference is : \n{pages - least_pages}")