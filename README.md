# AirBnB Clone

<img src="https://github.com/feliciahsieh/AirBnB_clone/blob/master/AirBnBClone.jpg" style="height:15%;width:15%" />

## Welcome
AirBnB is a subset of the the popular AirBnB app, where people can rent out their lodgings similar to a hotel for a price. A place is listed on the website with information about the place (such as the number of rooms, guests, price, location), amenities, and reviews of the listing. Information about the User (renter and lister) is also collected.

Phase I is the creation of the Command-Line tool, "console", using Python's "cmd" module. This tool can Create, Retrieve, Update, and Delete (CRUD) table data in a few formats (see below). The command tool takes advantages of the Python "cmd" module. All of the table data is saved to a JSON file initially. A database will be incorporated in a future development phase. The Console should be able to be run in interactive mode and non-interactive mode.

The code uses object-oriented programming, the core object is the "BaseModel" object. The other objects derived from BaseModel include User, Place, Review, Amenity, City, and State.

Our project is written entirely in Python.

## Table of Contents
* [Requirements](#requirements)
* [Installation](#installation)
* [Usage](#usage)
* [Example Instructions](#example-instructions)
* [Credits](#credits)
* [License](#license)

## Requirements
* Ubuntu 14.04 LTS
* python3 (v3.4.3)
* PEP 8 styling (v1.7)

## Installation
In your terminal, git clone the directory with the following command:
```
https://github.com/feliciahsieh/AirBnB_clone.git
```

To run the Command-line tool, "console", type

```sh
./console
```

If you as a developer would like to fork our current project and create your own domain-specific AirBnB, please contact us. See the AUTHORS file.

## Usage
```sh
./console
```

[Insert image of Interactive mode]
[Insert image of Non-interactive mode]

## Example Instructions
The commands that you can use with our AirBnB project

| Category    | Instruction                               | Description                                                                     |
|-------------|-------------------------------------------|---------------------------------------------------------------------------------|
| BaseModel   | create BaseModel                          | Creates BaseModel instance with a unique ID, saves it to JSON, and prints ID    |
|             | show BaseModel [ID]                       | Displays the specific BaseModel instance                                        |
|             | destroy BaseModel [ID]                    | Deletes the specific BaseModel instance                                         |
|             | update BaseModel [ID] [Attribute] [Value] | Updates the specific instance with data given                                   |
| User        | create User                               | Creates User instance with a unique ID, saves it to JSON, and prints ID         |
|             | show User [ID]                            | Displays the specific User instance                                             |
|             | destroy User [ID]                         | Deletes the specific User instance                                              |
|             | update User [ID] [Attribute] [Value]      | Updates the specific instance with data given                                   |
| Place       | create Place                              | Creates Place  instance with a unique ID, saves it to JSON, and prints ID       |
|             | show Places [ID]                          | Displays the specific Places instance                                           |
|             | destroy Place [ID]                        | Deletes the specific BaseModel instance                                         |
|             | update Place [ID] [Attribute] [Value]     | Updates the specific instance with data given                                   |
| City        | create City                               | Creates City instance with a unique ID, saves it to JSON, and prints ID         |
|             | show City [ID]                            | Displays the specific City instance                                             |
|             | destroy City [ID]                         | Deletes the specific City instance                                              |
|             | update City [ID] [Attribute] [Value]      | Updates the specific instance with data given                                   |
| State       | create State                              | Creates States with a unique ID, saves it to JSON, and prints ID                |
|             | show State [ID]                           | Displays the specific State instance                                            |
|             | destroy State [ID]                        | Deletes the specific State instance                                             |
|             | update State [ID] [Attribute] [Value]     | Updates the specific instance with data given                                   |

[ID] is of the format,  "1234-1234-1234"

[Attribute] has the following set attributes, but can be appended with additional, dynamic attributes: Set attributes are:

| Category | Attribute        | Description [Attribute Value] |
|----------|------------------|-------------------------------|
| User     | email            | Email address                 |
|          | password         | User's password               |
|          | first_name       | User's first name             |
|          | last_name        | User's last name              |
| State    | name             | State name                    |
| City     | name             | City name                     |
|          | state_id         | State ID                      |
| Amenity  | name             | Amenity name                  |
| Place    | city_id          | Location's city ID            |
|          | user_id          | Owner's ID                    |
|          | name             | Location's name               |
|          | description      | Location's description        |
|          | number_rooms     | Number of rooms at place      |
|          | number_bathrooms | Number of bathrooms at place  |
|          | max_guest        | Number of guests at place     |
|          | price_by_night   | Rental price per day          |
|          | latitude         | Latitude of location          |
|          | longitude        | Longitude of location         |
|          | amenity_ids      | Amenity of location           |
| Review   | place_id         | Place id of the review        |
|          | user_id          | User id of review writer      |
|          | text             | Text of location review       |

## Credits
AirBnB is owned and maintained by Minas Anton ([@minas_anton](https://twitter.com/minas_anton)) and Felicia Hsieh ([@feliciahsiehsw](https://twitter.com/feliciahsiehsw)). You can reply to us and to [@holbertonschool](https://twitter.com/holbertonschool) on Twitter for more updates on this project and our forked projects.

## License
AirBnB is released under the MIT license. See [LICENSE](https://github.com/feliciahsieh/AirBnB_clone/blob/master/LICENSE) for details.