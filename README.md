![Logo](https://abdelwahab-hamada.github.io/adopets-app/logo192.png)
## an app for adopting pets
#### 🔗 [Adopets fullstack app link](https://abdelwahab-hamada.github.io/adopets-app/)

## Technologies 
<p align="left"> <a href="https://www.djangoproject.com/" target="_blank" rel="noreferrer"> <img src="https://cdn.worldvectorlogo.com/logos/django.svg" alt="django" width="40" height="40"/> </a>  <a href="https://graphql.org" target="_blank" rel="noreferrer"> <img src="https://www.vectorlogo.zone/logos/graphql/graphql-icon.svg" alt="graphql" width="40" height="40"/> </a> <a href="https://www.python.org" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg" alt="python" width="40" height="40"/> </a>   </p>

## API Reference ([grapiql Endpoint on Heroku](https://app-adopets.herokuapp.com/pets/))

- #### **query**
   ###### pets, ownerPets:
        -id: UUID!

        -name: String!

        -age: Int!

        -photo: String!

        -owner: UserType!

        -timeAgo: String

 
- #### **mutation**
        -register(username: String!,password: String!)

        -tokenAuth(username: String!,password: String!)

        -createPet(
        age: Int!
        name: String!
        photo: Upload!
        )

        -reqPet(petId: String!)

- #### **subscription**

        -subscribeNotifications(reciever: String)


## Features

- register
- authintication
- post pet information (name,age,image)
- request to adopt pet
- notifications system

