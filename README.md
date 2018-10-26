#### Nirbhaya and many others continue to suffer in our society because of a few ruthless people who often manage to escape unpunished. It is high time that we develop something that not only allows us to identify the culprits but also to catch them before it gets too late. ####

Considering the fact that the ways and means adopted by the culprits for performing such crimes in public transport often  involve activities like  - 
* Bus taking a detour especially  at night time, 
* Buses circling around the same location repeatedly, 
* Haulting of bus in an isolated area, 
* Holding people as hostage when number of  passengers are too less inside the bus.
We can develop a software that will use route monitoring and computer vision along with deep learning to identify a suspicious bus.

Features : 
The predefined route of the bus would be fed into to the system.The bus route would be constantly monitored through gps and any significant detour or suspicious activity would alert the system which will activate the camera installed inside the bus. Using the information received from the camera our software will calculate the probability of a suspicious activity considering various parameters like -
* Population inside the bus, 
* Presence of any weapon, 
* Expressions ( worried/scared/angry) , 
* Loud shrieks
 Keeping in mind these parameters along with the real-time traffic state ( red lights/jam) , working state of the camera ( switched off means suspicious) and many other factors, the concerned authority/police will be informed along with the current location of the bus so that the necessary actions could be taken asap. 

Constraints :
* Cameras and gps chips need to be installed in buses
* Budget available (high cost of CCTVs)
* Time duration for which the camera should be kept active 

Known Issues :
* It is difficult to differentiate a breakdown of the bus from a suspicious activity. Hence a breakdown might lead to false predictions.
* Determination of the permissable extent of detour
