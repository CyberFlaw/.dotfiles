import json
import os

default_path = '~/.config/'
default_operation = 'ln -s '

key_editor = "editor"
key_env = "environment"
key_scripts = "scripts"
key_terminal = "terminal"
key_ssh = "ssh"
key_backup = "backup-codes"
key_fonts = "fonts"
key_themes = "themes"
key_pkgs = "packages"
key_languages = "languages"

with open("./config.json", "r") as config:
    data = json.load(config)

print("-----Dotfiles Config-----")

# Naming schemes:
# c_.* -> choice 
# l_.* -> list of all settings
# v_.* -> index value for chosen setting

print("[Editor]")
c_editor = input("Do you want to config the editor? (y/n): ")
if c_editor == "y" or c_editor == "Y":
    print("Choose the editor to configure")
    l_editor = []
    i = 0
    for editor in data[key_editor]:
        l_editor.append(editor)
        print(i, ".", editor)
        i += 1

    v_editor = int(input())
    while v_editor >= i:
        print("Wrong option!")
        v_editor = int(input("Enter the prefered editor: "))

    editor = l_editor[v_editor]
    print(editor)
    
    # perform linking
    if data[key_editor][l_editor[v_editor]] == "default":
        print("Linking", l_editor[v_editor], "to default path...")
        editor_linking = default_operation + "./editor/" + editor + " -t " + default_path
        if not os.system(editor_linking):
            print("Linking successful...")
        else:
            print("Linking failed! Please fix this manually...")
    else:
        print("Linking", l_editor[v_editor], "to", data[key_editor][l_editor[v_editor]] ,"...")
        editor_linking = default_operation + "./editor/nvim/" + " " + data[key_editor][l_editor[v_editor]] 
        print(editor_linking)
        # os.system(editor_linking)
else:
    print("Editor config skipped")


