# Solution

with open("server_logs.txt", 'r') as logs, \
     open("ip_summary.txt", 'w') as summary:

    all_ip_addr = {}
    sorted_ips = {}

    for line in logs:
        line = line.strip()
        parts = line.split(' - ')

        ip_addr = parts[0].strip()
        log = parts[1].strip()

        all_ip_addr[ip_addr] = all_ip_addr.get(ip_addr, 0) + 1
        # -- Alternative for the above line
        # if ip_addr in all_ip_addr:
        #     all_ip_addr[ip_addr] += 1
        # else:
        #     all_ip_addr[ip_addr] = 1

        sorted_ips = sorted(all_ip_addr.items(), key=lambda item:(-item[1], item[0]))
        # -- Alternative 1 for the above line
        # def my_func(item):
        #     return (-item[1], item[0])
        # sorted_ips = sorted(all_ip_addr.items(), key=my_func)
        # -- Too complex relative to a lambda function, and unnecessary
        # -- considering that it'll be used only once.
        # -- Alternative 2 for the above line
        # from operator import itemgetter
        # sorted_ips = sorted(all_ip_addr.items(), key=itemgetter(1))
        # -- This is not a perfect equivalent.

    summary.write("IP Address Access Summary:\n")
    for ip_addr, count in sorted_ips:
        summary.write(f"{ip_addr}: {count}\n")
