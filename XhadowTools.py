#!/usr/bin/env python 
# -*- coding: utf-8 -*-

BLUE, RED, WHITE, CYAN, DEFAULT, YELLOW, MAGENTA, GREEN, END, BOLD = '\33[94m', '\033[91m', '\33[97m', '\033[36m', '\033[0m', '\33[93m', '\033[1;35m', '\033[1;32m', '\033[0m', '\033[1m'

import time
import os
import json

Green="\033[1;33m"
Blue="\033[1;34m"
Grey="\033[1;30m"
Reset="\033[0m"
Red="\033[1;31m"

with open("tools.json", "r") as file:
    ATTACK_TOOLS = json.load(file)

def banner():
    font = f"""
    {Red}__  ___               _               _____           _     
    {Red}\ \/ / |__   __ _  __| | _____      _|_   _|__   ___ | |___ 
     {Red}\  /| '_ \ / _` |/ _` |/ _ \ \ /\ / / | |/ _ \ / _ \| / __|
     {Red}/  \| | | | (_| | (_| | (_) \ V  V /  | | (_) | (_) | \__ \ 
    {Red}/_/\_\_| |_|\__,_|\__,_|\___/ \_/\_/   |_|\___/ \___/|_|___/  """

    print(font)


def menu():
    print(f"{Grey}    ||----------------------------------------------------------------------------------||")
    print(f"{Grey}    ||                                    {BLUE}MENU{Grey}                                          ||")
    print(f"{Grey}    ||----------------------------------------------------------------------------------||")
    print(f"{Grey}    ||                                        |                                         ||")
    print(f"{Grey}    ||      [1]{RED} IoT {Grey}                          |      [3]{RED} Network{Grey}                        ||")
    print(f"{Grey}    ||                                        |                                         ||")
    print(f"{Grey}    ||      [2]{RED} Social Media{Grey}                  |      [4]{RED} Web App{Grey}                        ||")
    print(f"{Grey}    ||                                        |                                         ||")
    print(f"{Grey}    ||      [5]{RED} Exit{Grey}                          |                                         ||")
    print(f"{Grey}    ||----------------------------------------------------------------------------------||")  

def options():
    opc = input("Pick a number:")
    if opc == "1":
        time.sleep(0.5)
        os.system("clear")
        iot()
    elif opc == "2":
        time.sleep(0.5)
        os.system("clear")
        socialMedia()
    elif opc == "3":
        time.sleep(0.5)
        os.system("clear")
        network()
    elif opc == "4":
        time.sleep(0.5)
        os.system("clear")
        webApp()
    elif opc == "5":
        time.sleep(0.5)
        os.system("clear")
        exit(0)

def show_tools(attack_type, phase):
    if attack_type in ATTACK_TOOLS and phase in ATTACK_TOOLS[attack_type]:
        print(f"\n{Green}Tools for {attack_type} - {phase}:{Reset}")
        for tool in ATTACK_TOOLS[attack_type][phase]:
            print(f"  - {tool['name']}: {tool['url']}")
    else:
        print(f"{Red}No tools found for {attack_type} - {phase}.{Reset}")

#IoT
def iot():
    print(f"{Grey}||----------------------------------------------------------------------------------||")
    print(f"{Grey}||                                            {Blue}IoT{Grey}                                   ||")
    print(f"{Grey}||----------------------------------------------------------------------------------||")
    print(f"{Grey}||                                        |                                         ||")
    print(f"{Grey}|| [1]{Green} Reconnaissance {Grey}                    |      [5]{Green} Reporting{Grey}                      ||")
    print(f"{Grey}||                                        |                                         ||")
    print(f"{Grey}|| [2]{Green} Scanning{Grey}                           |      [6]{Green} Back to menu{Grey}                   ||")
    print(f"{Grey}||                                        |                                         ||")
    print(f"{Grey}|| [3]{Green} Exploitation{Grey}                       |                                         ||")
    print(f"{Grey}||                                        |                                         ||")
    print(f"{Grey}|| [4]{Green} Post-Exploitation{Grey}                  |                                         ||")
    print(f"{Grey}||                                        |                                         ||")
    print(f"{Grey}||----------------------------------------------------------------------------------||")
    print("These tools will be installed in the directory tools/IoT")
    print("Choose a tool:")
    tool = input("[+] ")
    if tool == "1":
        show_tools("IoT", "Reconnaissance")
        time.sleep(1)
        iot()
    elif tool == "2":
        show_tools("IoT", "Scanning")
        time.sleep(1)
        iot()
    elif tool == "3":
        show_tools("IoT", "Exploitation")
        time.sleep(1)
        iot()
    elif tool == "4":
        show_tools("IoT", "Post-Exploitation")
        time.sleep(1)
        iot()
    elif tool == "5":
        show_tools("IoT", "Reporting")
        time.sleep(1)
        iot()
    elif tool == "6":
        time.sleep(1)
        menu()
        options()

