

def WriteToFile(data, outputFile):
    """
    Writes the result to a text file with the following name
    Parameters
    ----------
    data : string
        Simple text file

    outputFile : string
        be the file where the string has been written
    Returns
    -------
    DataFrame
        ts exponential SMA result
    """
    f = open(outputFile, 'a')
    f.write(data)
    f.close()
