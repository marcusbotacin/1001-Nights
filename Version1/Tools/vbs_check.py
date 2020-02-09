# Marcus Botacin
# Tool to help detect patterns on VBS data
# This tools is part of the "1001 nights" paper

import sys  # Receive args
import re   # regex matching

# Check if the script checks for a correct number of arguments
def check_arguments(line):
    if "arguments.length"in line.lower():
        print("Argument Check")

# check if the script uses a shell
def check_shell(line):
    if "shell.application" in line.lower():
        print("Shell Application")

# check if there are escaped strings inside the script
def check_escaped_string(line):
    pattern=r'chr\(34\)(.*?)chr\(34\)'
    m = re.findall (pattern, line.lower())
    if m:
        print("Escaped String")

# check is the script escalate privs
def check_priv(line):
    if "runas" in line.lower() or "uac" in line.lower():
        print("Privilege Escalation")

# check if there are embedded urls
def check_url(line):
    if "http://" in line.lower() or "https://" in line.lower():
        print("Embedded URL")

# check for embedded IP addresses
def check_ip(line):
    ip = re.findall( r'[0-9]+(?:\.[0-9]+){3}', line.lower())
    if ip:
        print("Embedded IP")

# check for the presence of SQL queries
def check_sql(line):
    pattern=r'select(.*?)from'
    m = re.findall (pattern, line.lower())
    if m:
        print("Embedded SQL")

# check for DNS queries
def check_dns(line):
    if "dnsserver" in line.lower():
        print("DNS query")

# check for case change on function methods
def check_case(line):
    if any(x.isupper() for x in line) and any(x.islower() for x in line) and "." in line:
        print("Upper/Lower Case")

# check for HTTP requests
def check_http(line):
    if "xmlhttp" in line.lower() or "get" in line.lower() or "post" in line.lower():
        print("HTTP")

# check for comments
def check_comments(line):
    pattern=r'\'(.*?)'
    m = re.findall (pattern, line.lower())
    if m:
        print("Commented Code")

# check for submask target check
def check_target(line):
    if "255.255.255.0" in line.lower():
        print("Domestic User Target")

# check for proxy
def check_proxy(line):
    if ".setgateway" in line.lower():
        print("Proxy")

# check for the use of winmgmt
def check_mgmt(line):
    if "winmgmts:\\" in line.lower():
        print("Management")

# check for user interaction
def check_user(line):
    if "msgbox" in line.lower():
        print("User Interaction")

# check for autorun
def check_run(line):
    if ".run" in line.lower():
        print("Run Command")

# check for modular construction
def check_function(line):
    if "Function" in line:
        print("Code has Function")

# check for information gathering
def check_info(line):
    if ".ComputerName" in line:
        print("Computer Info")

# check for registry interaction
def check_reg(line):
    if "reg_sz" in line.lower() or "hkcu" in line.lower() or "hklm" in line.lower():
        print("Registry")

# check for user data access
def check_user2(line):
    if "c:\\users\\" in line.lower():
        print("User Data Access")

# check for obfuscation/deobfuscation functions
def check_obfuscation(line):
    pattern=r'>=(.*?) and (.*?)<='
    m = re.findall (pattern, line.lower())
    if m:
        print("Obfuscation")

# check for app interference
def check_app(line):
    if "Program Files" in line:
        print("Application Check")

# check for file deletion
def check_del(line):
    if ".DeleteFile" in line:
        print("Delete File")
        pattern=r'.DeleteFile(.*?).vbe'
        m = re.findall (pattern, line)
        if m:
            print("Delete Itself")

# check for infection check
def check_infection(line):
    if "folderexists" in line.lower():
        print("Existing Check")

# check for shell environment
def check_env(l):
    if "cmd" in l.lower() or "powershell" in l.lower():
        print("Shell Environment Change")

# check for time-based function (evasion?)
def check_time(line):
    if ".sleep" in line.lower():
        print("Time Delay")

# check for environment components (java)
def check_env2(line):
    if "java" in line.lower():
        print("Environment Component Check")

# look for architecture checks
def check_arch(line):
    if "PROCESSOR_ARCHITECTURE" in line:
        print("x32/x64 Check")

# look for language checks (target?)
def check_lang(line):
    if "Portuguese" in line:
        print("Language Check")

# check for xor-based obfuscation
def check_xor(line):
    if "xor" in line.lower():
        print("Xor obfuscation")

# check for SMTP
def check_mail(line):
    if "smtp" in line.lower():
        print("Mailing")

# open vbs file
f=open(sys.argv[1],"r")
# for each line
for line in f:
    # clear line control chars
    l=line.strip()
    # call all checks
    check_arguments(l)
    check_shell(l)
    check_escaped_string(l)
    check_priv(l)
    check_url(l)
    check_ip(l)
    check_sql(l)
    check_dns(l)
    check_case(l)
    check_http(l)
    check_comments(l)
    check_target(l)
    check_proxy(l)
    check_mgmt(l)
    check_user(l)
    check_run(l)
    check_function(l)
    check_info(l)
    check_reg(l)
    check_user2(l)
    check_obfuscation(l)
    check_app(l)
    check_del(l)
    check_infection(l)
    check_env(l)
    check_time(l)
    check_env2(l)
    check_arch(l)
    check_lang(l)
    check_xor(l)
    check_mail(l)
