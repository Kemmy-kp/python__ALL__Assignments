'''Write a Python function to insert a string in the middle of a string.'''
#hello,hiiworld!

orgn_string="hello,world!"
string_insert="hii"

middle_index=len(orgn_string)//2
result_string=orgn_string[:middle_index]+string_insert+orgn_string[middle_index:]
print(result_string)
