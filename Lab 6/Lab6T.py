"""
Lab 6: Student DemoGraphics
cs107
Haverford College

Danylo Shudrenko

!IMPORTANT NOTE:
JackC was mentioned in csv file twice,
so I deleted one of the copies

!!!!!!!!!!!Misinformation/Disinformation!!!!!!!!:
I tried several things to create misiformation. First of all, I tried to change the name of course,
or section insignificantly, so it wiill be not noticed by a person, but definetly noticed by the
program. For example, instead of "CMSCH107A" I put "CSMCH107A". Apparently, students didn't
follow the same format, so I could see both name variations of this course in the table
(the information initially was misleading hehehe :0)
Secondly, I tried to the information about one studet twice, in this case function like
neighbour count started to provide incorrect information
Finally, I tried to change different functions. For example, I switched the return in the
function connected, which automatically made other functions to provide misinformation




>>> G = LoadGraph()                     # initialize graph from external file

My test:
#representation
>>> print(G)
{'LoganS': ['CHEMH310E', 'CHEMH352D', 'CHEMH355E', 'CHEMH362A', 'CHEMH391J', 'CMSCH107A'], 'CHEMH310E': ['LoganS'], 'CHEMH352D': ['LoganS'], 'CHEMH355E': ['LoganS', 'MimiL'], 'CHEMH362A': ['LoganS'], 'CHEMH391J': ['LoganS'], 'CMSCH107A': ['LoganS', 'GeorgeM', 'DerekZ', 'JaxonR', 'AlexS', 'IsabelleA'], 'ConradC': ['SPANH100', 'CMSCH107', 'PHILH107', 'SOCLH155'], 'SPANH100': ['ConradC'], 'CMSCH107': ['ConradC'], 'PHILH107': ['ConradC', 'DeanW'], 'SOCLH155': ['ConradC'], 'JackC': ['CSMCH107A', 'ASTRH204A', 'PHYSH308A', 'PHYSH399F', 'PHYSH412F'], 'CSMCH107A': ['JackC', 'OliverF', 'BeccaL', 'WillBC', 'LeoG', 'DanS', 'BenJ', 'OwenY', 'ErinD', 'RyanR', 'DaniyalA', 'MimiL', 'SuzanneL'], 'ASTRH204A': ['JackC'], 'PHYSH308A': ['JackC', 'AlexS'], 'PHYSH399F': ['JackC'], 'PHYSH412F': ['JackC'], 'OliverF': ['CSMCH107A', 'JNSEH001A', 'MATHH215A', 'WRPRH156A'], 'JNSEH001A': ['OliverF'], 'MATHH215A': ['OliverF', 'BenJ', 'RyanR', 'DaniyalA'], 'WRPRH156A': ['OliverF', 'LeoG'], 'BeccaL': ['CSMCH107A', 'ASTRH341A', 'PHYSH211F', 'HARTB103', 'ARTSH104D'], 'ASTRH341A': ['BeccaL'], 'PHYSH211F': ['BeccaL'], 'HARTB103': ['BeccaL'], 'ARTSH104D': ['BeccaL'], 'WillBC': ['CSMCH107A', 'LATNH102A', 'MATHH118A', 'WRPRH150A', 'MUSCH216F', 'PEH532'], 'LATNH102A': ['WillBC'], 'MATHH118A': ['WillBC', 'LeoG', 'JaxonR'], 'WRPRH150A': ['WillBC', 'BenJ', 'OwenY'], 'MUSCH216F': ['WillBC'], 'PEH532': ['WillBC'], 'LeoG': ['CSMCH107A', 'ECONH105A', 'MATHH118A', 'PEH100', 'WRPRH156A'], 'ECONH105A': ['LeoG', 'DerekZ'], 'PEH100': ['LeoG'], 'DanS': ['ARTTB253', 'CHEMH111A', 'CSMCH107A', 'MATHB201', 'PEH102', 'PEH112', 'SPANH001A'], 'ARTTB253': ['DanS'], 'CHEMH111A': ['DanS', 'GeorgeM'], 'MATHB201': ['DanS'], 'PEH102': ['DanS'], 'PEH112': ['DanS'], 'SPANH001A': ['DanS', 'JaxonR'], 'BenJ': ['CSMCH107A', 'MATHH215A', 'SPANH101A', 'WRPRH150A'], 'SPANH101A': ['BenJ', 'ErinD'], 'GeorgeM': ['CHEMH111A', 'LATNH001A', 'CMSCH107A', 'WRPRH120A'], 'LATNH001A': ['GeorgeM'], 'WRPRH120A': ['GeorgeM'], 'OwenY': ['CSMCH107A', 'ECONB105', 'MATHH121A', 'WRPRH150A', 'PEH562'], 'ECONB105': ['OwenY'], 'MATHH121A': ['OwenY', 'ErinD', 'DerekZ'], 'PEH562': ['OwenY'], 'ErinD': ['MATHH121A', 'CSMCH107A', 'ANTHH106A', 'SPANH101A'], 'ANTHH106A': ['ErinD'], 'DerekZ': ['CMSCH107A', 'CNSEB101', 'ECONH105A', 'MATHH121A'], 'CNSEB101': ['DerekZ'], 'DeanW': ['CSMCH107', 'HISTH226', 'PHILH107', 'CMSCB231'], 'CSMCH107': ['DeanW'], 'HISTH226': ['DeanW'], 'CMSCB231': ['DeanW'], 'JaxonR': ['CMSCH107A', 'MATHH118A', 'PHILH108A', 'SPANH001A'], 'PHILH108A': ['JaxonR'], 'RyanR': ['CSMCH107A', 'ECONH201A', 'MATHH215A', 'PHILH242A'], 'ECONH201A': ['RyanR', 'DaniyalA'], 'PHILH242A': ['RyanR'], 'AlexS': ['CMSCH107A', 'PHYSH308A', 'ECONH298A', 'MEAM3540'], 'ECONH298A': ['AlexS'], 'MEAM3540': ['AlexS'], 'DaniyalA': ['CSMCH107A', 'ECONH201A', 'MATHH215A', 'PHILH238A'], 'PHILH238A': ['DaniyalA'], 'MimiL': ['CSMCH107A', 'CHEMH355E', 'CHEMH301A', 'MATHH204A', 'CHEMH304A'], 'CHEMH301A': ['MimiL'], 'MATHH204A': ['MimiL'], 'CHEMH304A': ['MimiL'], 'IsabelleA': ['CMSCH107A', 'LINGH208A', 'LINGH215A', 'LINGH299A'], 'LINGH208A': ['IsabelleA'], 'LINGH215A': ['IsabelleA'], 'LINGH299A': ['IsabelleA'], 'SuzanneL': ['CSMCH107A', 'CSMCH105A', 'MUSCH255A'], 'CSMCH105A': ['SuzanneL'], 'MUSCH255A': ['SuzanneL']}

#connected method
>>> assert G.connected('LoganS', 'CHEMH310E')
>>> assert G.connected('ConradC', 'SPANH100')
>>> assert G.connected('JackC', 'ASTRH204A')
>>> assert not G.connected('ConradC', 'CHEMH310E')
>>> assert not G.connected('ConradC', 'JackC')

#neighbour_count
>>> print(G.neighbor_count('LoganS'))
6
>>> print(G.neighbor_count('ConradC'))
4
>>> print(G.neighbor_count('JackC'))
5

#list_nodes
>>> print(G.list_nodes())
['LoganS', 'CHEMH310E', 'CHEMH352D', 'CHEMH355E', 'CHEMH362A', 'CHEMH391J', 'CMSCH107A', 'ConradC', 'SPANH100', 'CMSCH107', 'PHILH107', 'SOCLH155', 'JackC', 'CSMCH107A', 'ASTRH204A', 'PHYSH308A', 'PHYSH399F', 'PHYSH412F', 'OliverF', 'JNSEH001A', 'MATHH215A', 'WRPRH156A', 'BeccaL', 'ASTRH341A', 'PHYSH211F', 'HARTB103', 'ARTSH104D', 'WillBC', 'LATNH102A', 'MATHH118A', 'WRPRH150A', 'MUSCH216F', 'PEH532', 'LeoG', 'ECONH105A', 'PEH100', 'DanS', 'ARTTB253', 'CHEMH111A', 'MATHB201', 'PEH102', 'PEH112', 'SPANH001A', 'BenJ', 'SPANH101A', 'GeorgeM', 'LATNH001A', 'WRPRH120A', 'OwenY', 'ECONB105', 'MATHH121A', 'PEH562', 'ErinD', 'ANTHH106A', 'DerekZ', 'CNSEB101', 'DeanW', 'CSMCH107', 'HISTH226', 'CMSCB231', 'JaxonR', 'PHILH108A', 'RyanR', 'ECONH201A', 'PHILH242A', 'AlexS', 'ECONH298A', 'MEAM3540', 'DaniyalA', 'PHILH238A', 'MimiL', 'CHEMH301A', 'MATHH204A', 'CHEMH304A', 'IsabelleA', 'LINGH208A', 'LINGH215A', 'LINGH299A', 'SuzanneL', 'CSMCH105A', 'MUSCH255A']

#list_neighbours
>>> print(G.list_neighbors('MimiL') )
['CSMCH107A', 'CHEMH355E', 'CHEMH301A', 'MATHH204A', 'CHEMH304A']
>>> print(G.list_neighbors('BenJ') )
['CSMCH107A', 'MATHH215A', 'SPANH101A', 'WRPRH150A']
>>> print(G.list_neighbors('DanS'))
['ARTTB253', 'CHEMH111A', 'CSMCH107A', 'MATHB201', 'PEH102', 'PEH112', 'SPANH001A']
>>> print(G.list_neighbors('OwenY'))
['CSMCH107A', 'ECONB105', 'MATHH121A', 'WRPRH150A', 'PEH562']
>>> print(G.list_neighbors('DerekZ'))
['CMSCH107A', 'CNSEB101', 'ECONH105A', 'MATHH121A']

#size
>>> print(G.size())
81

#common courses
>>> print(G.common_courses('BenJ','DanS'))
['CSMCH107A']

>>> print(G.common_courses('DerekZ','OwenY'))
['MATHH121A']

#who_is_taking
>>> print(G.who_is_taking('CSMCH107A'))
['JackC', 'OliverF', 'BeccaL', 'WillBC', 'LeoG', 'DanS', 'BenJ', 'OwenY', 'ErinD', 'RyanR', 'DaniyalA', 'MimiL', 'SuzanneL']

>>> print(G.who_is_taking('CMSCH107A'))
['LoganS', 'GeorgeM', 'DerekZ', 'JaxonR', 'AlexS', 'IsabelleA']

>>> print(G.who_is_taking('MATHH121A'))
['OwenY', 'ErinD', 'DerekZ']

#PopularNode
>>> print(Popular_Node(G, 1))
CSMCH107A
>>> print(Popular_Node(G, 2))
DanS
>>> print(Popular_Node(G, 3))
WillBC
>>> print(Popular_Node(G, 4))
CMSCH107A
>>> print(Popular_Node(G, 5))
LoganS
"""

