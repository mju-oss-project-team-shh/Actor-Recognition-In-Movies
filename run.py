import sys

from time import sleep
from consolemenu import *
from consolemenu.items import *
from consolemenu.format import *
from consolemenu.screen import Screen
from tkinter import Tk
from tkinter.filedialog import askopenfilename
from getActorList import searchByTitle

menu = None
movieName = None
chosenFile = None
fileType = None

def renderPrologueByMovieName():
    global movieName
    if movieName is None:
        mn = "None"
    else:
        mn = movieName
    return "Movie name: " + mn

def renderPrologueByFilePath():
    global chosenFile
    if chosenFile is None:
        cf = "None"
    else:
        cf = chosenFile
    return "Chosen file: " + cf

def chooseFileFromFolder(folderPath):
    global fileType
    Tk().withdraw()
    title = None
    filetypes = None
    if fileType == "image":
        title = "Select an image file"
        filetypes = (
            ("PNG", "*.png"),
            ("JPEG", "*.jpg"),
            ("All files", "*.*")
        )
    elif fileType == "video":
        title = "Select a video file"
        filetypes = (
            ("MP4", "*.mp4"),
            ("AVI", "*.avi"),
            ("All files", "*.*")
        )
    else:
        return None
    filename = askopenfilename(
        initialdir = folderPath,
        title = title,
        filetypes = filetypes
    )
    return filename

def enterMovieName():
    global menu, movieName
    movieName = input("Enter movie name: ")
    menu.prologue_text = renderPrologueByMovieName()
    menu.draw()

def selectFile(folderPath, fileTypeFlag):
    global menu, fileType, chosenFile
    if(folderPath is not None and fileTypeFlag is not None):
        fileType = fileTypeFlag
        chosenFile = chooseFileFromFolder(folderPath)
        menu.prologue_text = renderPrologueByFilePath()
        menu.draw()

def printMovieName():
    global menu
    menu.prologue_text = renderPrologueByMovieName()
    menu.draw()

def printChosenFile():
    global menu
    menu.prologue_text = renderPrologueByFilePath()
    menu.draw()

def startCommand():
    global menu, fileType, chosenFile, movieName
    # TODO: Start commands
    # [1] Get actors's name
    searchByTitle(movieName)
    # [2] Crawl
    #
    print("All process completed")
    for i in range(5):
        print("Return to menu at " + str(5 - i) + " second(s)")
        sleep(1)

def main():
    global menu
    menu = ConsoleMenu(
        "< Actor Recognition In Movies v2 >", 
        "Choose the file type & select the file",
        prologue_text = renderPrologueByMovieName(),
        epilogue_text = "Made by divya2raj & modified by noah0316, jidungg, 13circle.",
        formatter = MenuFormatBuilder()
            .set_title_align("center")
            .set_subtitle_align("center")
            .set_border_style_type(MenuBorderStyleType.DOUBLE_LINE_BORDER)
            .show_prologue_top_border(True)
            .show_prologue_bottom_border(True)
    )

    input_movie_name_item = FunctionItem("Enter movie name", enterMovieName, [])
    sel_img_item = FunctionItem("Select image", selectFile, [".", "image"])
    sel_vid_item = FunctionItem("Select video", selectFile, [".", "video"])
    get_movie_name_item = FunctionItem("Show movie name", printMovieName, []);
    get_chosen_file_item = FunctionItem("Show chosen file", printChosenFile, []);
    input_item = FunctionItem("Start Conversion", startCommand, [])

    menu.append_item(input_movie_name_item)
    menu.append_item(sel_img_item)
    menu.append_item(sel_vid_item)
    menu.append_item(get_movie_name_item)
    menu.append_item(get_chosen_file_item)
    menu.append_item(input_item)

    menu.show()

if __name__ == "__main__":
    main()

