import string
import random

print ("Script by MrHydden.")

pwc = list(string.ascii_letters + string.digits + "!@#$%^&*()")

def grp():

	lng = int(input("Choose your password length: "))

	random.shuffle(pwc)
	

	pw = []
	for i in range(lng):
		pw.append(random.choice(pwc))


	random.shuffle(pw)



	print("".join(pw))



grp()