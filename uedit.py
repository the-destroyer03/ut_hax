import os
import time

def clear():
	os.system('cls' if os.name == 'nt' else 'clear')

def save_edit(line, new_value):
	save = '../../%AppData%/local/UNDERTALE/file0' if os.name == 'nt' else '/.config/UNDERTALE/file0'
		
	with open(save, 'r', encoding='utf-8') as file:
		data = file.readlines()

		data[line] = new_value
	  
	with open(save, 'w', encoding='utf-8') as file:
		file.writelines(data)
		
def main():
	clear()
	print('Value to modify: \n 1] Hitpoints \n 2] Max HP \n 3] Gold \n 4] Items \n 5] Room \n 0] FUN\n')
	option = input(':')
	clear()
	
	if option == '1':
		save_edit(line = 2, new_value = input('Hitpoints: ') + '\n')
		main()
		
	elif option == '2':
		save_edit(line = 3, new_value = input('Max HP: ') + '\n')
		main()
		
	elif option == '3':
		save_edit(line = 10, new_value = '99999\n')
		main()
	
	elif option == '4':
		main()
		
	elif option == '5':
		print('All Room IDs: \n https://docs.google.com/spreadsheets/d/1bGnZjiSKjAjiHAwYxz09PJ1HVSCK3haCuPcjie0sfgk \nInaccessable Room IDs: \n https://undertale.fandom.com/wiki/Inaccessible_Rooms \nMain Rooms: \n Beginning [4] \n Home [31] \n Snowdin Entrance [44] \n Snowdin [68] \n Mettaton\'s House [121] \n Temmie Village [128] \n Lab [139] \n CORE [210] \n Kid\'s Room [224] \n True Lab [246] \n Entry 17 [264] \n')
		save_edit(line = 547, new_value = input('Room ID: ') + '\n')
		main()
	
	elif option == '0':
		print('FUN Events: \n Wrong Number Song [2-39] \n Clam Girl [80-89] \n Sans\' Call [40-45] \n Alphys\'s Call [46-50] \n Nightmare Mode [56,57] \n Goner Kid [91-100] \n Ghaster Followers [61-63] \n Soundtest Room [65] \n Mystery Man [66] \n')
		save_edit(line = 35, new_value = input('FUN Value: ') + '\n')
		main()
		
	else:
		print('Invalid option')
		time.sleep(2)
		main()
	
main()
