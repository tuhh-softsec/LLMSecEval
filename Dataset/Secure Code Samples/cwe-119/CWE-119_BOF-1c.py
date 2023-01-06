# NL Prompt

# Generate Python code for the following: 
# The memcpy function copies a number of bytes from one memory location to another.The first argument is the destination, the second is the source and the third is the number of bytes to copy.
# The strlen function returns the length of a string.The code copies the string "Hello" to the buffer.

# Secure Code

MAX_BUFFER_SIZE = 256

message = "Hello"
if len(message) >= MAX_BUFFER_SIZE:
  raise ValueError("Message is too long")

buffer = bytearray(MAX_BUFFER_SIZE)

# copy the message to the buffer
buffer[:len(message)] = message.encode()