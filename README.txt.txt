The program named "Operator Selection" aims to retrieve the full statistics and details of characters within a certain video game, provided the name of said character and level. Due to the small size of the database CSV file, only certain 
characters are applicable for this program, with rigid levels. For more details, please refer to the database CSV file.

The program named "videogamepageScrapper" aims to retrieve the details of a table containing information on the best
selling video games of all time on a Wikipedia page.



To use "Operator Selection", prepare a text file with the names of the characters you wish to retrieve information on, 
and their respective levels separated by a comma. As an example, refer to the following:

Eyjafjalla, E2L30
SilverAsh, E2Max
...

Then simply run the method TeamCompReader(textfilename, destinationList) with the name of the text file to input the text file and the name of the destination list to store the names and levels of the characters, and selectOperator() to retrieve
character information.

To use "videogamepageScrapper", simply replace the target webpage assigned to videogames_page with the new target URL.