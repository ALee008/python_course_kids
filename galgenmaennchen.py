import turtle

turtle.color('deep pink')
style = ('Courier', 30, 'normal')
word = "Hello World"
lines = len(word) * "_"
style_line = ("Courier", 30, "normal")
turtle.write(lines, font=style_line, align="center")
lines_as_list = list(lines)

turtle.hideturtle()
turtle.undo()
schrift = turtle.clone()
while True:
    letter = str(input("Choose a letter: "))
    if letter.upper() in word.upper():
        positions = []
        for i, l in enumerate(word.upper()):
            if l == letter.upper():
                positions.append(i)
        for i in positions:
            lines_as_list[i] = letter.upper()
        joined_word = "".join(lines_as_list)
        turtle.write(joined_word, font=style, align="center")
        if joined_word == word.upper():
            break
