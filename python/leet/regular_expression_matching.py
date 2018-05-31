
def regular_expression_matching(mtc_str, reg_ex):
    regcnt = 0
    mchar = reg_ex[regcnt]
    regchar = mchar if mchar in '.*' else ''
    has_matched = True
    
    for char in mtc_str:
        if regchar == '*':
            if mchar != '.' or mchar != char:
                return False

        if regchar == '.':
            regcnt += 1
            mchar = reg_ex[regcnt]
            regchar = mchar if mchar in '.*' else ''
        el
        else:
            if mchar != char:
                return False
            regcnt += 1
            mchar = reg_ex[regcnt]
            regchar = mchar if mchar in '.*' else '' 
        
        
        
        
        
        
            
        

if __name__ == '__main__':
    mtc_str = 'aa'
    reg_ex = 'a'
    print("%s matches %s = %s" % (mtc_str, reg_ex, 
                                  regular_expression_matching(mtc_str, reg_ex)))
    
    mtc_str = 'aa'
    reg_ex = 'a*'
    print("%s matches %s = %s" % (mtc_str, reg_ex, 
                                  regular_expression_matching(mtc_str, reg_ex)))
    
    mtc_str = 'ab'
    reg_ex = '.*'
    print("%s matches %s = %s" % (mtc_str, reg_ex, 
                                  regular_expression_matching(mtc_str, reg_ex)))
    
    mtc_str = 'aab'
    reg_ex = 'c*a*b'
    print("%s matches %s = %s" % (mtc_str, reg_ex, 
                                  regular_expression_matching(mtc_str, reg_ex)))
    
    mtc_str = 'mississippi'
    reg_ex = 'mis*is*p*.'
    print("%s matches %s = %s" % (mtc_str, reg_ex, 
                                  regular_expression_matching(mtc_str, reg_ex)))
