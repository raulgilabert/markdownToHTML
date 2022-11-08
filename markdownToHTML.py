import sys

def convert(markdown_math: str) -> str:
    file = open(markdown_math, "r")
    lines = file.readlines()
    
    text = ""

    u_list_mode = False
    p_mode = False

    for line in lines:

        if line[0] == "#":
            text += "<h"

            counter = 1

            while (line[counter] == "#"):
                counter += 1

            text += str(counter) + ">"

            text += line[counter + 1:-1] + "</h" + str(counter) + ">\n"

        elif line == "---\n":
            text += "<hr>\n"

        elif line[0] == "-":
            if not u_list_mode:
                text += "<ul>\n"
                u_list_mode = True

            text += "<li>" + line[2: -1] + "</li>\n"
        
       
        else:
            if line[0] != "\n":
                if not p_mode:
                    text += "<p>\n"
                    p_mode = True

                text += line

            else:
                if u_list_mode:
                    text += "</ul>\n"
                    u_list_mode = False

                if p_mode:
                    text += "</p>\n"
                    p_mode = False

           

    if u_list_mode:
        text += "</ul>\n"
    
    if p_mode:
        text += "</p>\n"

    return text

if __name__ == "__main__":
    print(convert(sys.argv[1]))
