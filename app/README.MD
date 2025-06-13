### Demo project
Build a simple python application,that reads a csv file(input.csv) from a folder called input,cleans it a little bit and then rewrties the cleaned csv file as cleaned_data.csv.
Create a docker file for the application ,build and run it.


### How to do it
Create a directory called app
```
mkdir app
```
Inside the directory run the following
```
mkdir input
touch Dockerfile
touch app.py
touch input/input.csv
```

Paste all the contents in the respective files


### How to build the application
In the directory where dockerfile lives,run the following command
```
docker build -t csv-cleaner .

```
### How to run the application
```
docker run --rm csv-cleaner
docker run -it csv-cleaner
```
--rm tells docker start the container but immediately remove it.

### To check the cleaned csv data
```
docker run -it csv-cleaner bin/bash
python app.py
cd output
cat cleaned_data.csv
```
Boom, you have your application dockerised.

### Next steps
Push the image to docker hub,to have ur own custom image


### License

[MIT](https://choosealicense.com/licenses/mit/)