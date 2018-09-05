#############################################
##          REVERSE STRING
##
##          Tests in Python
##         Learning the Syntax
##
############################################

class main ():


    def reverseString():
        string = 'abcdefghijklmnopqrstuvwxyz'
        string2 = 'zyxwvutsrqponmlkjihgfedcba'

        print('\n ### normal to reverse ### \n')

        for i in range (len(string)):
            arrayString =[string]

            for words in arrayString:
                print (words[25 - i])

        print('\n ### reverse to normal ### \n')

        for i in range (len(string2)):
            arrayString2 = [string2]


            for words in arrayString2:
                print (words [25 - i])


    reverseString()
