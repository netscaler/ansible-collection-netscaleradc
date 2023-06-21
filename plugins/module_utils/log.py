loglines = []


def log(msg):
    debug_level = msg.split(": ", 1)[0]
    if debug_level not in ["TRACE", "INFO", "WARNING", "ERROR", "DEBUG"]:
        msg = "DEBUG: " + msg
    loglines.append(msg)
