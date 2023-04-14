#%%
import subprocess
def checkPing(hostname): 
    #%%
    print(hostname)
    cmd = "ping -c 4 " + hostname + " | grep '4 received' "
    print(cmd)
    p1 = subprocess.run([cmd], capture_output=True,text=True,shell=True)
    if p1.stdout:
        print(p1.stdout)
        x=p1.stdout 
    else : 
        print(p1.stdout)
        x=p1.stdout + "Host not found"
    return x
checkPing('1.1.1.1')