#Social Media
def socialMedia():
    print(""+Grey+ "||----------------------------------------------------------------------------------||")	
    print(""+Grey+ "||                                  "+Blue+"Social Media"+Grey+"                                    ||")
    print(""+Grey+ "||----------------------------------------------------------------------------------||")
    print(""+Grey+ "||                                        |                                         ||")
    print(""+Grey+ "|| [1]"+Green+"Reconaissance "+Grey+"                      |      [5]"+Green+"Reporting  "+Grey+"                     ||")
    print(""+Grey+ "||                                        |                                         ||")
    print(""+Grey+ "|| [2]"+Green+"Phishing"+Grey+"                            |      [6]"+Green+"Back to menu "+Grey+"                   ||")
    print(""+Grey+ "||                                        |                                         ||")
    print(""+Grey+ "|| [3]"+Green+"Credential Stuffing"+Grey+"                 |                                         ||")
    print(""+Grey+ "||                                        |                                         ||")
    print(""+Grey+ "|| [4]"+Green+"Impersonation"+Grey+"                       |                                         ||")
    print(""+Grey+ "||                                        |                                         ||")
    print(""+Grey+ "||----------------------------------------------------------------------------------||")
    print("Estas Herramientas se instalaran en el directorio tools/IoT")    
    print("Que Herramienta elige:")    
    tool = input("[+] ")
    if tool == "1":
        show_tools("Social Media", "Reconnaissance")
        time.sleep(1)
        socialMedia()
    elif tool == "2":
        show_tools("Social Media", "Phishing")
        time.sleep(1)
        socialMedia()
    elif tool == "3":
        show_tools("Social Media", "Credential Stuffing")
        time.sleep(1)
        socialMedia()
    elif tool == "4":
        show_tools("Social Media", "Impersonation")
        time.sleep(1)
        socialMedia()
    elif tool == "5":
        show_tools("Social Media", "Reporting")
        time.sleep(1)
        socialMedia()
    elif tool == "6":
        time.sleep(1)
        menu()
        options()

#Network
def network():
    print(""+Grey+ "||----------------------------------------------------------------------------------||")	
    print(""+Grey+ "||                                  "+Blue+"Network"+Grey+"                                         ||")
    print(""+Grey+ "||----------------------------------------------------------------------------------||")
    print(f"{Grey}||                                        |                                         ||")
    print(f"{Grey}|| [1]{Green} Reconnaissance {Grey}                    |      [5]{Green} Reporting{Grey}                      ||")
    print(f"{Grey}||                                        |                                         ||")
    print(f"{Grey}|| [2]{Green} Scanning{Grey}                           |      [6]{Green} Back to menu{Grey}                   ||")
    print(f"{Grey}||                                        |                                         ||")
    print(f"{Grey}|| [3]{Green} Exploitation{Grey}                       |                                         ||")
    print(f"{Grey}||                                        |                                         ||")
    print(f"{Grey}|| [4]{Green} Post-Exploitation{Grey}                  |                                         ||")
    print(f"{Grey}||                                        |                                         ||")
    print(f"{Grey}||----------------------------------------------------------------------------------||")
    print("Estas Herramientas se instalaran en el directorio tools/IoT")    
    print("Que Herramienta elige:")    
    tool = input("[+] ")
    if tool == "1":
        show_tools("Network", "Reconnaissance")
        time.sleep(1)
        network()
    elif tool == "2":
        show_tools("Network", "Scanning")
        time.sleep(1)
        network()
    elif tool == "3":
        show_tools("Network", "Exploitation")
        time.sleep(1)
        network()
    elif tool == "4":
        show_tools("Network", "Post-Exploitation")
        time.sleep(1)
        network()
    elif tool == "5":
        show_tools("Network", "Reporting")
        time.sleep(1)
        network()
    elif tool == "6":
        time.sleep(1)
        menu()
        options()

#WebApp
def webApp():
    print(""+Grey+ "||----------------------------------------------------------------------------------||")	
    print(""+Grey+ "||                          "+Blue+"Web Application"+Grey+"                                         ||")
    print(""+Grey+ "||----------------------------------------------------------------------------------||")
    print(f"{Grey}||                                        |                                         ||")
    print(f"{Grey}|| [1]{Green} Reconnaissance {Grey}                    |      [5]{Green} Reporting{Grey}                      ||")
    print(f"{Grey}||                                        |                                         ||")
    print(f"{Grey}|| [2]{Green} Scanning{Grey}                           |      [6]{Green} Back to menu{Grey}                   ||")
    print(f"{Grey}||                                        |                                         ||")
    print(f"{Grey}|| [3]{Green} Exploitation{Grey}                       |                                         ||")
    print(f"{Grey}||                                        |                                         ||")
    print(f"{Grey}|| [4]{Green} Post-Exploitation{Grey}                  |                                         ||")
    print(f"{Grey}||                                        |                                         ||")
    print(f"{Grey}||----------------------------------------------------------------------------------||")
    print("Estas Herramientas se instalaran en el directorio tools/IoT")    
    print("Que Herramienta elige:")    
    tool = input("[+] ")
    if tool == "1":
        show_tools("Web Application", "Reconnaissance")
        time.sleep(1)
        webApp()
    elif tool == "2":
        show_tools("Web Application", "Scanning")
        time.sleep(1)
        webApp()
    elif tool == "3":
        show_tools("Web Application", "Exploitation")
        time.sleep(1)  
        webApp()
    elif tool == "4":
        show_tools("Web Application", "Post-Exploitation")
        time.sleep(1)
        webApp()
    elif tool == "5":
        show_tools("Web Application", "Reporting")
        time.sleep(1)
        webApp()
    elif tool == "6":
        time.sleep(1)
        menu()
        options()

if __name__ == "__main__":
    try:
        banner()
        time.sleep(1)
        menu()
        options()
    except KeyboardInterrupt:
        choice = eval(input('\n\n{0}[1] {1}Return XhadowTools {0}[2] {1}Exit \n{2}XhadowTools >> {1}'.format(GREEN, DEFAULT, RED)))
        if choice == 1:
            os.system('cls && python XhadowTools.py')	
        elif choice == 2:
            time.sleep(2)
            exit(0)
        else:
            print(("\n{}[x] Invalid option.".format(RED)))
            time.sleep(2)	
            exit(0)