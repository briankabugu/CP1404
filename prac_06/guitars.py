from prac_06.guitar import Guitar

def main():
    guitars = []
    
    # guitar_name = input("Enter guitar name: ")
    # year = input("Enter year guitar was made: ")
    # cost = input("Enter the cost of the guitar: ")
    # guitars.append(Guitar(guitar_name,year,cost))
    
    guitars.append(Guitar("Gibson L-5 CES", 1922, 16035.40))
    guitars.append(Guitar("Line 6 JTV-59", 2010, 1512.9))
    
    
    for i,guitar in enumerate(guitars,1):
      vintage_string = "(vintage)" if guitar.is_vintage() else ""  
      print(f"Guitar {i}: {guitar.name:15} ({guitar.year}), worth ${guitar.cost:10,.2f}{vintage_string}")
      
main()