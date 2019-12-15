# user-service

## Project setup
install `docker`

### Build the image
```
docker build . -t user-service
```

### Run the development container
```
docker container run -p 5000:5000 user-service
```
then, you will have a server running on 5000 port.

## Endpoints

Do a HTTP request with the given methods to the endpoints below.

### list all users

```
GET https://yourownhost:5000/v1/users/ 
```

### list a user with a given id

```
GET https://yourownhost:5000/v1/users/<id>
```

### update a user with a given id

```
PUT https://yourownhost:5000/v1/users/<id>
```

### delete a user with a given id

```
DELETE https://yourownhost:5000/v1/users/<id>
```

