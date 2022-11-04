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
\x50\x4C\x41\x59\x20\x57\x49\x54\x48\x20\x54\x48\x45\x20\x43\x49\x50\x48\x45\x52\x54\x45\x58\x54\x20\x55\x53\x49\x4E\x47\x20\x57\x48\x41\x54\x20\x57\x41\x53\x20\x4E\x41\x4D\x45\x44\x20\x41\x46\x54\x45\x52\x20\x41\x20\x4C\x4F\x52\x44\x20\x48\x4F\x53\x49\x44\x55\x4D\x59\x4F\x50\x49\x41\x4D\x49\x43\x5A\x41\x5A\x42\x55\x44\x54\x50\x43\x49\x4C\x4E\x56\x4D\x50\x5A\x42\x45\x42\x5A\x42\x47\x54\x45\x42\x4D\x4C\x46\x43\x43\x41\x51\x49\x4D\x47\x52\x4C\x44\x59\x45\x58\x49\x50\x51\x4D\x43\x4B\x4E\x5A\x43\x54\x52\x5A\x4C\x58\x44\x46\x43\x4C\x43\x54\x55\x51\x49\x4F\x41\x45\x4F\x59\x55\x42\x4F\x46\x48\x4B\x50\x54\x51\x4E\x44\x59\x5A\x42\x51\x41\x44\x55\x47\x4F\x43\x55\x41\x5A\x42\x55\x44\x49\x44\x56\x41\x5A\x42\x55\x44\x59\x47\x4F\x44\x55\x4B\x43\x58\x54\x55\x51\x49\x4F\x41\x45\x4F\x59\x53\x49\x44\x5A\x46\x43\x49\x59\x4E\x54\x49\x4B\x49\x51\x4C\x4D\x42\x44\x43\x55\x53\x49\x43\x4B\x42\x44\x50\x4B\x51\x42\x4E\x5A\x4C\x45\x55\x42\x4F\x53\x4F\x56\x50\x41\x49\x51\x42\x4C\x43\x55\x51\x43\x4B\x42\x53\x49\x42\x55\x43\x55\x48\x47\x44\x4D\x5A\x59\x58\x44\x41\x46\x4F\x57\x58\x54\x41\x46\x47\x4C\x55\x57\x41\x59\x51\x44\x4E\x50\x54\x4E\x49\x4E\x56\x49\x41\x48\x46\x4C\x55\x57\x44\x47\x4D\x54\x58\x55\x4C\x56\x54\x4E\x57\x50\x51\x5A\x57\x43\x4B\x47\x51\x48\x4F\x49\x49\x55\x4B\x59\x4C\x46\x4E\x49\x4B\x47\x54\x44\x44\x59\x52\x4B\x51\x42\x47\x41\x4F\x54\x51\x4B\x4E\x50\x48\x59\x48\x54\x48\x47\x58\x54\x41\x46\x47\x4C\x44\x4D\x5A\x59\x58\x44\x41\x46\x4F\x57\x42\x53\x52\x48\x52\x48\x47\x51\x45\x51\x41\x46\x46\x4C\x57\x44\x57\x56\x52\x57\x45\x4B\x46\x41\x48\x59\x47\x54\x45\x4B\x49\x4D\x57\x49\x49\x56\x59\x44\x55\x57\x41\x5A\x56\x4B\x41\x51\x52\x48\x47\x41\x42\x51\x56\x48\x44\x54\x5A\x59\x56\x49\x46\x47\x58\x55\x48\x56\x4B\x56\x50\x59\x4E\x52\x48\x47\x58\x51\x48\x47\x44\x4C\x5A\x57\x56\x4B\x4C\x56\x45\x57\x55\x57\x47\x41\x4F\x59\x5A\x59\x56\x49\x46\x47\x59\x45\x59\x51\x57\x49\x59\x51\x47\x4F\x49\x47\x4E\x49\x4B\x47\x51\x58\x50\x54\x51\x4B\x5A\x59\x58\x54\x48\x47\x41\x48\x49\x58\x53\x54\x47\x51\x4F\x41\x59\x51\x54\x50\x45\x4B\x4B\x56\x4C\x46\x4E\x54\x48\x51\x48\x47\x51\x5A\x43\x56\x46\x4C\x57\x44\x57\x56\x52\x57\x45\x4B\x49\x4D\x57\x49
```

## converting the utf-8 email message to plain text

```
PLAY WITH THE CIPHERTEXT USING WHAT WAS NAMED AFTER A LORD HOSIDUMYOPIAMICZAZBUDTPCILNVMPZBEBZBGTEBMLFCCAQIMGRLDYEXIPQMCKNZCTRZLXDFCLCTUQIOAEOYUBOFHKPTQNDYZBQADUGOCUAZBUDIDVAZBUDYGODUKCXTUQIOAEOYSIDZFCIYNTIKIQLMBDCUSICKBDPKQBNZLEUBOSOVPAIQBLCUQCKBSIBUCUHGDMZYXDAFOWXTAFGLUWAYQDNPTNINVIAHFLUWDGMTXULVTNWPQZWCKGQHOIIUKYLFNIKGTDDYRKQBGAOTQKNPHYHTHGXTAFGLDMZYXDAFOWBSRHRHGQEQAFFLWDWVRWEKFAHYGTEKIMWIIVYDUWAZVKAQRHGABQVHDTZYVIFGXUHVKVPYNRHGXQHGDLZWVKLVEWUWGAOYZYVIFGYEYQWIYQGOIGNIKGQXPTQKZYXTHGAHIXSTGQOAYQTPEKKVLFNTHQHGQZCVFLWDWVRWEKIMWI
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
