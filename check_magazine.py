# Harold is a kidnapper who wrote a ransom note, but now he is worried it will
# be traced back to him through his handwriting. He found a magazine and wants
# to know if he can cut out whole words from it and use them to create
# an untraceable replica of his ransom note. The words in his note are
# case-sensitive and he must use only whole words available in the magazine.
# He cannot use substrings or concatenation to create the words he needs.

# Given the words in the magazine and the words in the ransom note, print Yes
# if he can replicate his ransom note exactly using whole words from
# the magazine; otherwise, print No.


class RansomNote:
    def check_magazine(magazine, note):
        flag = 0
        mag_dict = {}
        for item in magazine:
            if item in mag_dict.keys():
                mag_dict[item] += 1
            else:
                mag_dict[item] = 1
        for word in note:
            if word not in mag_dict.keys() or mag_dict[word] == 0:
                print("No")
                flag = 1
                break
            else:
                mag_dict[word] -= 1
        if flag == 0:
            print("Yes")


if __name__ == '__main__':
    main_obj = RansomNote()
    magazine = input().rstrip().split()
    note = input().rstrip().split()
    main_obj.check_magazine(magazine, note)
