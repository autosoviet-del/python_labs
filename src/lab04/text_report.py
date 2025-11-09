from scr.lib.texts import normalize, tokenize

from io_txt_csv import read_text, write_csv

txt = read_text("text.txt") 
normtxt = normalize(txt)
toktxt = tokenize(normtxt)
txtkor = tuple(tuple(line.split()) for line in normtxt.splitlines())
write_csv(txtkor, "text.csv")
print (toktxt)