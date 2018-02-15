# Define model for all vehicles

class Vehicle:

    def __init__(self, brand, model, mileage, service):
        self.brand = brand
        self.model = model
        self.mileage = mileage
        self.service = service

    def vehicle_info(self):
        return self.brand + ' ' + self.model


# Display current list of cars in Car park
def list_of_vehicles(car_park):
    if not car_park:
        print('')
        print('You have no cars in your Car-park. Press 2 if you want to add a car\n')

    else:
        for index, vehicle in enumerate(car_park):
            print('ID: {}'.format(str(index)))
            print('Brand: {}'.format(vehicle.brand))
            print('Model: {}'.format(vehicle.model))
            print('Mileage: {}'.format(vehicle.mileage))
            print('Service date: {}'.format(vehicle.service))
            print('')


def add_new_vehicle(car_park):
    brand = input('Car Brand: ')
    model = input('Car Model: ')
    mileage = input('Mileage: ')
    service = input('Service date: ')

    new_car = Vehicle(brand=brand, model=model, mileage=mileage, service=service)
    car_park.append(new_car)
    print('')
    print('You added: ' + new_car.vehicle_info())


# Edit mileage for a selected vehicle
def edit_mileage(car_park):
    print('Select vehicle ID to update mileage')

    for index, vehicle in enumerate(car_park):
        print(str(index) + '\n ' + vehicle.vehicle_info())

    print('')
    id_num = input('ID num: ... ')
    selected_id = car_park[int(id_num)]

    new_mileage = input('Enter mileage value for {}: '.format(selected_id.vehicle_info()))
    selected_id.mileage = new_mileage

    print('')
    print('Mileage updated for {}'.format(selected_id.vehicle_info()))


# Edit service date for selected vehicle
def edit_service(car_park):
    print('Select vehicle ID to update service date')

    for index, vehicle in enumerate(car_park):
        print(str(index) + '\n' + Vehicle.vehicle_info(vehicle))

    print('')
    id_num = input('ID num: ... ')
    if id_num != car_park[int(id_num)]:
        print('That ID does not extist')

    selected_id = car_park[int(id_num)]

    new_service = input('Enter mileage value for {}: '.format(selected_id.vehicle_info()))
    selected_id.service = new_service

    print('')
    print('Service date updated for {}'.format(selected_id.vehicle_info()))


def delete_vehicle(car_park):
    print('Select item ID you want to delete')

    for index, vehicle in enumerate(car_park):
        print(str(index) + '\n' + vehicle.vehicle_info())

    print('')
    selected_id = input('Delete item with ID: ')
    selected_vehicle = car_park[int(selected_id)]

    car_park.remove(selected_vehicle)


def save_to_disk(car_park):
    with open("vehicles.txt", "w+") as veh_file:
        for index, vehicle in enumerate(car_park):
            veh_file.write('ID: {}\n'.format(str(index)))
            veh_file.write("{}\n{}\n{}\n{}\n\n".format(vehicle.brand, vehicle.model, vehicle.mileage, vehicle.service))


def main():
    car_park = []
    print('Welcome to your Car Park.')

    while True:
        print("""
Select options:
1) Show current Car Park
2) Add new vehicle
3) Edit vehicles mileage
4) Edit vehicles service date
5) Delete vehicle from Car Park
q) Save & Exit \n""")

        selection = input('Select action: ')

        if selection == '1':
            list_of_vehicles(car_park)
        elif selection == '2':
            add_new_vehicle(car_park)
        elif selection == '3':
            edit_mileage(car_park)
        elif selection == '4':
            edit_service(car_park)
        elif selection == '5':
            delete_vehicle(car_park)
        elif selection == 'q'.lower():
            print('Thank you. Your selection is logged in cars.txt file')
            save_to_disk(car_park)
            break
        else:
            print('Im sorry, that was not a valid command.')
            continue


if __name__ == '__main__':
    main()
