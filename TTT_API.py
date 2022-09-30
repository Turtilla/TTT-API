from bs4 import BeautifulSoup
import requests

def get_plant_dict(plant_name):
    # a function intended for retrieving information about plants matching
    # the user request in a dictionary format name:edibility
    
    # the url/website from which the results are sources
    website = requests.get(url=f"https://www.thetortoisetable.org.uk/plant-database/viewplants/search/?searchtogglestatus=&searchchoice=exactwords&searchtxt={plant_name}&x=0&y=0#.YxI5UXZBzD4").text
    
    # turning the website into a BeautifulSoup object
    soup = BeautifulSoup(website, 'html.parser')  
    # retrieving a list of text elements only pertaining to plants
    plant_contents = list(soup.find(id='content').stripped_strings)[3:]
    
    # creating a list of lists, where every element is one plant
    all_plants = []
    temporary_plant = []
    # the elements can be edibility, plant name, alternative names, Latin
    # names, and 'See More'
    for element in plant_contents:
        if element != 'See More':  # 'See More' delineates separate plants
            temporary_plant.append(element)
        else:  # if it is 'See More'
            all_plants.append(temporary_plant)
            temporary_plant = []
    
    # creating the dictionary to be returned
    plant_dict = {}
    for entry in all_plants:
        edibility = entry[0]
        name = entry[1]
        latin = entry[-1]  # it is always the last entry, but some plants have alternative names as [2] and some do not
        plant_dict[name] = {"edibility":edibility, "latin":latin}
        
    return plant_dict
    