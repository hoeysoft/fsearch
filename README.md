sl_gen
======
Search Launcher & its Generator
####Search in "Run dialog box"([Win]-R)


Simple Use:
-----------
>RUN "setup.bat" AS ADMINISTRATOR

```
In Run dialog box
    g [words] : google
    n [words] : naver
    e [words] : naver english dictionary
    k [words] : naver korean dictionary
    we [words] : wiki in English
    wk [words] : wiki in Korean
```


Add customized Search Launcher
------------------------------
*Required: python 2.x (I've used 2.7.5)*

>Command Line Arg mode:
```
sl_gen.py query_url [outfile]
```

>Standard Input mode(Reads utill EOF):
```
sl_gen.py < list.txt
```

>>list.txt(seperated with [:space:]*)
```
query_url   [outfile]
query_url   [outfile]
...
```
=======
fsearch
=======

Fast Search in Run Dialog @ Windows
