# Use command line argument to read in specified filename
import sys


def readFile():
    inputPath = "C:/Users/peter.deeming/Downloads/"
    # example filename: "CMR Surgical Jira 2021-03-09T14_58_16+0000.csv"
    try:
        arg = sys.argv[1]
    except IndexError:
        raise SystemExit(f"\nUsage: {sys.argv[0]} <filename>\n\twhere <filename> is in... C:/Users/peter.deeming/Downloads/\n")

    return inputPath + arg
        

def main():
    testFilename = readFile()
    print (testFilename)


if __name__ == "__main__":
    main()