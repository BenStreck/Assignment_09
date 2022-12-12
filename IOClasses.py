#------------------------------------------#
# Title: IO Classes
# Desc: A Module for IO Classes
# Change Log: (Who, When, What)
# DBiesinger, 2030-Jan-01, Created File
# DBiesinger, 2030-Jan-02, Extended functionality to add tracks
# BStreck, 2022-Dec-11, Completed functaionality in TODO sections
#------------------------------------------#

if __name__ == '__main__':
    raise Exception('This file is not meant to run by itself')

import DataClasses as DC
import ProcessingClasses as PC

class FileIO:
    """Processes data to and from file:
    
    Properties:
    
    Methods:
        save_inventory(file_name, lst_Inventory): -> None
        load_inventory(file_name): -> (a list of CD objects)
    
    """
    @staticmethod
    def save_inventory(file_name: list, lst_Inventory: list) -> None:
        """
        Saves cd and track info to the two corresponding files
        
        Args:
            file_name (list): list of file names [CD Inventory, Track Inventory] that hold the data.
            lst_Inventory (list): list of CD objects.
        
        Returns:
            None.
        
        """
        file_name_CD, file_name_track = file_name[0], file_name[1]
        try:
            with open(file_name_CD, 'w') as file:
                for disc in lst_Inventory:
                    file.write(disc.get_record())
            with open(file_name_track, 'w') as file:
                for disc in lst_Inventory:
                    tracks = disc.cd_tracks
                    cd_index = disc.cd_id
                    for track in tracks:
                        if track != None:
                            dum1 = '{},{}'.format(cd_index, track.get_record())
                            file.write(dum1)
        except Exception as e:
            print('There was a general error!', e, e.__doc__, type(e), sep='\n')
    
    @staticmethod
    def load_inventory(file_name: list) -> list:
        """
        Loads cd and track info from the two corresponding text files
        
        Args:
            file_name (list): list of file names [CD Inventory, Track Inventory] that hold the data.
        
        Returns:
            list: list of CD objects.
        
        """
        lst_Inventory = []
        file_name_CD, file_name_track = file_name[0], file_name[1]
        try:
            with open(file_name_CD, 'r') as file:
                for line in file:
                    data = line.strip().split(',')
                    row = DC.CD(data[0], data[1], data[2])
                    lst_Inventory.append(row)
            with open(file_name_track, 'r') as file:
                for line in file:
                    data = line.strip().split(',')
                    disc = int(data[0])
                    tplTrackInfo = (int(data[1]), data[2], data[3])
                    PC.DataProcessor.add_track(tplTrackInfo, lst_Inventory[disc-1])
        except FileNotFoundError:
            print('\nOne or both of the following files do not exist:')
            print('{}, {}'.format(file_name_CD, file_name_track))
            print('\nCreating the files...')
            file = open(file_name_CD, 'w')
            file.close()
            file = open(file_name_track, 'w')
            file.close()
            print('\nThe files, {} and {} have now been created!'.format(file_name_CD, file_name_track))
        except Exception as e:
            print('There was a general error!', e, e.__doc__, type(e), sep='\n')
        return lst_Inventory

class ScreenIO:
    """Handling Input / Output"""
    
    @staticmethod
    def print_menu():
        """Displays a menu of choices to the user
        
        Args:
            None.
        
        Returns:
            None.
        
        """
        print('\nMain Menu\n\n[l] Load Inventory from File\n[a] Add CD / Album\n[d] Display Current Inventory')
        print('[c] Choose CD / Album\n[s] Save Inventory to File\n[x] Exit\n')
    
    @staticmethod
    def menu_choice():
        """Gets user input for menu selection
        
        Args:
            None.
        
        Returns:
            choice (string): a lower case sting of the users input out of the choices l, a, d, c, s or x
        
        """
        choice = ' '
        while choice not in ['l', 'a', 'd', 'c', 's', 'x']:
            choice = input('Which operation would you like to perform? [l, a, d, c, s or x]: ').lower().strip()
        print()  # Add extra space for layout
        return choice
    
    @staticmethod
    def print_CD_menu():
        """Displays a sub menu of choices for CD / Album to the user
        
        Args:
            None.
        
        Returns:
            None.
        
        """
        print('\nCD Sub Menu\n\n[a] Add track\n[d] Display CD / Album Details\n[r] Remove Track\n[x] Exit to Main Menu')
    
    @staticmethod
    def menu_CD_choice():
        """Gets user input for CD sub menu selection
        
        Args:
            None.
        
        Returns:
            choice (string): a lower case sting of the users input out of the choices a, d, r or x
        
        """
        choice = ' '
        while choice not in ['a', 'd', 'r', 'x']:
            choice = input('Which operation would you like to perform? [a, d, r or x]: ').lower().strip()
        print()  # Add extra space for layout
        return choice
    
    @staticmethod
    def show_inventory(table):
        """Displays current inventory table
        
        Args:
            table (list of dict): 2D data structure (list of dicts) that holds the data during runtime.
        
        Returns:
            None.
        
        """
        print('======= The Current Inventory: =======')
        print('ID\tCD Title (by: Artist)\n')
        for row in table:
            print(row)
        print('======================================')
    
    @staticmethod
    def show_tracks(cd):
        """Displays the Tracks on a CD / Album
        
        Args:
            cd (CD): CD object.
        
        Returns:
            None.
        
        """
        try:
            cd.get_tracks()
            print('====== Current CD / Album: ======')
            print(cd)
            print('============ Tracks: ============')
            print(cd.get_tracks())
            print('=================================')
        except:
            print('====== Current CD / Album: ======')
            print(cd)
            print('============ Tracks: ============')
            print(' No tracks saved for this Album  ')
            print('=================================')
    
    @staticmethod
    def get_CD_info(table: list):
        """Function to request CD information from User to add CD to inventory
        
        Returns:
            cdId (string): Holds the ID of the CD dataset.
            cdTitle (string): Holds the title of the CD.
            cdArtist (string): Holds the artist of the CD.
        
        """
        cdId = len(table) + 1
        cdTitle = input('What is the CD\'s title? ').strip()
        cdArtist = input('What is the Artist\'s name? ').strip()
        return cdId, cdTitle, cdArtist
    
    @staticmethod
    def get_track_info():
        """Function to request Track information from User to add Track to CD / Album
        
        Returns:
            trkId (string): Holds the ID of the Track dataset.
            trkTitle (string): Holds the title of the Track.
            trkLength (string): Holds the length (time) of the Track.
        
        """
        trkId = input('Enter Position on CD / Album: ').strip()
        trkTitle = input('What is the Track\'s title? ').strip()
        trkLength = input('What is the Track\'s length? ').strip()
        return trkId, trkTitle, trkLength
    
    