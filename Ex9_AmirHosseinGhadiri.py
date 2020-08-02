class time:
    def __init__(arg,t1_hour,t1_minute,t1_second):
        arg.hour = t1_hour
        arg.minute=t1_minute
        arg.second=t1_second

    def __str__(arg):
        return str(arg.hour) + ":" + str(arg.minute) + ":" + str(arg.second)

    def __repr__(arg):
        return str(arg.hour) + ":" + str(arg.minute) + ":" + str(arg.second)
    
    def show(arg):
        return str(arg.hour) + ":" + str(arg.minute) + ":" + str(arg.second)

    def __add__(arg,other):
        S=arg.second + other.second
        M=arg.minute + other.minute
        H=arg.hour + other.hour
         
        if S >= 60:
            S-=60
            M+=1
           
        if M >= 60:
            M-=60
            H+=1
            
        return str(H)+":"+str(M)+":"+str(S)    


    def __sub__(arg,other):
        S=arg.second - other.second
        M=arg.minute - other.minute
        H=arg.hour - other.hour
        return str(H)+":"+str(M)+":"+str(S)


    def __eq__(arg,other):
        return  (arg.hour)*3600 + (arg.minute)*60 + (arg.second) == (other.hour)*3600 + (other.minute)*60 + (other.second)


    def __lt__(arg,other):
        if (arg.hour)*3600 + (arg.minute)*60 + (arg.second) < (other.hour)*3600 + (other.minute)*60 + (other.second):
            return True
        else:
            return False

    def __gt__(arg,other):
        if (arg.hour)*3600 + (arg.minute)*60 + (arg.second) < (other.hour)*3600 + (other.minute)*60 + (other.second):
            return False
        else:
            return True            
        
    
#ba tavajoh be soal, karbar agah ast va khodash sa@te manteghi vared mikonad.
#dar gheire in soorat be rahati mitavanestim az taghsim sahih estefade konim.    
