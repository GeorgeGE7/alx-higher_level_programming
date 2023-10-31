 #!/usr/bin/python3
def uppercase(s):
    uppercase_str = ""
    for char in s:
        if 'a' <= char <= 'z':
            char = chr(ord(char) - ord('a') + ord('A'))
        uppercase_str += char
    print("{}\n".format(uppercase_str))
