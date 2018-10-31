import csv #we import csv before we can use the csv module


	
	
def player(): # out the Raptor team into a file as required
	with open("teams.txt","a") as file:
		file.write("Raptors \n")
		for players in Raptors:
			players=",".join(players)
			file.write ("\n" "\n"+ str(players ))
		
				 
def player1(): # output the Dragons team into a file as required
	with open("teams.txt","a") as file:
		file.write('\n' '\n' "Dragons")
		for player2 in Dragons:
			player2=",".join(player2)
			file.write ("\n" "\n"+ str(player2))
							
	
def player3():# output the Sharks team into a file as required
	with open("teams.txt","a") as file:
		file.write( '\n' '\n' "Sharks")
		for player4 in Sharks:
			player4=",".join(player4)
			file.write ("\n" "\n"+ str(player4))
				
				
if __name__ == '__main__':
	with open('soccer_players.csv',newline='') as csvfile:# open the file as a string
		soccer_reader = csv.reader(csvfile) #  read what is in the file before we can use the file
		rows = list(soccer_reader) # Convert the file into a list
		del(rows[0]) # delete the first row which contains just the headings, to make access easier	
		Experienced = [] # define an empty list of experienced players
		Inexperienced = [] #define an empty list of inexperienced players
		Raptors = [] #define an empty list of the Raptors team
		Dragons = [] #define an empty list of the Dragons team
		Sharks = [] #define an empty list of the Sharks team
		
	
	for row in rows: # loop the through the player list
		if row[2]=='YES': # sought out the experienced players
			Experienced.append(row) # convert  the experienced players into a list
		else:
			Inexperienced.append(row) # sought out the inexperienced players
	Raptors = Experienced[:3] + Inexperienced[:3] # divide the players evenly and assign them into the various teams
	Dragons = Experienced[3:6] + Inexperienced[3:6]
	Sharks = Experienced[6:] + Inexperienced[6:]
	
	player()			
	player1()
	player3()
		
			



