# SpotifyReleaseDateFilter
Find saved albums in your Spotify library by date range.

- Go to https://developer.spotify.com/dashboard/ to grab your client secret and id
- We found the easiest way to generate the token was to use Postman, but you can also add code in-app to obtain authorization via one of the methods detailed in the Spotify Guide.
Another  way to get the token is on the Spotify site here: https://developer.spotify.com/console/get-current-user-saved-albums/
Keep in mind that the token from Postman or Spotify will only last an hour.
(See Images folder on how to obtain token in Postman)
- Once you have the token from Postman, fill it in the empty string in the secrets.py file
- Choose your date range and run it
