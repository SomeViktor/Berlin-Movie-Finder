# Berlin-Movie-Finder
What are the single components?

- kino.py crawls a movie show time website for showtimes, names, address and name of the theater and the movie's genre.
  All data is saved to a mongo.db database in form of a kino event.
- geotager.py reads all untagged entries from the database and uses the google geotagger to geotagg every cinema.
- reqhan.p handles requests: it iterates over the database and searches for movie showing events in the next X hours, not   more than Y kilometes from the user away.
