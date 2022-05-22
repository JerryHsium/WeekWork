def conversion(cel):
    return 32 + cel * 1.8

 if __name__ == 'main':
      cel = float(input("Please enter a temperature in degrees celsius: "))
      print("Fahrenheit temperature: ", conversion(cel))