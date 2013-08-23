sl_gen
======

Search Launcher Generator - Search in "Run dialog box"([Win]-R)

Simple Use:
  RUN "setup.bat" AS ADMINISTRATOR

  In Run dialog box
    g [words] : google
    n [words] : naver
    e [words] : naver english dictionary
    k [words] : naver korean dictionary
   we [words] : wiki in English
   wk [words] : wiki in Korean


Add customized Search Launcher
  Required: python 2.x (I've used 2.7.5)
  
  Command Line Arg mode:
    sl_gen.py query_url [outfile]

  Standard Input mode(Reads until meet EOF):
    sl_gen.py < list.txt

    == list.txt(each line is seperated with \s*)
    query_url   [outfile]
    query_url   [outfile]
    ...
