### Testing task 1:

# Carry out static testing on the code below.
# Comment on any errors that you see below.

Note that we are only looking for errors here.

**Not** any issues with, i.e.: 
Thinking that methods should be renamed or should be class level, or using string interpolation etc. 

These aren't errors but rather standards that vary from developer to developer. 

Only comment on errors that would stop the tests running.

```python

class CardGame: # add attribute of self.cards = [] to CardGame


  def check_for_ace(self, card): # This function should be in Card class
    if card.value = 1: # There needs to be a double equal sign (i.e. ' == ')
      return True
    else # There needs to be a colon after this
      return False
   

  dif highest_card(self, card1 card2): # spelling error 'dif' should be 'def' and there needs to be a comma between parameters card1 and card2
  if card1.value > card2.value: # This line and lines below should be indented
    return card # 'card' needs to be more specific, i.e. 'card1.value'
  else:
    return card2 # change to card2.value
  


def cards_total(self, cards):
  total # Variable needs to be set to 0 (i.e. 'total=0')
  for card in cards:
    total += card.value
    return "You have a total of" + total # This needs to be on new line, indented same as 'for' and total needs to be changed to a string (i.e. str(total))
  
```
