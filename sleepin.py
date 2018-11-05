

def sleep_in(weekday, vacation):
    sleep_in = False

    if vacation==True:
        sleep_in = True
    else:
        if weekday==True:
            sleep_in = False
        else:
            sleep_in = True

    return sleep_in


s = sleep_in(True, True)
print("Sleep In: ", s)
s = sleep_in(True, False)
print("Sleep In: ", s)
s = sleep_in(False, False)
print("Sleep In: ", s)
s = sleep_in(False, True)
print("Sleep In: ", s)


# def sleep_in(weekday, vacation):
#   if vacation==True:
#     return True
#   else:
#     if weekday==True:
#       return False
#     else:
#       return True