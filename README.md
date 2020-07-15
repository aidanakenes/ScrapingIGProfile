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