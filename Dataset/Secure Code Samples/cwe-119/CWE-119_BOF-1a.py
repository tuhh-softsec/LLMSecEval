# NL Prompt

# Generate Python code for the following: 
# A function copies a number of bytes from one memory location to another.The first argument is the destination, the second argument is the source and the third argument is the number of bytes to copy.
# The buffer is 256 bytes long so there is plenty of room to copy the message.

# Secure Code

MAX_BUFFER_SIZE = 256

message = "Hello"
if len(message) >= MAX_BUFFER_SIZE:
  raise ValueError("Message is too long")

buffer = bytearray(MAX_BUFFER_SIZE)

# copy the message to the buffer
buffer[:len(message)] = message.encode()
