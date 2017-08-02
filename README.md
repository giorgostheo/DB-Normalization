**---WORK IN PROGRESS!---**
# Database normalization script
***

#### OVERVIEW

Script made for automating the process of finding the candidate keys in a database, identifying the normal form that is used in said database and then turning it in a BCNF database.


#### Candidate key identification.

The algorithm that is used is the following:
Two lists are used, one for checking if the algorithm needs to stop (when said list is full , which means that all the keys are part of the needed dependencies) and one for storing the keys that are part of the candidate key. The algorithm is executed multiple times if there are multiple candidate keys in the database. For every key that is a part of the list that stores the candidate key, the algorithm checks if that key is capable of generating other keys (checks the dependencies from the input). If so , the keys that are generated from the key , if they are not a part of the list already, are added to that same list (because we will eventually check those too for being able to generate keys), and the key that we checked is added to the candidate key.If not then we check if the key is part of a double dependency (ex. 12-34) in which case we also check for the second key of the dependency. If said key is after our first key , then we add both of them to the candidate key , and the keys that they produce to the checking list. If the key is not a part of a double dependency, we check if it is the last key in our list. That means we have to generate a key that is capable of producing other keys, which in turn means that there is a chance that there are multiple candidate keys in our database (because there might be multiple keys that are capable).If that is not the case either , then the algorithm just checks the next key. After every iteration , the checklist is compared with a "full" list and if the are found to be the same (our list is also full) , our list is added to a "master" list of all the candidate keys.

#### Normal form identification.
Starting from the second normal form (checking if the first normal form is used is considered redundant) we check if the conditions of that form are met , proceeding to the next one after that. If not we stop the algorithm and we set the last normal form as the one that is used. The  Boyce Codd normal form is the last one to be checked, after the third normal form.

#### Boyce Codd "transformation". (needs work!)

The candidate key is used to turn the database to a BCNF database.







