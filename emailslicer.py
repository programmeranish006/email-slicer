





email=input("enter your email address: ")


atind=email.index("@")


username=email[:atind]
domain=email[atind+1:]



print("Username: ",username)
print("Domain: ",domain)
