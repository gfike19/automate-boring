# raise used to create custom error message
# traceback = callstack where it shows lines that called the error
import traceback

# traceback.format_exc = gets string version of error msg that can be written to file
# try/except blocks let you catch and manage exceptions. Exceptions can be triggered by raise , 
# assert , and a large number of errors such as trying to index an empty list. raise is typically used when you have detected an error condition. 
# assert is similar but the exception is only raised if a condition is met.