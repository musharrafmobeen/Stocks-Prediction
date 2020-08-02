import sys
import FacialRecognition as Fr

x = sys.argv[1]

if x=="'SignUp'":
    Fr.SignUp_With_FacialId()

elif x=="'SignIn'":
    Fr.SignIn_With_FacialId()

