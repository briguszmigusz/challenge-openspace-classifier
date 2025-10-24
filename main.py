from utils.openspace import OpenSpace

from utils.file_utils import read_names_from_csv

def main():
    input_filepath = "new_colleagues.csv"
    output_filename = "output.csv"

    names = read_names_from_csv(input_filepath)

    working_space = OpenSpace(number_of_tables=6, capacity_of_tables=4)
    working_space.organize(names)
    working_space.display()
    working_space.store(output_filename)

if __name__ == "__main__":
    main()