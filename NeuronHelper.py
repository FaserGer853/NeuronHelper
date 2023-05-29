x = "null"
y = "null"

class NeuHelp():
    
    def neuhelp(x1,y1,x2,y2,a1w,a2w,a3w,a4w,a5w,a6w,a7w,a8w):

        try:
            
            global x
            global y
            
            a1=x1*a1w
            a2=y1*a2w

            x2 = x2 + a1 + a2 + 1

            a3=x1*a3w
            a4=y1*a4w

            y2 = y2 + a3 + a4 + 1
            


            a5=x2*a5w
            a6=y2*a6w

            x = a5 + a6 + 1

            a7=x2*a7w
            a8=y2*a8w

            y = a7 + a8 + 1

            print("Global variables has been created: x, y.")
            
        except Exception as e:
            
            print("An error has occured while running NeutronHelper.")
            print("Please send this information to me(Joooai)")
            print(f"Traceback:{e}")

    def print():
        print(f"{x}, {y}")
            
if __name__ == "__main__":
  
    print("Caution! This is must be runned by a module!")
    print("NeutronHelper cannot be runned directly!")
