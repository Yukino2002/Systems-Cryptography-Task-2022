# Systems' Recruitment Task

## Step 1

The problem statement is presented as follows, just a website url along with a story. 
```
Mr. Cheems is the owner of https://www.somewebsite.com, however he has recently had difficulty accessing the admin dashboard.

Mr. Cheems was foolish, using the same and extremely weak password for both his website and mail service provider.
Mr. Cheems claims that his email address, someemailaddress@gmail.com, has been hacked.

He received an email from his own account (someemailaddress@gmail.com) in which the Hacker stated, "You must contact me if you wish to regain access to your account."

Mr. Cheems seems unconcerned about the tainted email, but really wants to get back his website access. Can you assist Mr. Cheems in regaining access to his website?

BTW, when Mr. Cheems created the website, he hid a backup password inside the website, and wasn't foolish enough to hide it in plain sight. 

```
 > https://www.somewebsite.com


The website is just a login page with two fields - username and password. 

In the website source code, there is an easily dechipherable cipher text, encrypted using ceaser cipher. which says 

> GUR HFREANZR VF: UHRUHRUHR
> 
> GUR ONPXHC CNFFJBEQ VF: V NZ GUR ORFG QBTR


> THE USERNAME IS: HUEHUEHUE
> 
> THE BACKUP PASSWORD IS: I AM THE BEST DOGE

This is however, just meant to stall the candidate. The username and the password work, but lead to a deadend on the website. 

## Step 2
> "You must contact me if you wish to regain access to your account."

This is the line that the candidate needs to focus on. 
When the candidate sends a email to the given email address, he/she receives a reply containing the Ciphertext that needs to be deciphered.

## Message received from email

```
\x48\x4f\x53\x49\x44\x55\x4d\x59\x4f\x50\x49\x41\x4d\x49\x43\x5a\x41\x5a\x42\x55\x44\x54\x50\x43\x49\x4c\x4e\x56\x4d\x50\x5a\x42\x45\x42\x5a\x42\x47\x54\x45\x42\x4d\x4c\x46\x43\x43\x41\x51\x49\x4d\x47\x52\x4c\x44\x59\x45\x58\x49\x50\x51\x4d\x43\x4b\x4e\x5a\x43\x54\x52\x5a\x4c\x58\x44\x46\x43\x4c\x43\x54\x55\x51\x49\x4f\x41\x45\x4f\x59\x55\x42\x4f\x46\x48\x4b\x50\x54\x51\x4e\x44\x59\x5a\x42\x51\x41\x44\x55\x47\x4f\x43\x55\x41\x5a\x42\x55\x44\x49\x44\x56\x41\x5a\x42\x55\x44\x59\x47\x4f\x44\x55\x4b\x43\x58\x54\x55\x51\x49\x4f\x41\x45\x4f\x59\x53\x49\x44\x5a\x46\x43\x49\x59\x4e\x54\x49\x4b\x49\x51\x4c\x4d\x42\x44\x43\x55\x53\x49\x43\x4b\x42\x44\x50\x4b\x51\x42\x4e\x5a\x4c\x45\x55\x42\x4f\x53\x4f\x56\x50\x41\x49\x51\x42\x4c\x43\x55\x51\x43\x4b\x42\x53\x49\x42\x55\x43\x55\x48\x47\x44\x4d\x5a\x59\x58\x44\x41\x46\x4f\x57\x58\x54\x41\x46\x47\x4c\x55\x57\x41\x59\x51\x44\x4e\x50\x54\x4e\x49\x4e\x56\x49\x41\x48\x46\x4c\x55\x57\x44\x47\x4d\x54\x58\x55\x4c\x56\x54\x4e\x57\x50\x51\x5a\x57\x43\x4b\x47\x51\x48\x4f\x49\x49\x55\x4b\x59\x4c\x46\x4e\x49\x4b\x47\x54\x44\x44\x59\x52\x4b\x51\x42\x47\x41\x4f\x54\x51\x4b\x4e\x50\x48\x59\x48\x54\x48\x47\x58\x54\x41\x46\x47\x4c\x44\x4d\x5a\x59\x58\x44\x41\x46\x4f\x57\x42\x53\x52\x48\x52\x48\x47\x51\x45\x51\x41\x46\x46\x4c\x57\x44\x57\x56\x52\x57\x45\x4b\x46\x41\x48\x59\x47\x54\x45\x4b\x49\x4d\x57\x49\x49\x56\x59\x44\x55\x57\x41\x5a\x56\x4b\x41\x51\x52\x48\x47\x41\x42\x51\x56\x48\x44\x54\x5a\x59\x56\x49\x46\x47\x58\x55\x48\x56\x4b\x56\x50\x59\x4e\x52\x48\x47\x58\x51\x48\x47\x44\x4c\x5a\x57\x56\x4b\x4c\x56\x45\x57\x55\x57\x47\x41\x4f\x59\x5a\x59\x56\x49\x46\x47\x59\x45\x59\x51\x57\x49\x59\x51\x47\x4f\x49\x47\x4e\x49\x4b\x47\x51\x58\x50\x54\x51\x4b\x5a\x59\x58\x54\x48\x47\x41\x48\x49\x58\x53\x54\x47\x51\x4f\x41\x59\x51\x54\x50\x45\x4b\x4b\x56\x4c\x46\x4e\x54\x48\x51\x48\x47\x51\x5a\x43\x56\x46\x4c\x57\x44\x57\x56\x52\x57\x45\x4b\x49\x4d\x57\x49
```

