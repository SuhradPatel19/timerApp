import time
inputSeconds=input("Seconds: ",)
remainingSeconds=inputSeconds

#2 commit
def countdown_timer(remainingSeconds):

    while remainingSeconds>0:

         minutes=int(remainingSeconds/60)
         seconds=int(remainingSeconds%60)
         if seconds<10:
              secondsStr='0'+str(seconds)
         else:
              secondsStr=str(seconds)
         timer=f"{minutes} : {secondsStr}"
         print(timer, end="\n")
         time.sleep(1)
         remainingSeconds-=1

    print("Time is Up")
 
countdown_timer(int(remainingSeconds))





