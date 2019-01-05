#code challenge on regular expression
"""
  Problem Statement:
    We have to bring together the information of two files.
    In the first file, we have a list of nearly 15000 lines of post codes with the
    corresponding city names plus additional information.

    The other file contains a list of the 19 largest German cities.
    Each line consists of the rank, the name of the city, the population,
    and the state (Bundesland):
    
    Our task is to create a list with the top 19 cities,
    with the city names accompanied by the postal code.
    If you want to test the following program,
    you have to save the list above in a file called largest_cities_germany.txt
    and you have to download and save the list of German post codes

  Output:
    The output of this file looks like this,
    but we have left out all but the first three postal codes for every city:
    
        Berlin {'10715', '13158', '13187', ...}
        Hamburg {'22143', '22119', '22523', ...}
        München {'80802', '80331', '80807', ...}
        Köln {'51065', '50997', '51067', ...}
        Frankfurt am Main {'65934', '60529', '60308', ...}
        Essen {'45144', '45134', '45309', ... }
        Dortmund {'44328', '44263', '44369',...}
        Stuttgart {'70174', '70565', '70173', ...}
        Düsseldorf {'40217', '40589', '40472', ...}
        Bremen {'28207', '28717', '28777', ...}
        Hannover {'30169', '30419', '30451', ...}
        Duisburg {'47137', '47059', '47228', ...}
        Leipzig {'4158', '4329', '4349', ...'}
        Nürnberg {'90419', '90451', '90482', ...}
        Dresden {'1217', '1169', '1324', ...}
        Bochum {'44801', '44892', '44805', ...}
        Wuppertal {'42109', '42119', '42287', ...}
        Bielefeld {'33613', '33607', '33699', ...}
        Mannheim {'68161', '68169', '68167', ...}
      
  Hint:
    Using Regular Expression
    zuordnung_plz_ort.csv
    list of nearly 15000 lines of post codes with the corresponding city names
    plus additional information.
"""
import re

largest_cities = open('largest_cities_germany.txt','r')
cities_data = open('post_codes_germany.txt')

post_data = cities_data.read()
cities_list = largest_cities.readlines()

#To find filter city name form file
expr1 = re.compile('\s[\w\s]+\s+')

#Dictionary to store final data 
final_data={}

for city in cities_list:
    zip_list =[]
    z=expr1.findall(city)
    x=z[0].strip()
    
    expr2 = x+'\s[\d]+\s'
    final = re.findall(expr2,post_data)
    
    for counter in range(3):
        data = final[counter].replace(x,'').strip()
        zip_list.append(data)
    final_data[x]=zip_list
    
print(final_data)
        
    
