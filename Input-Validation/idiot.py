import pyinputplus as pyip

while True:
    print("Want to know how to keep an idiot busy for hours?")
    response = pyip.inputYesNo()
    if response == 'no':
        break
print("Thanks loser")