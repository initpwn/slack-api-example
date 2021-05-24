# slack-api-example

* Create a new app: https://api.slack.com/apps & add to a workspace. (If you don't own a workspace, create it.)

* Add scopes for bot ```chat:write```

* Install app to workspace via OAuth & Permissions (from sidebar)

* Copy bot access token from OAuth & Permissions and sigining secret from App Creds  (APP > Basic Information > App Credentials) and change it [here](https://github.com/initpwn/slack-api-example/blob/5c71513cc24853f9ae8d6732c8c35d54d9f752e6/app.py#L10) & [here](https://github.com/initpwn/slack-api-example/blob/5c71513cc24853f9ae8d6732c8c35d54d9f752e6/app.py#L14) respectively

1. If you don't have a hosting server, host app on your local server & port forward it.
	
   + Download ngrok (No need to sign-up)
	+ Windows: https://bin.equinox.io/c/4VmDzA7iaHb/ngrok-stable-windows-amd64.zip
	+ Linux:   snap install ngrok
	+ Run python program (It will be listening on 3000)
	+ On another terminal, run ngrok as:
				```ngrok http 3000```
	+ Now, your application serving on 3000 will be forwarded to Internet. (Copy URL from ngrok)

2. If you've a hosting server, then run the app directly.

	+ If you want it as a production server, use linux systemd or pm2 utility.

* On slack app, go to Event Subscriptions.

* Enable events (If you've sockets enabled, disable it. Sometimes, sockets won't work with RTM. Donno, might be deprecated)

* Enter the ngrok url to "Request URL" text box. 

* Save it once it is verified

* Add bot user event ```message.channels```

* Save the changes, will get a message asking you to reinstall app. 

* Reinstall & click allow.

* Now on slack, send a text which is specified in Bag of Sentences [BoS](https://github.com/initpwn/slack-api-example/blob/5c71513cc24853f9ae8d6732c8c35d54d9f752e6/app.py#L12) eg: "hey bot say something"

* That bot surely reply something back. 

Slack documentation: https://api.slack.com/


## TODO
```
Sentiment analysis? 
NLU?
Actions based on bot commands? 
Manage users based on their messages?
User interests? 
```
