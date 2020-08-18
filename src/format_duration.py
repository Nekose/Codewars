def format_duration(seconds:int) -> str:
    year = 60*60*24*365
    day = 60*60*24
    hour = 60*60
    minute = 60
    if seconds == 0:
        return "now"
    if seconds >= year:
        numyear = seconds // year
        seconds %= year
    else:
        numyear = 0
    if seconds >= day:
        numday = seconds // day
        seconds %= day
    else:
        numday = 0
    if seconds >= hour:
        numhour = seconds // hour
        seconds %= hour
    else:
        numhour = 0
    if seconds >= minute:
        numminute = seconds // minute
        seconds %= minute
    else:
        numminute = 0
    time = (numyear,numday,numhour,numminute,seconds)
    format = ('years','days','hours','minutes','seconds')
    returnlist = []
    for pos,val in enumerate(time):
        if val == 0:
            continue
        if val == 1:
            returnlist.append(f'{val} {format[pos][:-1]}')
        if val > 1:
            returnlist.append(f'{val} {format[pos]}')
    returnstring = ""
    for pos,val in enumerate(returnlist):
        if len(returnlist) == 1:
            return returnstring + returnlist[0]
        if pos == len(returnlist) - 1:
            returnstring = returnstring[:-2]
            returnstring += f" and {val}"
        else:
            returnstring += f"{val}, "
    return returnstring