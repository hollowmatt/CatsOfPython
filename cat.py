## Initializations
#Cat Locations
cat_1 = 1
cat_2 = 3
#haven't found 'em yet
found_cat_1 = false
found_cat_2 = false
# End initialization

#start game
print "welcome to cat game"

while !found_cat_1 and !found_cat_2
	print "there are a bunch of rooms, pick one"
	player_input = prompt(input)
	#set location to the input
	cat_finder_location = player_input

	if cat_finder_location == cat_1 or found_cat_1:
		found_cat_1 = true
	if cat_finder_location == cat_2 or found_cat_2:
			found_cat_2 = true
print "you found them"
print "game over"
