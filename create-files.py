#!/usr/bin/env python3


import os
import better_exchook


my_dir = os.path.dirname(os.path.abspath(__file__))


def main():
    os.chdir(my_dir)

    chars = [chr(c) for c in range(ord('a'), ord('z') + 1)]
    with open("thesis.bib", "w") as f:
        for i in range(100):
            postfix = "" if i == 0 else "-%i" % i
            name_postfix = "" if i == 0 else chars[(i - 1) % len(chars)]
            f.write("""
@article{hochreiter1997lstm%s,
  title={Long short-term memory},
  author={Hochreiter%s, Sepp and Schmidhuber, J{\\"u}rgen},
  journal={Neural computation},
  volume={9},
  number={8},
  pages={1735--1780},
  year={1997},
  publisher={MIT Press}
}
""" % (postfix, name_postfix))

            f.write("""
@inproceedings{zeyer2018:asr-attention%s,
author= {Zeyer%s, Albert and Irie, Kazuki and Schlüter, Ralf and Ney, Hermann},
title= {Improved training of end-to-end attention models for speech recognition},
booktitle= {Interspeech},
year= 2018,
address= {Hyderabad, India},
month= sep,
booktitlelink= {http://interspeech2018.org/},
pdf = {https://www-i6.informatik.rwth-aachen.de/publications/downloader.php?id=1068&row=pdf}
}

""" % (postfix, name_postfix))

    num_chaps = 9

    with open("content.tex", "w") as f:        
        f.write("\n\\input{chap-intro.tex}\n")
        for i in range(1, num_chaps + 1):
            f.write("\\input{chap-%i.tex}\n" % i)
        f.write("\\input{chap-conclusion.tex}\n\n")

    for chap in range(1, num_chaps + 1):
        with open("chap-%i.tex" % chap, "w") as f:
            f.write("\n\\chapter{Chapter %i}\n\n" % chap)
            for j in range(5):
                f.write("\\section{Section %i}\n\n" % (j + 1))
                for i in range(1, 100):
                    f.write("Paragraph\n")
                    f.write("\\gls{lstm} \\cite{hochreiter1997lstm-%i}\n" % i)
                    f.write("\\cite{zeyer2018:asr-attention-%i}.\n" % i)
                    f.write("""
Lorem ipsum dolor sit amet, consectetur adipiscing elit,
sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.
Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.
Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.

""")

            num_tables = 10
            for i in range(num_tables):
                f.write("Great results in \\Cref{tab:chap%i:sth%i}.\n" % (chap, i))
            f.write("\n")

            for i in range(num_tables):
                f.write("""
\\begin{table}
\\centering
\\caption{Great table. \Gls{lstm}.
Lorem ipsum dolor sit amet, consectetur adipiscing elit,
sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.}
\\label{tab:chap%i:sth%i}
\\begin{tabular}{|c|c|c|c|c|}
\\hline
lattices & training & epoch time & \\multicolumn{2}{c|}{WER [\\%%]} \\\\
{}       & {}       & [secs]  & dev & eval \\\\ \\hline \\hline
small    & serial & 449  & \\textbf{5.32} & \\textbf{7.82} \\\\ \\cline{2-5}
{}       & parallel & \\textbf{343}  & 5.63 & 8.23 \\\\ \\hline \\hline
big      & serial   &   453        & 5.39 & 8.01 \\\\ \\cline{2-5}
{}       & parallel &   353        & 5.68 & 8.38 \\\\ \\hline
\\end{tabular}
\\end{table}

""" % (chap, i))


if __name__ == "__main__":
    better_exchook.install()
    main()