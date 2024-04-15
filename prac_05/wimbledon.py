"""
Game, Set, Match
Estimate: 25 minutes
Actual:   32 minutes
"""

def main():
    lines = []
    filename = "wimbledon.csv"
    #open the file
    with open(filename, "r", encoding="utf-8-sig") as in_file:
        next(in_file)  # Skip the header row
        lines = in_file.readlines()
        data = champions_count(lines)
        countries = get_countries(lines)
        display_champions_and_countries(data, countries)
           
    in_file.close()
    
    
#count number of times champions have won
def champions_count(file):
    data = {}
    for line in file:
           line_array = line.split(",")
           if line_array[2] in data:
               data[line_array[2]] += 1
           else:
               data[line_array[2]] = 1
    return data

#get countries of champions  
def get_countries(file):
    countries = set()

    for line in file:
        line_array = line.split(",")
        print('j')
        countries.add(line_array[1])
        
    for x in countries:
        print(x)

    return countries


#print champions count and countriesa belonging to the champions           
def display_champions_and_countries(data, countries):
    for champion, count in data.items():
        print(f"{champion}: {count}")
  
    countries_str = ", ".join(countries)
    print(f"Countries of champions in alphabetical order: {countries_str}")
    
main()