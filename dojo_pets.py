from ninja import Ninja
from pets import Pet

Tucker = Pet("Tucker", "dog", "jumping")
Samson = Pet("Samson", "cat", "being self absorbed")
Martin = Pet("Martin", "monkey", "thumping chest")

ninja1 = Ninja("Jeremy", "Hatfield", "Peanuts", "dog food", Tucker)
ninja2 = Ninja("Von", "Secret", "Bananas", "tree leafs", Martin)

# ninja1.feed()
# ninja1.walk()
# ninja1.bathe()

ninja2.feed()
ninja2.walk()
ninja2.bathe()

