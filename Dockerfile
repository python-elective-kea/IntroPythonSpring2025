# Use an official Nginx image as a parent image
FROM nginx:alpine

# Set the working directory in the container
WORKDIR /usr/share/nginx/html

# Copy the current directory contents into the container at /usr/share/nginx/html
COPY . .

# Make port 80 available to the world outside this container
EXPOSE 80

# Run Nginx when the container launches
CMD ["nginx", "-g", "daemon off;"]
