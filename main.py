import re


def main():
    count_wildfly_stops = 0
    with open("server.log.2018-04-05", 'r') as fstream:
        for line in fstream:
            line = line.rstrip('\n')
            if (re.search("WFLYSRV", line) is not None) and (re.search("OS signal", line) is not None):
                count_wildfly_stops += 1
                print(line)
    print(count_wildfly_stops)


if __name__ == "__main__":
    main()

