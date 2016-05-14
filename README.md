# Mozio Api

## Api for Provider

### Fetch Providers
```
curl \
 -X GET \
 http://<apiurl>/v1/provider/<id>/
 ```

### Create Provider
```
curl \
 -X POST \
 -d name="FirstName LatName" \
 -d email="username@hostname.domain" \
 -d phone_number="(800) 233-2742" \
 -d language=en \
 -d currency=USD \
 -H 'Accept: application/json' \
 http://<apiurl>/v1/provider/
```

### Update Provider
```
 curl \
 -X UPDATE \
 -d name="New Name" \
 -d email=newemail@gmail.com \
 -d phone_number="(800) 233-2742" \
 -d language=en \
 -d currency=USD \
 -H 'Accept: application/json' \
 http://<apiurl>/v1/provider/1/
```
### Delete Provider
```
curl \
 -X DELETE \
 -H 'Accept: application/json' \
 http://<apiurl>/v1/provider/1/
```

## Service Area

### Fetch ServiceArea
```
 curl \
 -X GET \
 -H 'Accept: application/json'  \
 http://<apiurl>/v1/servicearea/<id>/
```

### Create ServiceArea
```
 curl \
 -X POST \
 -d name="Delhi" \
 -d provider=1 \
 -d price=10.27 \
 -d poly='{"coordinates": [[[7.558593748947801,11.523087505286426],[7.558593748947801,11.436955214572082],[7.558593748947801,11.350796720824459],[7.558593748947801,11.350796720824459],[7.558593748947801,11.26461221095622],[7.558593748947801,11.523087505286426]]], "type": "Polygon"}'  \
 -H 'Accept: application/json'  \
 http://<apiurl>/v1/servicearea/
```
### Update ServiceArea
```
  curl \
 -X Update \
 -d name="New Delhi" \
 -d provider=2 \
 -d price=10.27 \
 -d poly='{"coordinates": [[[7.558593748947801,11.523087505286426],[7.558593748947801,11.436955214572082],[7.558593748947801,11.350796720824459],[7.558593748947801,11.350796720824459],[7.558593748947801,11.26461221095622],[7.558593748947801,11.523087505286426]]], "type": "Polygon"}'  \
 -H 'Accept: application/json'  \
 http://<apiurl>/v1/servicearea/3/
```
### Delete ServiceArea
```
 curl \
 -X DELETE \
 -H 'Accept: application/json'  \
http://<apiurl>/v1/servicearea/1/
```

## Search ServiceArea based upon lattitude/longitude pair
```
curl \
 -X GET \
 -H 'Accept: application/json' \
 http://<api-url>/v1/search-servicearea/11.5230/7.5585/
```
