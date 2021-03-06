import time

DESCRIPTION = "Exit from the Proton Framework."

def autocomplete(shell, line, text, state):
    return None

def help(shell):
    shell.print_plain("")
    shell.print_plain('Use "exit -f" to force exit the Proton Framework.')
    shell.print_plain("")

def convert_to_parsable(obj):
    if isinstance(obj, dict):
        new_obj = {}
        for key in obj:
            if isinstance(key, tuple):
                new_obj['/'.join(key)] = obj[key]
            elif isinstance(key, str):
                new_obj[key] = obj[key]

    elif isinstance(obj, list):
        new_obj = []
        for val in obj:
            if isinstance(val, tuple):
                new_obj.append('/'.join(val))
            elif isinstance(val, str):
                new_obj.append(val)
    else:
        new_obj = []

    return new_obj

def execute(shell, cmd):
    splitted = cmd.split()
    if len(splitted) < 2:
        splitted.append('')
    
    if splitted[1].lower() == "-f":
        restore_map = {}
        restore_map['creds'] = convert_to_parsable(shell.creds)
        restore_map['creds_keys'] = convert_to_parsable(shell.creds_keys)
        restore_map['domain_info'] = convert_to_parsable(shell.domain_info)
        restore_map['jobs'] = []
        for jkey, j in shell.jobs.items():
            new_j = {}
            new_j['results'] = j.results
            new_j['id'] = j.id
            new_j['session_id'] = -1
            new_j['completed'] = j.completed
            new_j['ip'] = j.ip
            new_j['name'] = j.name
            new_j['key'] = j.key
            restore_map['jobs'].append(new_j)

        restore_map['sessions'] = []
        for s in [vars(session) for skey, session in shell.sessions.items()]:
            new_s = dict(s)
            try:
                new_s.pop('stager')
                new_s.pop('shell')
            except:
                pass
            new_s['status'] = 0
            restore_map['sessions'].append(new_s)

        blank_state = True

        for k in restore_map:
            if restore_map[k]:
                blank_state = False

        if not blank_state:
            restore = open('restore.json', 'w')
            import json
            restore.write(json.dumps(restore_map)+"\n")
            restore.close()

        import sys
        sys.exit(0)
        

    conf = input('Exit Proton Framework? y/N: ')
    if conf == "y" or conf == "Y":
        time.sleep(0)
    else:
        return

    restore_map = {}
    restore_map['creds'] = convert_to_parsable(shell.creds)
    restore_map['creds_keys'] = convert_to_parsable(shell.creds_keys)
    restore_map['domain_info'] = convert_to_parsable(shell.domain_info)
    restore_map['jobs'] = []
    for jkey, j in shell.jobs.items():
        new_j = {}
        new_j['results'] = j.results
        new_j['id'] = j.id
        new_j['session_id'] = -1
        new_j['completed'] = j.completed
        new_j['ip'] = j.ip
        new_j['name'] = j.name
        new_j['key'] = j.key
        restore_map['jobs'].append(new_j)

    restore_map['sessions'] = []
    for s in [vars(session) for skey, session in shell.sessions.items()]:
        new_s = dict(s)
        try:
            new_s.pop('stager')
            new_s.pop('shell')
        except:
            pass
        new_s['status'] = 0
        restore_map['sessions'].append(new_s)

    blank_state = True

    for k in restore_map:
        if restore_map[k]:
            blank_state = False

    if not blank_state:
        restore = open('restore.json', 'w')
        import json
        restore.write(json.dumps(restore_map)+"\n")
        restore.close()

    import sys
    sys.exit(0)
