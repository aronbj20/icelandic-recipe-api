# icelandic-recipe-api
free REST API for recipes written in Icelandic. The API uses data from gottimatinn.is and is therefore only for non commercial purposes.
</br>
The API can be accessed at [api.uppskriftir.com](https://api.uppskriftir.com)

# Authentication
Before you can access any data from the API you will have to make an POST request to [/token](#post-token). This request will return a token that needs to be in headers under `Authorization`. 

# Endpoints

## POST
[/signup](#post-signup)</br>
[/token](#post-token)</br>
___
## GET
`Requires auth` [/recipes](#get-recipes)</br>
`Requires auth` [/recipes/{id}](#get-recipesid)</br>
`Requires auth` [/groups](#get-groups)</br>
`Requires auth` [/tags](#get-tags)</br>
___

### POST /signup

**Body**
```
{
    "username": "random@randomemail.com",
    "password": "strongpassword!1234"
}
```

**Response**
```
//On sucess
{
    "Detail": "successfully created user"
}
or

//If username is taken
{
    "detail": "Username is already taken"
}
```
___

### POST /token

**Body**
```
{
    "username": "random@randomemail.com",
    "password": "strongpassword!1234"
}
```
**Response**
```
//On sucess
{
    "access_token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoicmFuZG9tQHJhbmRvbTNlbWFpbC5jb20iLCJyb2xlIjoidXNlciIsImV4cGlyZXMiOjE2NDcwOTQyMjEuNjY0OTA2fQ.PLvf70iLTpKdJgOKlvEyg95m9n2AOxcaXFNJFC28XR8",
    "token_type": "bearer"
}
or

//If incorrect username or password
{
    "detail": "Incorrect username or password"
}
```
___

### GET /recipes
**Parameters**

|          Name | Required |  Type   | Description                                                                                                                                                           |
| -------------:|:--------:|:-------:| --------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|     `pageSize` | optional | int  | The number of recipes to get in one page. Defualt is `24` and max is `64`|
|     `page` | optional | int  | The page number. Default is `1`.    |
|     `groups` | optional | string | Filters recipies by group. Default is `None` | 
|     `tags` | optional | string | Filters recipes by tags. Default is `None` |
|     `random` | optional | bool| If set to true will return random recipes. Can be used with other params. <br/>Default is `false`|

**Response**
```
// Example response
[
    {
        "_id": "622bbbe46285ee795a73bd20",
        "name": "Fylltar d????lur ?? hnetuhj??p",
        "description": "H??r eru ?? fer??inni undurlj??ffengar d????lur ?? sparif??tunum. ??a?? er tilvali?? a?? bj????a upp ?? ????r sem forr??tt, ?? sm??r??ttarhla??bor??i n?? e??a bara ??egar ykkur langar ?? eitthva?? g??ms??tt. ??a?? tekur stutta stund a?? ??tb??a ??ennan r??tt og h??gt er a?? plasta ????r og geyma ?? k??li yfir n??tt s?? ??ess ??ska??.",
        "url": "https://www.gottimatinn.is/uppskriftir/fylltar-dodlur-i-hnetuhjup",
        "image_url": "https://www.gottimatinn.is//media/1/fylltar-dodlur---gott-i-matinn-1.jpg",
        "ingredients": [
            {
                "step_name": "",
                "items": [
                    {
                        "qty": "15.0 stk.",
                        "ingredient": "ferskar d????lur"
                    },
                    {
                        "qty": "150.0 g",
                        "ingredient": "??slenskur mascarpone fr?? Gott ?? matinn"
                    },
                    {
                        "qty": "2.0 msk.",
                        "ingredient": "hunang"
                    },
                    {
                        "qty": "None None",
                        "ingredient": "saxa??ar m??ndlur og hnetur a?? eigin vali, t.d. pekan-, kasj??-, pistas??u-, e??a jar??hnetur"
                    }
                ]
            }
        ],
        "instructions": [
            {
                "title": "A??fer??",
                "steps": [
                    "Skeri?? rauf ?? d????lurnar, fjarl??gi?? steininn og opni?? ???vasa??? ?? ????r.",
                    "Blandi?? Mascarpone osti og hunangi saman ?? sk??l, setji?? ?? sprautupoka/zip lock poka og fylli?? ???vasana??? ?? d????lunum.",
                    "Leggi?? rj??maostahli??ina ofan ?? sk??l me?? s??xu??um hnetum/m??ndlum og velti?? a??eins um svo ??a?? festist vel af bl??ndu vi?? hverja d????lu.",
                    "Geymi?? ?? k??li ??ar til bera ?? fram."
                ]
            }
        ],
        "tags": [
            "Einfalt",
            "S??tt og gott",
            "Sm??r??ttir",
            "Konfekt",
            "Afm??li",
            "Fermingar",
            "P??skar",
            "Saumakl??bbar"
        ],
        "author": "H??fundur: Berglind Hrei??arsd??ttir",
        "website": "https://www.gottimatinn.is/",
        "groups": [
            "Kv??ldmatur"
        ]
    }
]
```
___

### GET /recipes/{id}

**Response**
```
//On success

    "_id": "622bbbe46285ee795a73bd20",
    "name": "Fylltar d????lur ?? hnetuhj??p",
    "description": "H??r eru ?? fer??inni undurlj??ffengar d????lur ?? sparif??tunum. ??a?? er tilvali?? a?? bj????a upp ?? ????r sem forr??tt, ?? sm??r??ttarhla??bor??i n?? e??a bara ??egar ykkur langar ?? eitthva?? g??ms??tt. ??a?? tekur stutta stund a?? ??tb??a ??ennan r??tt og h??gt er a?? plasta ????r og geyma ?? k??li yfir n??tt s?? ??ess ??ska??.",
    "url": "https://www.gottimatinn.is/uppskriftir/fylltar-dodlur-i-hnetuhjup",
    "image_url": "https://www.gottimatinn.is//media/1/fylltar-dodlur---gott-i-matinn-1.jpg",
    "ingredients": [
        {
            "step_name": "",
            "items": [
                {
                    "qty": "15.0 stk.",
                    "ingredient": "ferskar d????lur"
                },
                {
                    "qty": "150.0 g",
                    "ingredient": "??slenskur mascarpone fr?? Gott ?? matinn"
                },
                {
                    "qty": "2.0 msk.",
                    "ingredient": "hunang"
                },
                {
                    "qty": "None None",
                    "ingredient": "saxa??ar m??ndlur og hnetur a?? eigin vali, t.d. pekan-, kasj??-, pistas??u-, e??a jar??hnetur"
                }
            ]
        }
    ],
    "instructions": [
        {
            "title": "A??fer??",
            "steps": [
                "Skeri?? rauf ?? d????lurnar, fjarl??gi?? steininn og opni?? ???vasa??? ?? ????r.",
                "Blandi?? Mascarpone osti og hunangi saman ?? sk??l, setji?? ?? sprautupoka/zip lock poka og fylli?? ???vasana??? ?? d????lunum.",
                "Leggi?? rj??maostahli??ina ofan ?? sk??l me?? s??xu??um hnetum/m??ndlum og velti?? a??eins um svo ??a?? festist vel af bl??ndu vi?? hverja d????lu.",
                "Geymi?? ?? k??li ??ar til bera ?? fram."
            ]
        }
    ],
    "tags": [
        "Einfalt",
        "S??tt og gott",
        "Sm??r??ttir",
        "Konfekt",
        "Afm??li",
        "Fermingar",
        "P??skar",
        "Saumakl??bbar"
    ],
    "author": "H??fundur: Berglind Hrei??arsd??ttir",
    "website": "https://www.gottimatinn.is/",
    "groups": [
        "Kv??ldmatur"
    ]
}

or

//On error
{
    "detail": "No recipe exists with supplied ID"
}
```
___

### GET /groups

**Response**
```
[
    "Kv??ldmatur",
    "Bakstur",
    "Yfir daginn",
    "Hollusta"
]
```
___

### GET /tags

**Response**
```
[
    "Afm??li",
    "A??rir kj??tr??ttir",
    "Baka??ir ostar",
    "Bakstur",
    "Bollak??kur og m??ffins",
    "Bolludagur",
    "Boozt drykkir",
    "Brau??",
    "Brau??r??ttir",
    "Br????kaup",
    "B??ndadagur",
    "D??gur??ur (Brunch)",
    "Eftirr??ttir",
    "Einfalt",
    "Fermingar",
    "Fiskr??ttir",
    "Fl??ki??",
    "Frakkland",
    "Gott ?? kv??ldmatinn",
    "Grikkland",
    "Gr??nmetisr??ttir",
    "Hamborgarar",
    "Heilsuuppskriftir",
    "Hrekkjavaka",
    "Indland",
    "J??l",
    "Kaffidrykkir",
    "Kj??klingar??ttir",
    "Konfekt",
    "Konudagur",
    "K??kur",
    "Lambakj??t",
    "L??gkolvetna r??ttir",
    "L??ttir r??ttir",
    "Mex??k??",
    "Me??l??ti",
    "Mi??lungs",
    "Morgunmatur",
    "Nautakj??t",
    "Nesti",
    "Ostabakkar",
    "Ostak??kur",
    "Ostar og ??d??fur",
    "Ostar??ttir",
    "Part??",
    "Pasta og b??kur",
    "Pizzur",
    "P??skar",
    "Sal??t",
    "Samlokur",
    "Saumakl??bbar",
    "Skyrk??kur",
    "Sm??k??kur",
    "Sm??r??ttir",
    "Sn????ar og horn",
    "Sp??nn",
    "Sumar",
    "S??tar s??sur",
    "S??tt og gott",
    "S??sur",
    "S??pur",
    "Tilefni",
    "Um v????a ver??ld",
    "Yfir daginn",
    "??d??fur",
    "??s",
    "??tal??a"
]
```
___


