# chitchat-slack-chatting-bot-app
a ChatGPT based slack chatting bot who response to direct messages, locally deploy with slack socket mode.
![1677880240605](https://user-images.githubusercontent.com/36948683/222836101-5b851353-f513-4a49-91bb-ff2a144d29e8.jpg)


# how
#### get OPENAI_API_KEY
1.  Go to the OpenAI API website https://platform.openai.com/docs/guides/completion
2.  Log in or sign up for an OpenAI account
3.  Go to the API Key section and create a new API key
4.  Copy the API key, Paste OPENAI_API_KEY into the Dockerfile

#### get SLACK_BOT_TOKEN and SLACK_APP_TOKEN
1.  Go to the Slack API website https://api.slack.com/
2.  Click on “Create an app” and select “From scratch”
3.  Give your app a name, select your Slack workspace
4.  In Basic information > Add features and functionality. Click on “Permissions” and in Scopes add in Bot Token Scopes: all permissions needed are listed in chitchat/slack-app-configs/OATH&permissions.txt
5. Features > Event Subscriptions >. Click on “Subscribe to bot events” and in Scopes add events subscriptions: all permissions needed are listed in chitchat/slack-app-configs/event-subscriptions.txt ![image](https://user-images.githubusercontent.com/36948683/222836364-2be12b9a-cd4e-4031-af9b-1e4c14401062.png)
6.  In settings, click on “Socket Mode”, enable it and give the token a name. Copy the Slack Bot App Token (starts with xapp), paste into the Dockerfile
7.  In Basic information > Add features and functionality. Click on “Event Subscriptions” and enable it. Furthermore in “Subscribe to bot events” select “app_mention”. Save changes.
8.  Go to the “OAuth & Permissions” section and install your app to your workspace
9.  Copy the Slack Bot Token (starts with xoxb), paste into the Dockerfile

#### after turn on docker daemon 
```
docker build -t chitchat-image .
docker run chitchat-image
```
![image](https://user-images.githubusercontent.com/36948683/222836506-72c37454-94eb-41e9-9967-65d424444b87.png)


#### add this app to your workplace
use ctrl + R to refresh the Slack, send a direct message to your bot, now you can start chat!

