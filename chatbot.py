import aiml
import os

#Create the kernel and learn the AIML files
kernel = aiml.Kernel()
if os.path.isfile("bot_brain.brn"):
	kernel.bootstrap(brainFile = "bot_brain.brn")
else:
	kernel.bootstrap(learnFiles = "std-startup.xml", commands="load aiml b")
	kernel.saveBrain("bot_brain.brn")

#Press CTRL-C to break the loop
while True:
	print kernel.respond(raw_input("Enter your message >> "))
