## Robottas 
#### F1 Fantasy Market Mover Bot


![image](https://pbs.twimg.com/profile_images/1124674147257409537/0-vR0EBc_400x400.jpg)



#### Done
- create new account, login
- get all current driver prices and status
- get driver add buton xpaths
- store newly created accounts in accounts.xlsx
- replace button xpath on login page with id or something else (DONE)
- select driver buttons from an xpath stored in the driver dataframe (DONE)
- fix names with accents (DONE (scottish names lol))
- fix pageload system to make shit faster
- only choose countries from those that are actually available
- zoom out to capture all drivers in list (using keypress action chains)
- Headless mode (add option=options headless)
- Run concurrent instances (using supervisord in linux with robottas.conf)


#### TODO

- Proper error loggin for all concurrent instances
- Some kind of tracker that keeps track of how many votes are cast
- weird xpaths (PARTIALLY DONE)

- make sure you can't spend more than 100m (works, but buggy)

- dockerize the whole thing and get it running on the cloud 

- create an alternative function just to monitor prices (and graph them, maybe? hosted online somewhere?)
- idea is to run a single instance of robottas with just read capabilities in the clooud and have it update a github pages site, interacting with github through python
- store prices in excel per cycle to track changes over time 


Someday:
- create another function to login using existing accounts and push prices of drivers I hate down (screw you LH, doin my boy albon dirty like that)




