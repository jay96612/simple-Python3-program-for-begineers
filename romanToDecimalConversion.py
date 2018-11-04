# converting roman char to equivalent decimal value
def convertDigit(a_roman_char): 
    # for I: 1
    if (a_roman_char == 'I'): 
        return 1
    # for V : 5
    if (a_roman_char == 'V'): 
        return 5
    # for X: 10    
    if (a_roman_char == 'X'): 
        return 10
    # for L: 50
    if (a_roman_char == 'L'): 
        return 50
    # for C: 100
    if (a_roman_char == 'C'): 
        return 100
    # for D: 500
    if (a_roman_char == 'D'): 
        return 500
    # for M:1000
    if (a_roman_char == 'M'): 
        return 1000
    # for invalid roman character     
    return -2                
# TO covert roman numbers to decimal value
def romanToDecimal(roman_chars): 
    # initial decimal 0
    decimal = 0
    # length finding
    length=len(roman_chars)
    index=0
    # Loop untill all characters are not accessed
    while (index < length): 
        # find decimal of character at index  'index'
        d1 = convertDigit(roman_chars[index]) 
       # checking for next character
        if (index+1 < length): 
  
            # finding decimalof next character 
            d2 = convertDigit(roman_chars[index+1])   
            # Comparing both values 
            # if current indexed value >= to next character
            if (d1 >= d2): 
                decimal = decimal + d1 
                index = index + 1
            # if current indexed value < to next character
            else: 
                decimal = decimal + d2 - d1 
                index = index + 2
        # No next character in the roman remaining        
        else: 
            decimal = decimal + d1 
            index = index + 1
    # return decimal value
    return decimal 
 
roman=str(input("Enter Roman Numbers : "))
print(roman + " : " + str(romanToDecimal(roman)))
