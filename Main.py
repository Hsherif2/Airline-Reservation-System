def main_menu()
  while true:
    if option == 1:
                add_flight()
            elif option == 2:
                modify_flight_schedules_menu()
            elif option == 3:
                display_records_menu()
            elif option == 4:
                print("Successfully Exit AIRLINE ADMIN SYSTEM")
                exit()
            else:
                print("Please select option 1-4!")
                print("Try again!")
                admin_menu()

            break
    
