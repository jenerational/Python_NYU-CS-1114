## explains to select pplz how my mind works and why i cant even like anyone anymore

def q1():
    q1q = input("Do I like them? ").lower()
    if (q1q == "yes") or (q1q == "y"):
        return True
    elif (q1q == "no") or (q1q == "n"):
        print("I don't like him and I don't fuck w ppl i don't like.")
        return False
    else:
        print("Who the fuck knows. Let's just continue on anyways.")
        return True
        


def main():
    print("Why I say no:")               
    q1A = q1()
    if q1A == False:
        return
    print("hi") 
    
main() 