from Graph import *         # get the graph class
import csv                  # to access the functions for CSV file access

def LoadGraph():
    g = graph()
    with open('StudentCourseData.csv', 'r') as f:   
        r = csv.reader(f)   
        for entry in r:
            if entry[0] != 'Timestamp':
                g.add_node(entry[1])
                for index in range(2, len(entry)):
                    if entry[index] != '':
                        g.add_node(entry[index])
                        g.link(entry[index], entry[1])
        f.close()
    return g

#preconditions
#function Popular_Node accepts two variable "g" - graph, "n" - interger, the nth largest element is searcjed for
def Popular_Node(g, n):
    nodelist = g.list_nodes() #finding the node list for the graph
    popularitylist=[] #setting up the list, which is would be examined later
    for node in nodelist: #for all nodes
        popularitylist.append([g.neighbor_count(node), node]) #creating the pair of the amount of neighbors(popularity)
        #and the value of node
    #subfunction howtosort is used to sort the popularity list only by popularity of nodes
    def howtosort(val):
        return val[0]

    popularitylist.sort(key=howtosort) #sorting the list
    return popularitylist[-n][1] #finding the nth element
#postcondition
#the function Popular_Node returns the nth popular node based on the amount of its neighbor
#if several nodes have the same value of popularity, it would return one of them
"""
WHAT DO I NEED TO FIND THE Nth POPULAR COURSE? 
To do that, I need to be able to distinguish nodes, which are students and courses
To implement it, I can create a second representation of the graph, where
for each node I would create a marker if it is student or course
Please see preudocode

def __init__(self): #constructor   
    self.rep = {}
    self.marker = {} #seting second representation
    
and later when I will add nodes, I will need, one more value in method, see below: 


 def add_node(self, node, marker):   
     if not node in self.rep:
        self.rep[node] = [] 
        self.marker[marker] = marker #marking each of the node as a student or course
        
and I will create one more method 

def if_course(self, node):
    if self.marker[node] == "course":
        return True
    else: 
        return False
        
Hence, I would be able to check if the node is course, 
and examine only course in the function Popular_Node
"""




