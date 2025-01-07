def determineEligiblity_tograduate(name,credits,gpa,satscore):
    if credits >= 120 and gpa >= 2.0 and satscore >=800:
        print(f"{name} is eligble to graduate")
    else:
        print(f"{name} is not eliablge to graduate")


def listOfMovies(name,price,genre):
    print(f"{name} is a {genre} movie and costs $ {price}")
    if genre == 'comedy':
        print('you will laugh a lot')
    elif genre == "horror":
        print('ypu will be scared')
    else:
        print('you will enterained')

determineEligiblity_tograduate('alice',120,2.0,800)
determineEligiblity_tograduate('bob',119,1.9,799)