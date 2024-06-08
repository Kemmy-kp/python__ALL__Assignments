#What is File function in python? What is keywords to create and write file.

1)Read Only ('r’): This mode opens the text files for reading only.
           The start of the file is where the handle is located.
           It raises the I/O error if the file does not exist.
           This is the default mode for opening files as well.
2)Read and Write ('r+’): This method opens the file for both reading and writing.
                The start of the file is where the handle is located.
                If the file does not exist, an I/O error gets raised.
3)Write Only ('w’): This mode opens the file for writing only.
            The data in existing files are modified and overwritten.
            The start of the file is where the handle is located.
            If the file does not already exist in the folder, a new one gets
            created.
4)Write and Read ('w+’): This mode opens the file for both reading and writing.
                The text is overwritten and deleted from an existing file.
                The start of the file is where the handle is located.
5)Append Only ('a’): This mode allows the file to be opened for writing.
             If the file doesn't yet exist, a new one gets created.
             The handle is set at the end of the file. The newly written data
             will be added at the end, following the previously written data.
6)Append and Read (‘a+’): Using this method, you can read and write in the file.
             If the file doesn't already exist, one gets created. The handle is
             set at the end of the file. The newly written text will be added at


Character	Mode               Description
‘r’	  Read (default)	--> Open a file for read only
‘w’	  Write	                -->Open a file for write only (overwrite)
                                   f = open('myfile.txt', 'w')
                                   f.write('Overwrite existing data.')


‘a’	  Append	        -->Open a file for write only (append)
                                    f = open('myfile.txt', 'a')
                                    f.write(' Append this text.')

‘r+’	  Read+Write	        -->open a file for both reading and writing
                                   f = open('myfile.txt', 'r+')
                                   f.write('---Overwrite content---')
‘x’	  Create	         -->Create a new file           
                                the end, following the previously written data.
