import datetime


def iso_year_start(iso_year):
    "The gregorian calendar date of the first day of the given ISO year"
    fourth_jan = datetime.date(iso_year, 1, 4)
    delta = datetime.timedelta(fourth_jan.isoweekday() - 1)
    return fourth_jan - delta


def replace_id(num, words):
    for k, w in words.items():
        num = num.replace(k, w)
    return num


def iso_to_gregorian(iso_year, iso_week, iso_day):
    "Gregorian calendar date for the given ISO year, week and day"
    year_start = iso_year_start(iso_year)
    return year_start + datetime.timedelta(
        days=iso_day - 1, weeks=iso_week - 1)


def parse(code):
    code = i.upper()
    res = {}
    if code.startswith("Q"):
        res["Manufacturer"] = "Quanta Computer"
        code = code[1:]
    elif code.startswith("C"):
        res["Manufacturer"] = "Compal Electronics"
        code = code[1:]
    else:
        return {"Error": "Invalid Manufacturer/Serial Number"}
    if len(code) < 6: return {"Error": "Enter more digits"}
    code = code[:6]
    for digit in code:
        if digit not in "0123456789":
            return {"Error": "Invalid digit: " + digit}
    modelnumber = code[:2]
    model = str(modelnumber)
    modelid = {
        '13': 'Pebble Classic v1.3',
        '15': 'Pebble Classic v1.5',
        '20': 'Pebble Steel',
        '30': 'Pebble Time',
        '35': 'Pebble Time Steel',
        '40': 'Pebble Time Round',
        '45': 'Pebble Time Round v4.5',
        '50': 'Pebble 2 SE',
        '55': 'Pebble 2 HR'
    }
    modelreplace = replace_id(model, modelid)
    if (modelreplace == str(modelnumber)):
        return {"Error": "Unknown Pebble Model"}
    else:
        res["Model"] = modelreplace
    "I spent too much time checking for the invalid pebbles and yet I can't do anything about the relics"
    "So far no one has describe the kickstarter so that's annoying"
    "And I'm awaiting confirmation if there is any pre-P2s made by Compal"
    date = iso_to_gregorian(2010 + int(code[5]), int(code[3:5]), int(code[2]))
    res["Date"] = date.strftime("%A %d %B %Y")
    return res


"Original script by WNP78#2849 @ Rebble Discord"
print(
    "If your serial starts with 2 or 3 instead of Q or C, please don't use this."
)
print("I can't check for information about those old-age relics.")
i = input("Serial> ")
while i != "":
    res = parse(i)
    for k in res.keys():
        print(k + ":", res[k])
    i = input("Serial> ")
