import datetime


class Contents:
    """
    Common base class for files and folders
    """

    def __init__(self, name, parent_directory):
        """
        Constructor for Class Contents
        """
        self.name = name
        self.parent_directory = parent_directory
        self.creation_time = datetime.datetime.now()
        self.last_updated_time = self.creation_time
        self.last_accessed_time = self.creation_time

    def get_size(self):
        pass

    def get_creation_time(self):
        """
        Get creation time of a file or folder
        """
        return self.creation_time

    def get_last_updated_time(self):
        """
        Get last updated time of a file or folder
        """
        return self.last_updated_time

    def get_last_accessed_time(self):
        """
        Get last accessed time of a file or folder
        """
        return self.last_accessed_time

    def set_last_updated_time(self):
        """
        Set last updated time of a file or folder
        """
        self.last_updated_time = datetime.datetime.now()

    def set_last_accessed_time(self):
        """
        Set last accessed time of a file or folder
        """
        self.last_accessed_time = datetime.datetime.now()


class File(Contents):

    def __init__(self, file_name, parent_directory, contents):
        """
        Constructor for class File
        """
        super(File, self).__init__(file_name, parent_directory)
        self.contents = contents

    def get_size(self):
        """
        Get size of the file
        """
        self.set_last_accessed_time()
        return len(self.contents)

    def read(self):
        """
        Read contents from a file
        """
        self.set_last_accessed_time()
        return self.contents

    def write(self, contents):
        """
        Write contents to a file
        """
        self.set_last_accessed_time()
        self.set_last_updated_time()
        self.contents = contents


class Directory(Contents):

    def __init__(self, directory_name, parent_directory):
        """
        Constructor for class Directory
        """
        super(Directory, self).__init__(directory_name, parent_directory)
        self.list = []

    def add_file_or_folder(self, content):
        """
        Add files and folders to a directory
        """
        self.set_last_updated_time()
        self.list.append(content)

    def list_files_and_folders(self):
        """
        List all files and folders from the directory
        """
        self.set_last_accessed_time()
        for content in self.list:
            print(content.name)

    def search_file_or_folder(self, name, type):
        """
        Search for a file or folder inside the directory (which is also a folder)
        """
        self.set_last_accessed_time()
        directories = []
        for content in self.list():
            content.set_last_accessed_time()
            if isinstance(content, File):
                if content.name == name and isinstance(content, type):
                    return content
            else:
                if isinstance(content, Directory):
                    if content.name == name and isinstance(content, type):
                        return content
                    else:
                        directories.append(content)

        if len(directories) > 0:
            for directory in directories:
                result = directory.search_file_or_folder()
                if result is not None:
                    return result
        return None

    def remove_file_or_folder(self, content):
        """
        Remove a particular file or folder from the directory(Which is also a folder)
        """
        self.set_last_updated_time()
        self.list.remove(content)

    def get_size(self):
        """
        Count the number of files and folders in a directory recursively
        """
        self.set_last_accessed_time()
        count = 0
        for content in self.list:
            if isinstance(content, Directory):
                count += 1
                count += (content.get_size())
            elif isinstance(content, File):
                count += 1
        return count


