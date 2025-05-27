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
        # if ip_addr in all_ip_addr:
        #     all_ip_addr[ip_addr] += 1
        # else:
        #     all_ip_addr[ip_addr] = 1

        sorted_ips = sorted(all_ip_addr.items(), key=lambda item: (-item[1], item[0]))

    summary.write("IP Address Access Summary:\n")
    for ip_addr, count in sorted_ips:
        summary.write(f"{ip_addr}: {count}\n")
