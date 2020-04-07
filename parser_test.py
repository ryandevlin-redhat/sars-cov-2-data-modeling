from parser import Parser
import time

def main():
    # Build our parser
    # Later I could add the ability to change behavior by passing configuration info to the class
    # For our current purposes, it's simpler to hardcode them at the top of the class declaration
    parser = Parser()

    # calling parser.construct() builds and returns a dataframe of the entire dataset
    print(parser.construct())

if __name__ == "__main__":
    start = time.time()
    main()
    end = time.time()
    print("Execution time: {}".format(end - start))