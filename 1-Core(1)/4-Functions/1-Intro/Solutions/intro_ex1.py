# Function refactoring concept check

logfile_name = ('logfile.txt')
log_messages = ['just about to open database connection\n','just about to start data analysis\n','just about to write data to database\n']

def refactored_logging(logfile_name, log_message):
    logfile = open(logfile_name, 'a')
    logfile.write(log_message)
    logfile.close() 

log1 = refactored_logging(logfile_name,log_messages[0])
log2 = refactored_logging(logfile_name,log_messages[1])
log3 = refactored_logging(logfile_name,log_messages[2])