if __name__ == "__main__":
    import doctest
    doctest.testmod()
    print("Lab 6 tests completed")

""" This is the external CSV file for testing
Timestamp,"The name to use for you, first name then the initial character of your last name (e.g., the instructor is ""JohnD"") -- no spaces, only alphabetic characters, and please be consistent.","Here is my FIRST course, following the BIONIC convention with no spaces (e.g., this course is ""CSMCH107A"")","Here is my SECOND course, following the BIONIC convention with no spaces (e.g., this course is ""CSMCH107A"")","Here is my THIRD course, following the BIONIC convention with no spaces (e.g., this course is ""CSMCH107A"")","Here is my FOURTH course, following the BIONIC convention with no spaces (e.g., this course is ""CSMCH107A"")","Here is my FIFTH course, following the BIONIC convention with no spaces (e.g., this course is ""CSMCH107A"")","Here is my SIXTH course, following the BIONIC convention with no spaces (e.g., this course is ""CSMCH107A"")","Yes, I have a SEVENTH course, following the BIONIC convention with no spaces (e.g., this course is ""CSMCH107A"")"
11/24/2021 12:01:30,MaryD,CMSCH107A,MATHH215A,,,,,
11/28/2021 8:05:59,JD,CMSCH107A,CMSCH399A,CMSCH480A,,,,
11/28/2021 8:06:57,SuzanneL,CMSCH107A,,,,,,
"""


