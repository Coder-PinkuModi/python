from IPython.display import clear_output
import time

# Display something
print("This is the initial content.")

# Wait for a few seconds
time.sleep(3)

# Clear the output
clear_output(wait=True)

# Display updated content
print("This is the updated content.")
