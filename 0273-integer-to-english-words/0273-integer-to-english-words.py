class Solution:
    
    def numberToString(self, number):

        number = str(number)
        numbers = { 1:'One ', 2: 'Two ',3:'Three ',4:'Four ', 5:'Five ', 6: 'Six ', 7:'Seven ',8: 'Eight ', 9:'Nine ', 10:'Ten ', 11:'Eleven ',12: 'Twelve ',13:'Thirteen ',14:'Fourteen ',15:'Fifteen ', 16: 'Sixteen ', 17:'Seventeen ', 18:'Eighteen ', 19:'Nineteen ', 20:'Twenty ' ,30:'Thirty ',40:'Forty ', 50:'Fifty ', 60: 'Sixty ', 70:'Seventy ',80: 'Eighty ', 90:'Ninety ', 0:''}
        
        if len(number) == 3:
            return numbers[int(number[0])] + 'Hundred ' +self.numberToString(number[1:]) 
        elif len(number) == 2:
             if int(number[0])*10+int(number[1]) in numbers:
                return numbers[int(number[0])*10 + int(number[1])]
             else:
                return numbers[int(number[0])*10]+ numbers[int(number[1])]

        return numbers[int(number[0])]
            
        
    def bigNumberToString(self, num):
        postfix = { 1000: 'Thousand', 1000000:'Million', 1000000000:'Billion'}
        if int(num) < 1000:
            num = self.numberToString(int(num))
            return num[:-1]

        lastindex = len(str(num))%3 if len(str(num))%3 != 0 else 3
        num = str(num)
        return self.numberToString(int(num[0:lastindex]))+postfix[pow(10,(len(num) - lastindex))]+ ' ' + self.bigNumberToString(str(int(num[lastindex:]))) 
    
    def numberToWords(self, num):
        
        numberinwords = self.bigNumberToString(num)
        if numberinwords  == '':
            return 'Zero'
        
        numberinwords = numberinwords[:-1] if numberinwords[-1] == ' ' else numberinwords
        return numberinwords  