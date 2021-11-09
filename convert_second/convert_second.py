
def convert_second(seconds):
    houres = seconds // 3600 
    miniuts = (seconds - houres * 3600) // 60
    re_seconds = seconds - houres * 3600 - miniuts * 60 
    
    return houres, miniuts, re_seconds

houres, miniuts, seconds = convert_second(5000)
print(houres, miniuts, seconds)