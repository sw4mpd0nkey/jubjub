import time
import ipaddress



def pingsweep(ip):
    
    # for windows:   -n is ping count, -w is wait (ms)
    # for linux: -c is ping count, -w is wait (ms)
    # I didn't test subprocess in linux, but know the ping count must change if OS changes

    output = subprocess.Popen(['ping', '-n', '1', '-w', '150', str(all_hosts[ip])], stdout=subprocess.PIPE, startupinfo=info).communicate()[0]

    # lock this section, until we get a complete chunk
    # then free it (so it doesn't write all over itself)
    with print_lock:

      # normalize colors to grey
      print('\033[93m', end='')

      # code logic if we have/don't have good response
      if "Reply" in output.decode('utf-8'):
         print(str(all_hosts[ip]), '\033[32m'+"is Online")
      elif "Destination host unreachable" in output.decode('utf-8'):
         #print(str(all_hosts[ip]), '\033[90m'+"is Offline (Unreachable)")
         pass
      elif "Request timed out" in output.decode('utf-8'):
         #print(str(all_hosts[ip]), '\033[90m'+"is Offline (Timeout)")
         pass
      else:
         # print colors in green if online
         print("UNKNOWN", end='')
