# csound tools

In this repository you'll find an API for generating .sco files for csound rendering. These tools are designed with offline rendering of compositions in mind. 

### procedurally generating csound score files

To create a new score:

```
score = csound.Score()
```

Each instrument gets a "staff" which takes an arguemnt for its instrument number and the number of p-fields beyond 3:

```
staff1 = score.add_staff(1, 3)
```

Events are added to staves with their start time, their duration and their other p-fields in an array.

```
staff1.add_event(0, 1, [1 for i in range(3)])
```

Write the score to a .sco file:

```
score.write_score_file('01.sco')
```

### Ideas about things to come

1. Spellchecker which makes sure events on the same staff aren't overlapping
2. Algorithmic generation of instruments

	  
Get in touch if you have ideas or want to help out! -WJ
