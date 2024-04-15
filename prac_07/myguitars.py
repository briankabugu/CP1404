from guitar import Guitar

def main():
    guitars = []
    # Open the file for reading
    in_file = open('guitars.csv', 'r')
   
    # All other lines are language data
    for line in in_file:
        # print(repr(line))  # debugging
        # Strip newline from end and split it into parts (CSV)
        parts = line.strip().split(',')

        # Construct a ProgrammingLanguage object using the elements
        # year should be an int
        language = Guitar(parts[0], int(parts[1]), float(parts[2]))
        # Add the language we've just constructed to the list
        guitars.append(language)
    # Close the file as soon as we've finished reading it
    in_file.close()
    
    guitars.sort()
    # Print the sorted list of guitars
    
    for guitar in guitars:
        print(guitar.name)
main()