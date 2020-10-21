#If you want to overwrite a file("w") append a file("a") or read a file("r").

JobFile = open("CommunityServiceVolunteers.txt", "a")

JobFile.write("\nCommunity Service")

JobFile.close()