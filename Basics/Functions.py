
# Function definition
def foo1(parameter1):
    print("hello world")
    print("parameter1= ", parameter1)


def sendEmail(12, 11, 13, repeat=1):
	# prepare the email
	# Send it to the right email address
	# make sure it is successful

    print("12= ", sendEmailAddres)
    print("pass-in Message= ", Message)
    print("pass-in TitleEmail= ", TitleEmail)   
    print("pass-in repeat= ", repeat)   

    return True, repeat

# Usage
# start from here
#parameter1 = 5
#foo1(parameter_in)

sendEmailAddres = "guo95132@gmail.com"
Message = "Hi Dad"
TitleEmail = "Hi"
ret, repeatCnt = sendEmail(sendEmailAddres, Message, TitleEmail, 11)
print("\n")
if ret == True and repeatCnt == 1:
	print("send email successful, 1 time")
elif ret == True and 10 > repeatCnt > 1 :
	print("send email successful, multiple times")
elif ret == True and repeatCnt > 10:
	print("You send too many messages")
else:
	print("send email failed")
