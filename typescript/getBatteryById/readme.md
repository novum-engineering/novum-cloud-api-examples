This just demonstrates fetching a battery by its id after successfull login. Each battery has a unique id in our database. This id is unique over all users. Keep in mind the name of the battery is not unique. It's just unique for the user (owner). If you share your batteries with others users multiple batteries with the same name can exist.

```bash
  # install dependencies
  yarn install
  # start example
  yarn start
```