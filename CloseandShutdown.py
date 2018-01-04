#################################################
#												#
#	Name: Close and Shutdown 					#
#	Dates: 04/01		                   	    #
#   Ver: 1.0.0             						#
#	- Pulls list of potential opened software 	#
#	- Uses shutdown function					#
#                                           	#
#   Next Edits                              	#
#   - Pulls all current processes				#
#	- Add a regsitery for the list				#
#	        							    	#
#################################################

import subprocess
import os

# List of exes
ExeNames = ['Spotify', 'Outlook', 'chrome', 'winscp', 'Shutdown']

# Input methods
YesWays = ['yes', 'ok', 'sure', 'yerp', 'y', 'ya']

# Shutdown function
# Needs to be above where it's been called
def Shutdown(ShutdownInput):
	if ShutdownInput == "Yes":
		# Shutsdown the computer in 15 seconds
		os.system("shutdown -s -t 15")
	else:
		Exit = input("All programs are closed, press close to exit")

# For loop - Will loop though each item in the object list (array)
for ExeNames in ExeNames:

	# As Shutdown is last in the array this will function after the software closes
	if ExeNames == "Shutdown":

		ShutdownInput = input("Do you wish to shutdown? ")

		if ShutdownInput in YesWays:
			# Passes the yes parameter, this will activate the first function (from the if statement)
			Shutdown( "Yes" )
		else:
			# Passes the no parameter, this will activate the second function (from the if statement)
			Shutdown( "No" )

	else:

		# Accept's users input
		Close = input("Do you wanna close %s " % ExeNames)
	
		# Try and except for error grabbing
		try:
			# If the item is in the object / array
			# else write it as "if Close == "yes""
			if Close in YesWays:
				os.system("taskkill /f /im  %s.exe" % ExeNames)
				print ("%s" % ExeNames, "has been closed")
	
		except:
			print ("Error closing %s" % ExeNames)
			Exit = input("Press close to exit")

# The purpose of this script was pratice and so I can easily force close my applications