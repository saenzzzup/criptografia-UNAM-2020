import fileinput

class BifidCipher:

    key_num = [
        ['E', 'N', 'C', 'R', 'Y'],
        ['P', 'T', 'A', 'B', 'D'],
        ['F', 'G', 'H', 'I', 'K'],
        ['L', 'M', 'O', 'Q', 'S'],
        ['U', 'V', 'W', 'X', 'Z'],
    ]

    def encrypt(self, m):
        m.replace(" ", "")
        numbers = self.str_to_num(m)
        return self.num_to_str(numbers)

    def decrypt(self, c):
        numbers = self.str_to_num(c)
        new_numbers = ''
        j = len(numbers) / 2
        for i in range(j):
            new_numbers += (numbers[i] + numbers[j+i])
        return self.num_to_str(c)

    def num_to_str(self, m):
        j = len(m) / 2
        new_txt = ''
        for i in range(0, j, 2):
            new_txt +=  self.key_num[int(m[i])][int(m[i+1])]
        return new_txt

    def str_to_num(self, m):
        top_num = ''
        bottom_num = ''
        for letter in m:
            for i in range(5):
                try:
                    top_num += str(i)
                    bottom_num += str(self.key_num[i].index(letter))
                except:
                    pass
        return top_num + bottom_num

lines = [line for line in fileinput.input()]

bifidCipher = BifidCipher()
solution = ''

if lines[0] == 'ENCRYPT':
    solution = bifidCipher.encrypt(lines[1])
else :
    solution = bifidCipher.decrypt(lines[1])

print(solution)