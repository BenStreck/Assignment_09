#------------------------------------------#
# Title: Processing Classes
# Desc: A Module for processing Classes
# Change Log: (Who, When, What)
# DBiesinger, 2030-Jan-01, Created File
# DBiesinger, 2030-Jan-02, Extended functionality to add tracks
# BStreck, 2022-Dec-11, Completed functaionality in TODO sections
#------------------------------------------#

if __name__ == '__main__':
    raise Exception('This file is not meant to ran by itself')

import DataClasses as DC

class DataProcessor:
    """Processing the data in the application"""
    @staticmethod
    def add_CD(CDInfo, table):
        """Function to add CD info in CDinfo to the inventory table.
        
        Args:
            CDInfo (tuple): Holds information (ID, CD Title, CD Artist) to be added to inventory.
            table (list of dict): 2D data structure (list of dicts) that holds the data during runtime.
        
        Returns:
            None.
        
        """
        cdId, title, artist = CDInfo
        try:
            cdId = int(cdId)
        except:
            raise Exception('ID must be an Integer!')
        row = DC.CD(cdId, title, artist)
        table.append(row)
    
    @staticmethod
    def select_cd(table: list, cd_idx: int) -> DC.CD:
        """Selects a CD object out of table that has the ID cd_idx
        
        Args:
            table (list): Inventory list of CD objects.
            cd_idx (int): id of CD object to return
        
        Raises:
            Exception: If id is not in list.
        
        Returns:
            row (DC.CD): CD object that matches cd_idx
        
        """
        cd_idx = int(cd_idx)
        for obj in table:
            if obj.cd_id == cd_idx:
                return obj
        raise Exception
    
    @staticmethod
    def add_track(track_info: tuple, cd: DC.CD) -> None:
        """Adds a Track object with attributes in track_info to cd
        
        Args:
            track_info (tuple): Tuple containing track info (position, title, Length).
            cd (DC.CD): cd object the tarck gets added to.
        
        Raises:
            Exception: In case position is not an integer.
        
        Returns:
            None.
        
        """
        pos, title, length = track_info
        try:
            pos = int(pos)
        except ValueError:
            print('\nTrack Position must be an Integer!')
        cd.add_track(DC.Track(pos, title, length))
        
        