#!/usr/bin/python3

import re
                
def calc(A,B):
        ai=str(A)
        bi=str(B)
        p = re.compile('^[-+]?[0-9]+$') # Only integer
        if p.match(ai) and p.match(bi):
                a=float(ai)
                b=float(bi)
                if (a >= 1 and a <= 999) and (b >= 1 and b <= 999): 
                        valid=True
                else:
                        valid=False
        else:
                valid=False
                
        if valid:
                ans=a*b
                return ans
        else:
                return -1
        
                
def main ():
	matchstring = ''
	while matchstring != 'end':
                A = input ('input A: ')
                B = input ('input B: ')
                print ('input A * input B = ', calc(A,B))

if __name__ == '__main__':
	main()
