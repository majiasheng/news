- had a typo on docker-compose.yml's mongo environment, *MONG* instead of *MONGO*. this caused connections to fail (auth failure). had to delete the volume