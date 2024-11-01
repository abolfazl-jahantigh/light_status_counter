def count_light_changes(status_list):
    changes = 0
    for i in range(1, len(status_list)):
        if status_list[i] != status_list[i - 1]:
            changes += 1
    return changes
def main():
    while True:
        try:
            n = int(input("enter the number... "))
            if n == -1:
                print("exiting the program...")
                break
            if n <= 0:
                print("please enter a positive integer...")
                continue

            light_status = []
            for j in range(n):
                status = int(input("enter the lamp status..."))
                if status not in [0, 1]:
                    print("please enter 0 or 1...")
                    continue

                light_status.append(status)

            changes = count_light_changes(light_status)
            print("changes number :", changes)
        except ValueError:
            print("invalid input. please enter integers only")

        main()