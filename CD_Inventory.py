#------------------------------------------#
# Title: CD_Inventory.py
# Desc: The CD Inventory App main Module
# Change Log: (Who, When, What)
# DBiesinger, 2030-Jan-01, Created File
# DBiesinger, 2030-Jan-02, Extended functionality to add tracks
# BStreck, 2022-Dec-11, Completed functaionality in TODO sections
#------------------------------------------#

import ProcessingClasses as PC
import IOClasses as IO

lstFileNames = ['AlbumInventory.txt', 'TrackInventory.txt']
lstOfCDObjects = IO.FileIO.load_inventory(lstFileNames)

while True:
    IO.ScreenIO.print_menu()
    strChoice = IO.ScreenIO.menu_choice()

    if strChoice == 'x':
        break
    if strChoice == 'l':
        print('WARNING: If you continue, all unsaved data will be lost and the Inventory re-loaded from file.')
        strYesNo = input('Type \'yes\' to continue and reload from file. Otherwise reload will be canceled: ')
        if strYesNo.lower() == 'yes':
            print('\nReloading...')
            lstOfCDObjects = IO.FileIO.load_inventory(lstFileNames)
            print('Done\n')
            IO.ScreenIO.show_inventory(lstOfCDObjects)
        else:
            input('Canceling... Inventory data NOT reloaded.\nPress [ENTER] to return to the menu.')
        continue  # start loop back at top.
    elif strChoice == 'a':
        tplCdInfo = IO.ScreenIO.get_CD_info(lstOfCDObjects)
        PC.DataProcessor.add_CD(tplCdInfo, lstOfCDObjects)
        print()
        IO.ScreenIO.show_inventory(lstOfCDObjects)
        continue  # start loop back at top.
    elif strChoice == 'd':
        IO.ScreenIO.show_inventory(lstOfCDObjects)
        continue  # start loop back at top.
    elif strChoice == 'c':
        IO.ScreenIO.show_inventory(lstOfCDObjects)
        try:
            cd_idx = input('Select the CD / Album index: ')
            print()
            cd = PC.DataProcessor.select_cd(lstOfCDObjects, cd_idx)
        except:
            print('This CD does not exist...')
            print('Be sure to enter an integer value that is greater than zero and within the range of existing CDs')
            continue
        
        while True:
            IO.ScreenIO.print_CD_menu()
            trackChoice = IO.ScreenIO.menu_CD_choice()
            
            if trackChoice == 'x':
                break
            elif trackChoice == 'a':
                try:
                    tplTrackInfo = IO.ScreenIO.get_track_info()
                    PC.DataProcessor.add_track(tplTrackInfo, cd)
                    IO.ScreenIO.show_tracks(cd)
                except:
                    print('No track added...')
                    continue
            elif trackChoice == 'r':
                try:
                    IO.ScreenIO.show_tracks(cd)
                    tr_choice = int(input('Which track would you like to delete? Track Number: '))
                    if tr_choice < 1:
                        raise Exception
                    cd.rmv_track(tr_choice)
                    print('\nTrack {} has been deleted'.format(tr_choice))
                except ValueError:
                    print('\nInvalid choice... The track number must be an integer\nNo tracks deleted...')
                except Exception:
                    print('\nInvalid choice... The track number must be within the range of existing tracks')
                    print('No entries deleted...')
            elif trackChoice == 'd':
                IO.ScreenIO.show_tracks(cd)
            else:
                print('General Error')
    
    elif strChoice == 's':
        IO.ScreenIO.show_inventory(lstOfCDObjects)
        strYesNo = input('Save this inventory to file? [y/n] ').strip().lower()
        if strYesNo == 'y':
            print('\nSaving inventory...')
            IO.FileIO.save_inventory(lstFileNames, lstOfCDObjects)
            print('\nDone')
        else:
            input('The inventory was NOT saved to file. Press [ENTER] to return to the menu.')
        continue  # start loop back at top.
    else:
        print('General Error')
        
        