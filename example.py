from src.VKMSGStats.VKMSGStats import VKMSGStat

#Create object with your login and password
vk = VKMSGStat('example@site.com', 'examplePassword')

#Check if connection was successful
if vk.noProblem:

    #Get stats for user
    vk.getUserStats(12345678)

    #Print beauty output data
    vk.printStats()

else:
    print("Error")