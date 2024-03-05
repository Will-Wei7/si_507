class Media:
    """A class representing a media"""
    
    def __init__(self):
        """
        Constructs all the necessary attributes for the Media object.
        You need to init the instance with the following attribute with default value
        by passing the following parameter to the constructor.

        Parameters
        ----------
        title : str
            The title of the media, default value: "No Title"
        artist : str
            The artist of the media, default value: "No Artist"
        releaseDate : str
            The relase date of the media, default value: "No Release Date"
        url : str
            The URL of the media, default value: "No URL"

        Attributes
        -----------
        self.title 
        self.artist 
        etc.
        """
        

    def info(self):
        """
        Return a formatted string including the information of the media

        Format:
        <media title> by <artist> (<release date>)

        For example, “Bridget Jones's Diar (Unabridged) by Helen Fielding (2012)”
        """
        

    def length(self):
        """
        Return 0 as the length of the media

        You don't need to modify this class method
        """
        return 0

    def play(self):
        """
        Print the content of the media in the standard output.
        
        You should include the media information.

        Format:
        <media title> by <artist> (<release date>)
        """


class Track(Media):
    """ A class representing a music track."""
    
    def __init__(self):
        """
        Constructs all the necessary attributes for the Track object.
        remeber to use super().__init__(some parameters).
        Additional instance variables: 
        album (default value: "No Album"), 
        genre (default value: "No Genre"), 
        duration (default value: 0)

        Parameters
        ----------
        title : str
            The title of the track.
        artist : str
            The artist or group who performed the track.
        releaseDate : str
            The release date of the track.
        url : str
            The URL for the track.
        album : str
            The album on which the track appears.
        genre : str
            The genre of the track.
        duration : int 
            The duration of the track in seconds(rounded to nearest second).

        Attributes
        -----------
        self.title 
        self.artist 
        etc.        
        """
        

    def info(self):
        """
        Return a formatted string including the information of the music track
        It should add “[<genre>]” to the end of the output from Media.info(). 

        Format:
        <music title> by <artist> - <music album> (<release date>) [<genre>]
        For example “Hey Jude by The Beatles (1968) [Rock]”

        """
        

    def length(self):
        """
        Return the length of the music in seconds(rounded to nearest second)

        Notice the length in the provide json might not in seconds
        """
        

    def play(self):
        """
        Print the content of the music track in the standard output.
        
        You should include the music information along with the music length.

        Format:
        <music title> by <artist> - <music album> (<release date>) [<genre>] length: <length> sec
        """


class Movie(Media):
    """ A class representing a movie."""
    
    def __init__(self):
        """
        Constructs all the necessary attributes for the Movie object.
        remeber to use super().__init__(some parameters).
        Additional instance variables: 
        rating (default value: "No Rating"),
        movieLength (default value: 0) 

        Parameters
        ----------
        title : str
            The title of the movie.
        artist : str
            The artist or group who contributes to the movie.
        releaseDate : str
            The release date of the movie.
        url : str
            The URL for the movie.
        rating : str
            The rating of the movie.
        movieLength : int
            The movie length in minutes(rounded to nearest minute)

        Attributes
        -----------
        self.title 
        self.artist 
        etc.
        """
        

    def info(self):
        """
        Return a formatted string including the information of the movie
        add “[<rating>]” to the end of the output from Media.info( ). 

        Format:
        <movie title> by <artist> (<release date>) [<movie rating>]

        For example “Jaws by Steven Speilberg (1975) [PG]”
        """
        

    def length(self):
        """
        Return the length of the movie in minutes(rounded to nearest minute)

        Notice the length in the provide json might not in minutes
        """
        

    def play(self):
        """
        Print the content of the movie in the standard output.
        
        You should include the movie information along with the movie length.

        Format:
        <movie title> by <artist> (<release date>) [<movie rating>] length: <length> mins
        """