file = open("quotes.txt", "r")
quotes = file.readlines()
file.close()

corrected_quotes = []
for quote in quotes:
    fields = quote.strip().split("~")
    corrected_quotes.append(fields[0] + "\n~" + fields[1] + "\n")

file = open("quotes.txt", "w")
quotes = file.writelines(corrected_quotes)
file.close()