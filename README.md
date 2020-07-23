# Simple Instagram Profile Scraper

### ```GET /profile```
Query parameters:<br>
**username**: str *<i>required</i> - Instagram user profile e.g. __brckhmptn__

### Sample request
```
GET /profile?username=brckhmptn
```

### Sample response
```
{
"data": {
    "id": "1659018352",
    "url": "https://www.instagram.com/brckhmptn",
    "bio": "",
    "username": "brckhmptn",
    "fullname": "BROCKHAMPTON",
    "followers": 1075199,
    "followings": 16,
    "is_business": false,
    "is_private": false,
    "profile_picture_url": "https://instagram.ftse2-1.fna.fbcdn.net/v/t51.2885-19/s320x320/64563496_888785964819240_1000906192341434368_n.jpg?_nc_ht=instagram.ftse2-1.fna.fbcdn.net&_nc_ohc=vdSkrVGKaUIAX_QjLdt&oh=393c117eee1654dcf1939fd1168bdd4c&oe=5F378642"
    }
}
```

### Docker-compose
__docker-compose.yml__:<br>
```
        - app
        - db: MongoDB
        - cache: Redis
```

Installation (details in https://docs.docker.com/compose/install/)
/
```
sudo curl -L "https://github.com/docker/compose/releases/download/1.26.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose
```
Build, (re)create, start, and attache to containers for a service.
```
docker-compose up -d --build
```
Display log outputs
```
docker-compose logs -f
```
Stop containers and remove containers, networks, volumes, and images created by **up**
```
docker-compose down
```
