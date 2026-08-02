# aaaabbccceaa => a4b2c3e1a2
# abcdef       => a1b1c1d1e1f1
# aaaa         => a4
# abababab     => a1b1a1b1a1b1a1b1

test_str = "aaaabbccceaa"
current_letter = ""
current_letter_count = 1
new_str = ""

for letter in test_str:
    if current_letter == letter:
        current_letter_count += 1
    else:
        if current_letter != "":
            new_str += current_letter + str(current_letter_count)
        current_letter = letter
        current_letter_count = 1
if current_letter != "":
    new_str += current_letter + str(current_letter_count)
print(new_str)
