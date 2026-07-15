raw_logs = [
    "192.168.1.1/LOGIN/SUCCESS/10:00",
    "192.168.1.5/FILE_DOWNLOAD/FAIL/10:05",
    "192.168.1.1/FILE_UPLOAD/SUCCESS/10:12",
    "192.168.1.9/LOGIN/FAIL/10:15",
    "192.168.1.5/FILE_DOWNLOAD/SUCCESS/10:20",
    "192.168.1.1/LOGOUT/SUCCESS/10:30"
]

security_ledger = {}

for log in raw_logs:

    parts = log.split("/")
    ip = parts[0]
    action = parts[1]
    status = parts[2]
    time = parts[3]


    event_dict = {
        "action": action,
        "status": status,
        "time": time
    }

    if ip not in security_ledger:
        security_ledger[ip] = []

    security_ledger[ip].append(event_dict)

while True:
    print("\n" + "=" * 35)
    print("      UWC FIREWALL LOG PARSER      ")
    print("=" * 35)
    print("1. View Entire Security Ledger")
    print("2. Search Events by IP Address")
    print("3. Filter Failed Activities (Threat Detection)")
    print("4. Exit")
    print("=" * 35)

    option = input("Enter your option (1-4): ").strip()

    if option == "1":
        print("\n--- MASTER SECURITY LEDGER ---")
        for ip, events in security_ledger.items():
            print(f"\nIP Address: {ip}")
            for event in events:
                print(f"  -> {event['action']:<15} | Status: {event['status']:<7} | Time: {event['time']}")
            print("-" * 45)

    elif option == "2":
        search_ip = input("\nEnter IP address to query: ").strip()

        if search_ip in security_ledger:
            print(f"\nResults for IP: {search_ip}")

            for event in security_ledger[search_ip]:
                print(f"  -> {event['action']:<15} | Status: {event['status']:<7} | Time: {event['time']}")
        else:
            print("\n Error: IP Address not tracked in ledger.")

    elif option == "3":
        print("\n WARNING: Scanning for Failed Security Activities...")
        print("-" * 55)

        fail_count = 0
        for ip, events in security_ledger.items():
            for event in events:
                if event["status"] == "FAIL":
                    print(f"  Threat Alert: {ip} attempted {event['action']} at {event['time']}")
                    fail_count += 1

        if fail_count == 0:
            print(" Clean scan: No failed login or transaction events found.")
        else:
            print("-" * 55)
            print(f"Scan complete. {fail_count} failed attempts flag-logged.")

    elif option == "4":
        print("\nShutting down firewall parser. Security systems remaining active.")
        break

    else:
        print("\n Invalid choice! Please select a valid option from 1 to 4.")


