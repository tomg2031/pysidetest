# import the necessary modules
import zipfile, os

class Holderbot:
    def __init__(self):
        # define the location of the .zip files 
            # this is merging the end of the file name with the contents per line 18
                # added end slashjes
        self.zip_files_path = ""

        # define the location to extract files
        self.destination_path = ""

        # create a list of .zip files in the folder
        self.zip_files_list = []


    def unzip(self, from_path, to_path, *args):
        self.zip_files_path = from_path
        self.destination_path = to_path
        # create a list of .zip files in the folder
        self.zip_files_list = os.listdir(self.zip_files_path)

        # loop through the list of .zip files
        for zip_file in self.zip_files_list:
            if zip_file.endswith('.zip'):
                # create an instance of the zipfile
                zf = zipfile.ZipFile(self.zip_files_path + zip_file)
                # extract the files and skip any duplicates
                zf.extractall(self.destination_path, pwd=None, members=None) # deleted skip_duplicates=True How to make this work?
                # close the file instance
                zf.close()

                print("Files successfully extracted")