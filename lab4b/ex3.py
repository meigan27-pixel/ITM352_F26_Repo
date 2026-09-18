#get a url from the user, clean it and extract the domain name and top level domain
#Name: Meigan Mitsuyoshi
#sept. 18, 2026

url = input("Enter a URL: ")

cleanUrl = url.replace("https://", "")
cleanUrl = cleanUrl.replace("/", "")
print("Cleaned URL:", cleanUrl)

parts = cleanUrl.split(".")
print("parts are:", parts)

domain = parts[1]
tld = parts[2]
print("Domain name is:", domain)
print("Top level domain is:", tld)