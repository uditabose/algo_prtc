
def compress_decompress(compressed_str):
    '''
    In this exercise, you're going to decompress a compressed string.
    Your input is a compressed string of the format number[string]
    and the decompressed output form should be the string written
    number times. For example:

    The input
    3[abc]4[ab]c

    Would be output as
    abcabcabcababababc

    Other rules
    Number can have more than one digit. For example,
    10[a] is allowed, and just means aaaaaaaaaa
    One repetition can occur inside another.
    For example, 2[3[a]b] decompresses into aaabaaab
    Characters allowed as input include digits, small
    English letters and brackets [ ].
    Digits are only to represent amount of repetitions.
    Letters are just letters.
    Brackets are only part of syntax of writing repeated substring.
    Input is always valid, so no need to check its validity.

    https://techdevguide.withgoogle.com/paths/advanced/compress-decompression/#code-challenge

    Time : O(N)
    Space: O(N)
    Note :
    '''

    rp_stack = []
    wd_stack = []
    fin_str = ""

    new_repeat = False
    for char in compressed_str:
        if char.isdigit():
            if new_repeat:
                rp_stack.append(int(char))
                new_repeat = False
            else:
                #print(char)
                if len(rp_stack) > 0:
                    num = rp_stack.pop() * 10 + int(char)
                    rp_stack.append(num)
                else:
                    rp_stack.append(int(char))
        elif char.isalpha():
            if new_repeat:
                wd_stack.append(char)
                new_repeat = False
            else:
                if len(wd_stack) > 0:
                    wd_stack.append(wd_stack.pop() + char)
                else:
                    wd_stack.append(char)
        elif char == '[':
            new_repeat = True
        else:
            #print("wd_stack %s" % wd_stack)
            #print("rp_stack %s" % rp_stack)
            repeat = rp_stack.pop() if len(rp_stack) > 0 else 1
            charset = wd_stack.pop()
            charset = charset * repeat
            #print(charset)
            if len(rp_stack) == 0:
                fin_str += charset
            else:
                wd_stack.append(charset)

    #print("fin wd_stack %s" % wd_stack)
    #print("fin rp_stack %s" % rp_stack)
    if len(wd_stack) > 0:
        fin_str += wd_stack.pop()

    return fin_str

def run():
    compressed_str = '3[abc]4[ab]c'
    print("%s ->> %s" % (compressed_str, compress_decompress(compressed_str)))

    # 3[abc]4[ab]c ->> abcabcabcababababc
    # abcabcabcababababc

    compressed_str = '10[a]'
    print("%s ->> %s" % (compressed_str, compress_decompress(compressed_str)))
    # aaaaaaaaaa
    # 10[a] ->> aaaaaaaaaa

    compressed_str = '2[3[a]b]'
    print("%s ->> %s" % (compressed_str, compress_decompress(compressed_str)))
    # aaabaaab
    # 2[3[a]b] ->> aaabaaab

    compressed_str = '1[1[1[1[1[1[1[1[1[1[1[1[1[1[1[1[1[1[1[1[xx]]]]]]]]]]]]]]]]]]]]'
    print("%s ->> %s" % (compressed_str, compress_decompress(compressed_str)))


if __name__ == '__main__':
    run()
