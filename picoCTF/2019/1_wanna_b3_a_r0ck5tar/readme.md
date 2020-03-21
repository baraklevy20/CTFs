# Challenge
I wrote you another song. Put the flag in the picoCTF{} flag format

# Solution
This is a continuation of the `mus1c` challenge, but this time requires input. The first conditional is as follows:
```
Listen to the music             
If the music is a guitar                  
Say "Keep on rocking!"    
```
We don't need to manually compute `a guitar`, we can simply print it, after 'listening' (reading) `the music`. So:
```
Listen to the music   
Say a guitar          
If the music is a guitar                  
Say "Keep on rocking!"    
```
We get the value `10`. We use it as first input and get the output `Keep on rocking!`. We continue, and see our next conditional:
```
Listen to the rhythm
If the rhythm without Music is nothing
```
This one is more complicated - we don't know what 'without' does, so we simply try different values for `the rhythm` and print `the rhythm without Music` and understand that `without` is subtraction. In other words, the statement is equavalent to:
```
if the rhythm - Music === 0
```
which in turn is equivalent to:
```
if the rhythm === Music
```
We print the value of Music:
```
shout Music
```
and get `170`. That's our next input. We then get the flag in decimal:
```
Keep on rocking!
66
79
78
74
79
86
73
```
which translated to `BONJOVI`.

Flag: `picoCTF{BONJOVI}`
