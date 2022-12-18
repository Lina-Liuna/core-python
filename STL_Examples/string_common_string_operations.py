#1.  text sequence type - str
#2. String common string operations

#1.  text sequence type - str

print('student id\tstudent name\tstudent grade\t student GPA'.expandtabs())
print('student id\tstudent name\tstudent grade\t student GPA'.expandtabs(4))

# find() method should be used only if you need to know the position of a sub
print('pistachios'.find('ios'))
# to check if sub is a substring or not, use the in operator
print('ios' in 'pistachios')

left_aligned = 'Student ID'
center = 'Student Name'
right_aligned = 'Student Mark'
print("{0:<15}{1:^10}{2:>15}".format(left_aligned, center, right_aligned))
for left_aligned,center,right_aligned in zip('12345', 'abcde', '!@#$%'):
    print("{0:<15}{1:^10}{2:>17}".format(left_aligned, center, right_aligned))

# str.format_map(mapping)
# similar to str.format(**mapping), except that mapping is used directly and not copied to a dict.
# this is useful if mapping is a dict subclass

class Coordinate(dict):
    def __missing__(self, key):
        return key

for i, j in zip(range(10), reversed(range(10))):
    print('({x}, {y})'.format_map(Coordinate(x=i, y=j)))

