#------------------------------------------#
# Title: Data Classes
# Desc: A Module for Data Classes
# Change Log: (Who, When, What)
# DBiesinger, 2030-Jan-01, Created File
# DBiesinger, 2030-Jan-02, Modified to add Track class, Added methods to CD class to handle tracks
# BStreck, 2022-Dec-9, Completed functaionality in TODO sections
#------------------------------------------#

if __name__ == '__main__':
    raise Exception('This file is not meant to run by itself')

class Track():
    """Stores Data about a single Track:
    
    properties:
        position: (int) with Track position on CD / Album
        title: (str) with Track title
        length: (str) with length / playtime of Track
    methods:
        get_record() -> (str)
    
    """
    # -- Constructor -- #
    def __init__(self, tr_pos: int, tr_title: str, tr_len: str) -> None:
        """Set ID, Title and Artist of a new CD Object"""
        #    -- Attributes  -- #
        try:
            self.__tr_pos = int(tr_pos)
            self.__tr_title = str(tr_title)
            self.__tr_len = str(tr_len)
        except Exception as e:
            raise Exception('Error setting initial values:\n' + str(e))

    # -- Properties -- #
    # Track Position
    @property
    def tr_pos(self):
        return self.__tr_pos
    
    @tr_pos.setter
    def tr_pos(self, value):
        try:
            self.__tr_pos = int(value)
        except Exception:
            raise Exception('Position needs to be Integer')
    
    # Track Title
    @property
    def tr_title(self):
        return self.__tr_title
    
    @tr_title.setter
    def tr_title(self, value):
        try:
            self.__tr_title = str(value)
        except Exception:
            raise Exception('Title needs to be String!')
    
    # Track Length
    @property
    def tr_len(self):
        return self.__tr_len
    
    @tr_len.setter
    def tr_len(self, value):
        try:
            self.__tr_len = str(value)
        except Exception:
            raise Exception('Length needs to be String!')
    
    # -- Methods -- #
    def __str__(self):
        """Returns Track details as formatted string"""
        return '{:>2}.\t{} (by: {})'.format(self.tr_pos, self.tr_title, self.tr_len)
    
    def get_record(self) -> str:
        """Returns: Track record formatted for saving to file"""
        return '{},{},{}\n'.format(self.tr_pos, self.tr_title, self.tr_len)


class CD:
    """Stores data about a CD / Album:
    
    properties:
        cd_id: (int) with CD  / Album ID
        cd_title: (string) with the title of the CD / Album
        cd_artist: (string) with the artist of the CD / Album
        cd_tracks: (list) with track objects of the CD / Album
    methods:
        get_record() -> (str)
        add_track(track) -> None
        rmv_track(int) -> None
        get_tracks() -> (str)
        get_long_record() -> (str)
    
    """
    # -- Constructor -- #
    def __init__(self, cd_id: int, cd_title: str, cd_artist: str) -> None:
        """Set ID, Title and Artist of a new CD Object"""
        #    -- Attributes  -- #
        try:
            self.__cd_id = int(cd_id)
            self.__cd_title = str(cd_title)
            self.__cd_artist = str(cd_artist)
            self.__tracks = []
        except Exception as e:
            raise Exception('Error setting initial values:\n' + str(e))
    
    # -- Properties -- #
    # CD ID
    @property
    def cd_id(self):
        return self.__cd_id
    
    @cd_id.setter
    def cd_id(self, value):
        try:
            self.__cd_id = int(value)
        except Exception:
            raise Exception('ID needs to be Integer')
    
    # CD title
    @property
    def cd_title(self):
        return self.__cd_title
    
    @cd_title.setter
    def cd_title(self, value):
        try:
            self.__cd_title = str(value)
        except Exception:
            raise Exception('Title needs to be String!')
    
    # CD artist
    @property
    def cd_artist(self):
        return self.__cd_artist
    
    @cd_artist.setter
    def cd_artist(self, value):
        try:
            self.__cd_artist = str(value)
        except Exception:
            raise Exception('Artist needs to be String!')
    
    # CD tracks
    @property
    def cd_tracks(self):
        return self.__tracks
    
    # -- Methods -- #
    def __str__(self):
        """Returns: CD details as formatted string"""
        return '{:>2}.\t{} (by: {})'.format(self.cd_id, self.cd_title, self.cd_artist)
    
    def get_record(self):
        """Returns: CD record formatted for saving to file"""
        return '{},{},{}\n'.format(self.cd_id, self.cd_title, self.cd_artist)
    
    def add_track(self, track: Track) -> None:
        """Adds a track to the CD / Album
        
        Args:
            track (Track): Track object to be added to CD / Album.
        
        Returns:
            None.
        
        """
        self.__tracks.append(track)
        self.__sort_tracks()
    
    def rmv_track(self, track_id: int) -> None:
        """Removes the track identified by track_id from Album
        
        Args:
            track_id (int): ID of track to be removed.
        
        Returns:
            None.
        
        """
        self.__tracks.pop(track_id-1)
        self.__sort_tracks()
    
    def __sort_tracks(self):
        """Sorts the tracks using Track.tr_pos. Fills blanks with None"""
        n = len(self.__tracks)
        for track in self.__tracks:
            if (track is not None) and (n < track.tr_pos):
                n = track.tr_pos
        tmp_tracks = [None] * n
        for track in self.__tracks:
            if track is not None:
                tmp_tracks[track.tr_pos - 1] = track
        self.__tracks = tmp_tracks

    def get_tracks(self) -> str:
        """Returns a string list of the tracks saved for the Album
        
        Raises:
            Exception: If no tracks are saved with album.
        
        Returns:
            result (string): formatted string of tracks.
        
        """
        self.__sort_tracks()
        if len(self.__tracks) < 1:
            raise Exception('No tracks saved for this Album')
        result = ''
        for track in self.__tracks:
            if track is None:
                result += 'No Information for this track\n'
            else:
                result += str(track) + '\n'
        return result

    def get_long_record(self) -> str:
        """Gets a formatted long record of the Album: Album information plus track details
        
        Returns:
            result (string): Formatted information about album and its tracks.
        
        """
        result = 'CD:\n'
        result += self.__str__() + '\n\n'
        result += 'Tracks:\n'
        result += self.get_tracks() + '\n'
        return result
    
    