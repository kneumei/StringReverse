def reverse(s):
	if(len(s)==0):
		return "";
	return s[-1] + reverse(s[0:len(s)-1])

print reverse("Hello World")
print reverse("Here we go.")
print reverse("Code Kata is fun!")