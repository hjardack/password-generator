import random


#Basic Password Generator

def main():
    
    password = ''
    
    sample_space_standard = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
    
    sample_space_special_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*'
    
    number_of_chars = input("Enter desired number of characters. ")
    
    
    default_number_of_chars = 14
    
    if number_of_chars == '':
        number_of_chars = default_number_of_chars
    
    include_special_chars = input("Include special characters? Y/n ")
    
    try:
    
        if include_special_chars in ('Y', 'y', 'yes', 'Yes', 'YES', ''):
            while len(password) < int(number_of_chars):
                password += random.choice(sample_space_special_chars)
    
    
        elif include_special_chars in ('N', 'n', 'no', 'No', 'NO'):
            while len(password) < int(number_of_chars):
                password += random.choice(sample_space_standard)
        else:
            while len(password) < int(number_of_chars):
                password += random.choice(sample_space_special_chars)
    
    except ValueError: print("Please make sure you are entering an integer value for desired number of characters.")
        
            
    print(password)
    
if __name__ == "__main__":
    main()
    
    
    
    
    
    
    



