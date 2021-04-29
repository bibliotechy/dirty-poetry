# Dirty Poetry


# wat now? 

Poems made from the *dirtiest& OCR data available from the Library of Congress's [Chronicling America](https://chroniclingamerica.loc.gov/about/api/) dataset of historical Newspapers. 

And by dirty, I mean OCR that looks like:

```
J t- IV .'J tv -'-'
3:i;t-'-' i.M iipnUcntioo to, , '
.1 J. .Viwifint,. N,.'.A.,17; Vahiitoatit.,Iks.ul.
J to, 5 ;S0 p. in. and l.'. 'll .. in. Trains connect at
and aouttt, ot ! a. in., !?..; and 3.1ft p. m. The
(."tli tour, iloii, lm-me-fi in ;ih istiite-.
```

## y tho?

Every data project starts with a long slog of cleaning up the data to be useful. Well, this project is conceived under the idea of
"What if we leaned into our bad data? What if we took it on it's own terms, and didn't judge it. Where might it take us?"

 And the answer is: this absolute nonsense right here.

# SHOW ME THE POEMS


They looks like this:

```
»-„aI obituary poetry not be submitted for publi



i Groceries at No. Mnu, Street "(..L
u^ Fred a Brown and ·οη Willian
kj i u si vie ta.-. ,y-,,jin
luring the last half centur; . Not le..-l


soiac of tin ir make :i: .!. - iin
Rheumatism, gout, obesity and nenrous diseases =^£l
, i pi',. I II llr'llllll. lei Hllls.hl.il
roiicr.il strike order to he o(T...-'l\o Mnn


should ('(Pine directly from th,* Island**. Tbe
b-!a.'. n.a ii,!i. n tor the e.ir. il,
G. L. Ouklns, Or W ';: Miss attie Mors,
r," "Yes, sir, we got a parrot."--E


covi ?:\.-? loi: a BOX U BEBT LIT.
upon ?getting away at eon .? i??? tibie
upon ?getting away at eon .? i??? tibie
Tsmphlet i-ont Irio I y t ? ..;lil.i!ir v :.


fra la vie 25. ma e .'<ma
1 .n is for ile ehaaa n .a ?.??.
Nik lini weal Main street, 10 rooms. ?.".00.
Gel mm explicitly am.ojniC.-. that German subma


ETHlott, cnorai freight agent of Ihe gt. I.?.
Joseph Bond, af Mjcc-,, t? made thia
fra la vie 25. ma e .'<ma
giqe.-L'iar 4e M a do £.-O. du 23.


SE'f'Tlt’ tank*, pump*. cbem:-.*l tn a'*
^ i,.;,,rj,,u-. ?? -i :i ii) tha Deutocratk borough of Man*
•» «»*d hf are —and II they hay* /
BC_of, .?uuiiii | ;_? all u tiiau- a. i_


1 ii- booka of ii.... . i p. n.
1.  UMBSEN A C 0.,-1 Montgomery st.
. 1 95 Columbus street......... New Orleans.
r.o,u!r«>d da?n: Th«- hour of >-«.ur birth a. m.
```

[More examples](poems/)


## I'm afraid to ask this but...how?

Right! I've poured over ((ok, grepped) ~500GB of Chroincling America data to find lines that meet my low standard for nonsene, basically ones that match `egrep "[^a-zA-Z0-9 ]{3,}"`. Having found the absolute bottom of the barrel, I then ran each line through some parsing and analysis to determine each lines:

* `nonsense metre`. Essentiall looking at each "term" in a line and asking "is this even a word"!
* nonsense percentage
* final phonemes to use for "rhyming" (You ever try rhyming nonsenical gibberish before. Take it from me: DONT START!)
* and some other stuff.

And then I stuffed it all in a postgres database so I could try writing poetry by writing SQL. 

```sql
SELECT idiot from PEBCAK HAVING count(problems)= 2)
```


## Yeah, but OCR on old newspapers is HARD!

Damn right it is. This project isn't meant to diminish orthe hard work put in by the Library of Congress and it's partners. It's a love letter to working with what you are given and finding ricness in it's weirdest folds. 

Literally though, I could not have done this without the great work of all the folks who have contribued to Chronicling America! 

 