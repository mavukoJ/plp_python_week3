count = 1
total = 0

# BUG: The while statement was missing a colon (:).
# I added the colon so the while loop can run correctly.
while count <= 5:
    total = total + count

    # BUG: The original condition was count < 5,
    # which stopped the loop before adding 5.
    # I changed it to count <= 5 so that 5 is included.
    count = count + 1

# BUG: total is an integer, so it cannot be joined directly
# to a string using +. I converted total to a string using str().
print("Sum of 1 to 5 is: " + str(total))