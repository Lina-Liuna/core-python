# Generators are so useful that many programs start to look like layers of generators strung together.

# Example: I have a graphical program that's using generators to animate the movement of images onscreen.
# To get the visual effect I'm looking for, I need the images to move quickly at first, pause temporarily,
# and then continue moving at a slower pace.

# I define two generators that yield the expected onscreen deltas for each part of this animation.
