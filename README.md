# TTT-API
This script was created for the Dialogue Systems 2 course at the University of Gothenburg in 2022.  

It is a very simple script intended for extracting information about the edibility of certain plants from [The Tortoise Table](https://www.thetortoisetable.org.uk/index.php#.Yzb1MXZBzD4). It contains one function, get_plant_dict(), which returns a dictionary of plants matching the input string; each plant's value is another dictionary containing their edibility and latin name. Alternative names are not featured, nor are the details as to why the plant is edible or not. In case no match is found, the dictionary is returned empty. Input should be given in the form of a string. (Un)fortunately the search results are not up to the script, but to TTT's search algorithm. 

Example input and output:  
```
>>> import TTT_API as ttt
>>> ttt.get_plant_dict("Cherry")
{
'Laurel': {'edibility': 'Do not Feed', 'latin': 'Prunus laurocerasus'}, 
'Cherry': {'edibility': 'Feed Sparingly', 'latin': 'Prunus spp.'}, 
'Jerusalem Cherry': {'edibility': 'Do not Feed', 'latin': 'Solanum pseudocapsicum'}, 
'Chinese Lantern': {'edibility': 'Do not Feed', 'latin': 'Physalis spp.'}, 
'Heliotrope': {'edibility': 'Do not Feed', 'latin': 'Heliotropium spp.'}, 
'Bay Tree': {'edibility': 'Feed Sparingly', 'latin': 'Laurus nobilis'}
}
```