## converting the utf-8 email message to plain text

```
THE NEXT CIPHER KEYSQUARE IS THE ALPHABETS WITHOUT J HOSIDUMYOPIAMICZAZBUDTPCILNVMPZBEBZBGTEBMLFCCAQIMGRLDYEXIPQMCKNZCTRZLXDFCLCTUQIOAEOYUBOFHKPTQNDYZBQADUGOCUAZBUDIDVAZBUDYGODUKCXTUQIOAEOYSIDZFCIYNTIKIQLMBDCUSICKBDPKQBNZLEUBOSOVPAIQBLCUQCKBSIBUCUHGDMZYXDAFOWXTAFGLUWAYQDNPTNINVIAHFLUWDGMTXULVTNWPQZWCKGQHOIIUKYLFNIKGTDDYRKQBGAOTQKNPHYHTHGXTAFGLDMZYXDAFOWBSRHRHGQEQAFFLWDWVRWEKFAHYGTEKIMWIIVYDUWAZVKAQRHGABQVHDTZYVIFGXUHVKVPYNRHGXQHGDLZWVKLVEWUWGAOYZYVIFGYEYQWIYQGOIGNIKGQXPTQKZYXTHGAHIXSTGQOAYQTPEKKVLFNTHQHGQZCVFLWDWVRWEKIMWI
```

## Decrypting the message using Playfair Cipher.

```
IN THE TOWN OF DOGE XEVERYONE FOLXLOWED A WEIRD ALPHABET FGBQMYTCZKORLEHPXDSUWNVAI AND STUDIED IT RELIGIOUSLY TWELVE TIMES EVERYDAY EVERYTIME THEY STUDIED IT THEY HAD TO SHIFT PLACES THE HACKER APXPARENTLY LEFT A MESSAGE THERE SGFBOYXYCVAMYYSVAFMRZDVTAMOSOHOYFCFAFRZBIORZSFQSOZMUVXBIFSFIDKTIZFAOHIFOYYTUGRAFBIOUFMOIXISGFYSVAFMBOYXYCVAMYCRSGSGFRAUVAAFYBVZMRZEAVIXIRZEGOYGFYTYRZEVZFVLSGFBARXFYOYXYFKFZSFXFZOZMSGFVSGFAOYVZFFQBZRZFBITYXYFKFZDVTYGVTIMHFOHIFSVOUUFYXYSGFCFHYRSFRLDVTUOZEFZFAOSFSGFUVAXAFYBVZMRZEGOYG
```
You will have to manually add spaces. 

```                                                    
in the town of doge everyone followed a weird alphabet fgbqmytczkorlehpxdsuwnvai and studied it religiously twelve times every day every time they studied it they had to shift places 

the hacker apparently left a message there

sgf boyycvamy ysvafm rz dvta mosohoyf cfaf rz biorzsfqs ozm uvxbifsfid ktizfaohif oy ytug r afbioufm oii sgf ysvafm boyycvamy crsg sgfra uvaafybvzmrze aviirze goygfy tyrze vzf vl sgf barxfy oy yfkfzsffz ozm sgf vsgfa oy vzffqbzrzfbityyfkfz dvt ygvtim hf ohif sv ouufyy sgf cfhyrsf rl dvt uoz efzfaosf sgf uvaafybvzmrze goyg
```


## Using fgbqmytczkorlehpxdsuwnvai as the alphabet and applying Caesar Cipher using it.

```
the passwords stored in your database were in plaintext and completely vulnerable as such i replaced all the stored passwords with their corresponding rolling hashes using one of the primes as seventeen and the other as oneexpnineplusseven you should be able to access the website if you can generate the corresponding hash
```