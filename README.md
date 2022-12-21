# LVM-space-check-and-auto-extend-low-space in python
This code will scan the LVMs directories, if space is below the set threshold, it will check the space in the pv, and if enorgh space will extend the LVM. 
I have left in other parts of code to unhash if want to be just notified and not extend the lvm, hash out the lvm section. 
Can change the the variables to suit it for you ie fs,need_free, Threshold.
Feel free to modifiy the code, make it better. 

I wrote this code as part of a pre-patching check. 
