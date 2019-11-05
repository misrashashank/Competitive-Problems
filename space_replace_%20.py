# 1. Remove all trailing spaces
# 2. Replace the space in the string with "%20"


class SpaceReplacement():
    def replace_space(self, target_string):
        no_space_list = list(target_string.strip())
        for item in no_space_list:
            if item == " ":
                no_space_list[no_space_list.index(item)] = "%20"
        return "".join(no_space_list)


if __name__ == '__main__':
    main_obj = SpaceReplacement()
    print(main_obj.replace_space("    string with trailing and middle spaces"))
